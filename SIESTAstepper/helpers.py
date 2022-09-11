import os.path
import re
import shutil


def get_it(files):
    """Get a list of iterations"""
    try:
        return [int(re.search("/i([0-9]+)", f).groups(0)[0]) for f in files]
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
        newfdf.replace(re.search("(NumberOfAtoms +[0-9]+)", newfdf)[0], f"NumberOfAtoms   {number}")
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


def print_run(for_, cores, conda):
    """Print SIESTA's run information"""
    print(
        f"""Running SIESTA for {for_}
                {f' in parallel with {cores} cores' if cores is not None else ''}
                {' in conda' if conda else ''}"""
    )


def check_dm_xv(fdffile, i, label, cwd, cont):
    """Check DM and XV parameters in an FDF file"""
    fdf = fdffile.read()
    matchdm = re.search(r"#DM\.UseSaveDM +\.true\.", fdf)
    matchxv = re.search(r"#MD\.UseSaveXV +\.true\.", fdf)
    if matchdm is None:
        matchdm = re.search(r"DM\.UseSaveDM +\.false\.", fdf)
    if matchxv is None:
        matchxv = re.search(r"MD\.UseSaveXV +\.false\.", fdf)
    if matchdm is None:
        fdf += "\nDM.UseSaveDM        .true.\n"
    else:
        fdf.replace(matchdm[0], "DM.UseSaveDM        .true.")
    if matchxv is None:
        fdf += "\nMD.UseSaveXV        .true.\n"
    else:
        fdf.replace(matchxv[0], "MD.UseSaveXV        .true.")
    print(f"Setting 'DM.UseSaveDM' and 'MD.UseSaveXV' as '.true.' in {cwd}/i{i}/{cont}/{label}.fdf")
    fdffile.write(fdf)
    if re.search("WriteDM +.true.", fdf) is None or re.search("#WriteDM +.true.", fdf) is not None \
            or re.search("WriteDM +.false.", fdf) is not None:
        print(f"WARNING: 'WriteDM             .true.' not found in {cwd}/i{i}/{cont}/{label}.fdf")


def copy_file(sourcefile, destinationfile):
    """Copy and paste a file"""
    if not os.path.isfile(sourcefile):
        raise FileNotFoundError(f"ERROR: {sourcefile} is not found")
    try:
        print(f"Copying {sourcefile} to {destinationfile}")
        shutil.copy(sourcefile, destinationfile)
        print(f"{sourcefile} is copied to {destinationfile} successfully")
    except shutil.SameFileError:
        print(f"ERROR: {sourcefile} and {destinationfile} represents the same file")
    except PermissionError:
        print(f"ERROR: Permission denied while copying {sourcefile} to {destinationfile}")
    except Exception:
        print(f"ERROR: An error occurred while copying {sourcefile} to {destinationfile}")
