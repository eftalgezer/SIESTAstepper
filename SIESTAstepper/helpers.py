import re


def create_fdf(fdf, geo, newfdfpath):
    """Create new FDF file"""
    print(f"Creating {newfdfpath}")
    with open(newfdfpath, "w") as newfdffile:
        newfdf = fdf.split("%block AtomicCoordinatesAndAtomicSpecies\n")[0]
        newfdf += "%block AtomicCoordinatesAndAtomicSpecies\n"
        for g in geo:
            newfdf += g + "\n"
        newfdf += "%endblock AtomicCoordinatesAndAtomicSpecies\n"
        newfdffile.write(newfdf)
        print(f"{newfdfpath} is created")
        newfdffile.close()


def read_energy(energies=[], files=None, it=[]):
    """Read energy from log file"""
    found = None
    for f in files:
        try:
            found = re.search("/i[0-9]+", f)[0]
        except AttributeError:
            print("The path must be in format of 'path/to/i1/log'")
        print(f)
        with open(f, "r") as file:
            lines = file.readlines()
            for l in lines:
                if l.startswith("siesta:         Total =  "):
                    energies.append(float(l.split("=  ")[1]))
                    print(l.split("=  ")[1])
                    it.append(int(found.strip("/i")))
