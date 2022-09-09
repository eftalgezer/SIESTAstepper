import re
import shutil
import glob
from sh import tail
from subprocess import Popen
from subprocess import run as sprun
import shlex
from .core import run, run_next


def get_it(files):
    """Get a list of iterations"""
    try:
        return [int(re.search("/i[0-9]+", f)[0].strip("/i")) for f in files]
    except AttributeError:
        print("ERROR: The path must be in format of 'path/to/i1'")


def read_fdf(fdfpath, geo):
    """Read FDF file"""
    print(f"Reading {fdfpath}")
    with open(fdfpath, "r") as fdffile:
        fdf = fdffile.read()
        ind = fdf.split("%block ChemicalSpeciesLabel\n")[1].split("%endblock ChemicalSpeciesLabel\n")[0]
        ind = ind.splitlines()
        for i in ind:
            for g in geo:
                if g[0] == i[-1]:
                    geo[geo.index(g)] = f"{g}  " + re.split(" +", i)[0]
                    g = f"{g}  " + re.split(" +", i)[0]
                    geo[geo.index(g)] = geo[geo.index(g)].strip(i[-1])
    return fdf, geo


def create_fdf(fdf, geo, newfdfpath, number):
    """Create new FDF file"""
    print(f"Creating {newfdfpath}")
    with open(newfdfpath, "w") as newfdffile:
        newfdf = fdf.split("%block AtomicCoordinatesAndAtomicSpecies\n")[0]
        newfdf += "%block AtomicCoordinatesAndAtomicSpecies\n"
        for g in geo:
            newfdf += g + "\n"
        newfdf += "%endblock AtomicCoordinatesAndAtomicSpecies\n"
        newfdf.replace(re.search("(NumberOfAtoms +[0-9]+)")[0], f"NumberOfAtoms   {number}")
        newfdffile.write(newfdf)
        print(f"{newfdfpath} is created")
        newfdffile.close()


def read_energy(energies=[], files=None, it=[]):
    """Read energy from log file"""
    it += get_it(files)
    for f in files:
        print(f)
        with open(f, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("siesta:         Total =  "):
                    energies.append(float(line.split("=  ")[1]))
                    print(line.split("=  ")[1])


def copy_files(extensions, label, source_, destination):
    """Copy and paste files"""
    for ext in extensions:
        if ext == "psf":
            files = glob.glob(f"{source_}/*.psf")
            for f in files:
                file = f.split("/")[-1]
                try:
                    print(f"Copying {f} to {destination}/{file}")
                    shutil.copy(f"{f}", f"{destination}/{file}")
                    print(f"{f} is copied to {destination}/{file} successfully")
                except shutil.SameFileError:
                    print(f"ERROR: {f} and {destination}/{file} represents the same file")
                except PermissionError:
                    print(f"ERROR: Permission denied while copying {f} to {destination}/{file}")
                except Exception:
                    print(f"ERROR: An error occurred while copying {f} to {destination}/{file}")
        else:
            try:
                print(f"Copying {source_}/{label}.{ext} to {destination}/{label}.{ext}")
                shutil.copy(f"{source_}/{label}.{ext}", f"{destination}/{label}.{ext}")
                print(f"{source_}/{label}.{ext} is copied to {destination}/{label}.{ext} successfully")
            except shutil.SameFileError:
                print(f"ERROR: {source_}/{label}.{ext} and {destination}/{label}.{ext} represents the same file")
            except PermissionError:
                print(f"ERROR: Permission denied while copying {source_}/{label}.{ext} to {destination}/{label}.{ext}")
            except Exception:
                print(f"ERROR: An error occurred while copying {source_}/{label}.{ext} to {destination}/{label}.{ext}")


def print_run(for_, cores, conda):
    """Print SIESTA's run information"""
    print(
        f"""Running SIESTA for {for_}
                {f' in parallel with {cores} cores' if cores is not None else ''}
                {' in conda' if conda else ''}"""
    )


def command(runtype=None, label=None, log=None, conda=None, cores=None, i=None):
    """SIESTA's run command"""
    if conda:
        sprun(["conda", "activate", conda])
    with open(log, "w") as logger:
        Popen(
            shlex.split(f"{f'mpirun -np {cores} ' if cores is not None else ''}siesta {label}.fdf > {log}"),
            stdout=logger
        )
        for line in tail("-f", log, _iter=True):
            print(line)
            if line == "Job completed\n":
                if runtype == "run":
                    run(label)
                if runtype == "run_next":
                    run_next(i, label)
