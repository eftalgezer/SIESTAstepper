import os
import re
import shutil


def get_it(files):
    """Get a list of iterations"""
    try:
        return [int(re.search(f"{os.sep}i([0-9]+)", f).groups(0)[0]) for f in files]
    except AttributeError:
        print(f"ERROR: The path must be in format of 'path{os.sep}to{os.sep}i1'")


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
        match = re.search("(NumberOfAtoms +[0-9]+)", newfdf)
        if match is not None:
            newfdf.replace(match[0], f"NumberOfAtoms   {number}")
        else:
            newfdf += f"\nNumberOfAtoms   {number}\n"
        newfdffile.write(newfdf)
        print(f"{newfdfpath} is created")
        newfdffile.close()


def read_energy(energies=[], files=None, it=[], print_=True):
    """Read energy from log file"""
    it += get_it(files)
    for f in files:
        if print_:
            print(f)
        with open(f, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("siesta:         Total =  "):
                    energies.append(float(line.split("=  ")[1]))
                    if print_:
                        print(line.split("=  ")[1])


def print_run(for_, cores, conda):
    """Print SIESTA's run information"""
    print(
        f"""Running SIESTA for {for_}
                {f' in parallel with {cores} cores' if cores is not None else ''}
                {' in conda' if conda else ''}"""
    )


def check_restart(fdffile, i, label, cwd, cont, contextensions):
    """Check DM and XV parameters in an FDF file"""
    fdf = fdffile.read()
    if "DM" in contextensions:
        matchdm = re.search(r"# *DM\.UseSaveDM +\.true\.", fdf)
        if matchdm is None:
            matchdm = re.search(r"DM\.UseSaveDM +\.false\.", fdf)
        if matchdm is None:
            fdf += "\nDM.UseSaveDM        .true.\n"
        else:
            print(f"Setting 'DM.UseSaveDM' as '.true.' in {cwd}{os.sep}i{i}{os.sep}{cont}{os.sep}{label}.fdf")
            fdf.replace(matchdm[0], "DM.UseSaveDM        .true.")
        if re.search("WriteDM +.true.", fdf) is None or re.search("# *WriteDM +.true.", fdf) is not None \
                or re.search("WriteDM +.false.", fdf) is not None:
            print(
                f"WARNING: 'WriteDM             .true.' not found in {cwd}{os.sep}i{i}{os.sep}{cont}{os.sep}{label}.fdf"
            )
    if "XV" in contextensions:
        matchxv = re.search(r"# *MD\.UseSaveXV +\.true\.", fdf)
        if matchxv is None:
            matchxv = re.search(r"MD\.UseSaveXV +\.false\.", fdf)
        if matchxv is None:
            print(f"Setting 'MD.UseSaveXV' as '.true.' in {cwd}{os.sep}i{i}{os.sep}{cont}{os.sep}{label}.fdf")
            fdf += "\nMD.UseSaveXV        .true.\n"
        else:
            print(f"Setting 'MD.UseSaveXV' as '.true.' in {cwd}{os.sep}i{i}{os.sep}{cont}{os.sep}{label}.fdf")
            fdf.replace(matchxv[0], "MD.UseSaveXV        .true.")
    if "CG" in contextensions:
        matchcg = re.search(r"# *MD\.UseSaveCG +\.true\.", fdf)
        if matchcg is None:
            matchcg = re.search(r"MD\.UseSaveCG +\.false\.", fdf)
        if matchcg is None:
            print(f"Setting 'MD.UseSaveCG' as '.true.' in {cwd}{os.sep}i{i}{os.sep}{cont}{os.sep}{label}.fdf")
            fdf += "\nMD.UseSaveCG        .true.\n"
        else:
            print(f"Setting 'MD.UseSaveCG' as '.true.' in {cwd}{os.sep}i{i}{os.sep}{cont}{os.sep}{label}.fdf")
            fdf.replace(matchcg[0], "MD.UseSaveCG        .true.")
    if "LWF" in contextensions:
        matchlwf = re.search(r"# *ON\.UseSaveLWF +\.true\.", fdf)
        if matchlwf is None:
            matchlwf = re.search(r"ON\.UseSaveLWF +\.false\.", fdf)
        if matchlwf is None:
            print(f"Setting 'ON.UseSaveLWF' as '.true.' in {cwd}{os.sep}i{i}{os.sep}{cont}{os.sep}{label}.fdf")
            fdf += "\nON.UseSaveLWF        .true.\n"
        else:
            print(f"Setting 'ON.UseSaveLWF' as '.true.' in {cwd}{os.sep}i{i}{os.sep}{cont}{os.sep}{label}.fdf")
            fdf.replace(matchlwf[0], "ON.UseSaveLWF        .true.")
    fdffile.write(fdf)

def check_userbasis(fdffile):
    with open(fdffile, "r") as f:
        if re.search("Userbasis *\.true\.", f.read()):
            return True
        f.close()
        return False

def copy_file(sourcefile, destinationfile):
    """Copy and paste a file"""
    if not os.path.isfile(sourcefile):
        raise FileNotFoundError(f"ERROR: {sourcefile} is not found")
    try:
        print(f"Copying {sourcefile} to {destinationfile}")
        if not os.path.isfile(destinationfile):
            shutil.copy(sourcefile, destinationfile)
            print(f"{sourcefile} is copied to {destinationfile} successfully")
        else:
            print(f"{destinationfile} exists")
    except shutil.SameFileError:
        print(f"ERROR: {sourcefile} and {destinationfile} represents the same file")
    except PermissionError:
        print(f"ERROR: Permission denied while copying {sourcefile} to {destinationfile}")
    except Exception:
        print(f"ERROR: An error occurred while copying {sourcefile} to {destinationfile}")


def sort_(files, path, cont):
    """Naive sort function for directories"""
    path = path.replace("*", "([0-9]+)")
    sortedfiles = []
    match = [re.search(f"{path}({os.sep}{cont}_*([0-9]*))*", f) for f in files]
    sortedmatch = [[m[0], m[1], m[2], m[3]] for m in match]
    sortedmatch = [x for _, x in sorted(zip(
        [int(f"{m[1]}0") if m[3] is None else int(f"{m[1]}1") if m[3] == "" else int(m[1] + m[3]) for m in
         sortedmatch
         ], sortedmatch
    ))]
    for s in sortedmatch:
        for f in files:
            fmatch = re.search(f"{path}({os.sep}{cont}_*([0-9]*))*", f)
            if s[0] == fmatch[0] and f not in sortedfiles:
                sortedfiles.append(f)
    return sortedfiles


def remove_nones(files, path, cwd, cont, log):
    """Remove the files which do not return any energy values"""
    path = path.replace("*", "[0-9]+")
    active_log = {}
    to_remove = []
    for filename in files:
        logmatch = re.search(
            f"({cwd}{os.sep}({path})({os.sep}{cont}(_([0-9]+))?)?{os.sep}{log})", filename
        )
        if not logmatch:
            continue
        _, instance, extended, _, increment = logmatch.groups()
        lognumber = 0
        if extended is not None:
            lognumber = 1 if increment is None else int(increment)
        if instance not in active_log:
            active_log[instance] = (lognumber, filename)
        elif active_log[instance][0] > lognumber:
            to_remove.append(filename)
        else:
            to_remove.append(active_log[instance][1])
            active_log[instance] = (lognumber, filename)
    for filename in to_remove:
        files.remove(filename)
