import glob
import os
import time
import matplotlib.pyplot as plt
from sh import tail
from itertools import zip_longest
import re
from .helpers import create_fdf, read_fdf, read_energy, get_it

cwd = os.getcwd()
log = "log"
cores = None
conda = None


def run_next(i, label):
    """Run SIESTA for given step"""
    os.chdir(f"{cwd}/i{i}")
    print(f"Changed directory to {os.getcwd()}")
    print(
        f"""Running SIESTA for i{i}
        {f' in parallel with {cores} cores' if cores is not None else ''}
        {' in conda' if conda else ''}"""
    )
    if conda:
        os.system(f"conda activate {conda}")
    os.system(f"{f'mpirun -np {cores} ' if cores is not None else ''}siesta {label}.fdf > {log} &")
    for line in tail("-f", log, _iter=True):
        print(line)
        if line == "Job completed\n":
            run(label)


def ani_to_fdf(anipath, fdfpath, newfdfpath):
    """Convert last geometry of an ANI to FDF by using the previous FDF and ANI files"""
    print(f"Reading {anipath}")
    with open(anipath, "r") as anifile:
        geo = anifile.read()
        number = geo.split("\n", 1)[0].strip()
        geo = geo.split(number + "\n \n")[-1]
        geo = geo.splitlines()
        fdf, geo = read_fdf(fdfpath, geo)
        create_fdf(fdf, geo, newfdfpath)
        anifile.close()


def xyz_to_fdf(xyzpath, fdfpath, newfdfpath):
    """Convert XYZ to FDF by using the previous FDF and XYZ files"""
    print(f"Reading {xyzpath}")
    with open(xyzpath, "r") as xyzfile:
        geo = xyzfile.read()
        geo = geo.splitlines()[2:]
        fdf, geo = read_fdf(fdfpath, geo)
        create_fdf(fdf, geo, newfdfpath)
        xyzfile.close()


def merge_ani(label=None, path=None, missing=None):
    """Merge ANI files"""
    if path is None:
        path = "i*"
    if label is None:
        raise ValueError("ERROR: Please set a label")
    files = list(glob.glob(f"{cwd}/{path}/{label}.ANI"))
    if missing is not None:
        files += list(glob.glob(f"{cwd}/{path}/{missing}/{label}.ANI"))
    files.sort(key=lambda _: int(re.sub("\D""", "", _)))
    if files:
        it = get_it(files)
        if it != list(range(min(it), max(it) + 1)):
            print("WARNING: There are missing ANI files!")
        with open(f"{cwd}/{label}-merged.ANI", "w") as outfile:
            print(f"{cwd}/{label}-merged.ANI is opened")
            for f in files:
                with open(f) as infile:
                    print(f"Writing {f}")
                    content = infile.read()
                    outfile.write(content)
                    infile.close()
            outfile.close()
        print("All ANI files are merged")
    else:
        print("No ANI files found")


def run(label):
    """Execute"""
    os.chdir(cwd)
    folders = glob.glob("*/")
    logs = glob.glob(f"*/{log}")
    if len(logs) == 0:
        run_next("1", label)
    elif len(folders) != len(logs) != 0 or folders[-1] != logs[-1].split("/")[0] + "/":
        with open(logs[-1], "r") as file:
            lines = file.readlines()
            if lines[-1] == "Job completed\n":
                print(f"{logs[-1]}: Job completed")
                if not os.path.isfile(
                        f"{cwd}/i" + str(int(logs[-1].split("/")[0].strip("i")) + 1) + "/" + label + ".fdf"):
                    ani_to_fdf(
                        logs[-1].split("/")[0] + "/" + label + ".ANI",
                        logs[-1].split("/")[0] + "/" + label + ".fdf",
                        "i" + str(int(logs[-1].split("/")[0].strip("i")) + 1) + "/" + label + ".fdf"
                    )
                file.close()
                run_next(str(int(logs[-1].split("/")[0].strip("i")) + 1), label)
            else:
                print(f"{logs[-1]}: Job is not completed")
                print("Snoozing for 15 minutes")
                time.sleep(900)
                run(label)
    print("All iterations are completed")
    if conda:
        os.system("conda deactivate")


def analysis(path=None, missing=None, plot_=True):
    """Plot and return energies from log files"""
    if path is None:
        path = "i*"
    files = glob.glob(f"{cwd}/{path}/{log}")
    energies = []
    it = []
    read_energy(energies=energies, files=files, it=it)
    if sorted(it) != list(range(min(it), max(it) + 1)) and missing is None:
        print("WARNING: There are missing values! Please set 'missing' parameter.")
    if missing is not None:
        files = glob.glob(f"{cwd}/{path}/{missing}/{log}")
        read_energy(energies=energies, files=files, it=it)
    if plot_:
        plt.scatter(it, energies)
        plt.xlabel("Step")
        plt.ylabel("Energy (eV)")
        plt.show()
    return sorted(list(zip_longest(it, energies)), key=lambda x: x[0])
