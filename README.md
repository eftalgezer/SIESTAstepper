# SIESTAstepper

SIESTAstepper runs SIESTA step by step, designed for constrained calculations.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install SIESTAstepper.

```bash
pip install SIESTAstepper
```

## Usage

All SIESTA working directories must be named as i1, i2, i3 ... and so on.

### In code
```python
import SIESTAstepper

#Sets the path of the working directory
SIESTAstepper.cwd = "path/to/working/directory"

#Sets the name of SIESTA log files (default is "log")
SIESTAstepper.log = "log"

# Runs SIESTA step by step
SIESTAstepper.run("graphene")

# Converts last geometry of an ANI to FDF by using the previous FDF and ANI files
SIESTAstepper.ani_to_fdf("path/to/ANI", "path/to/FDF", "path/to/newFDF")

# Converts XYZ to FDF by using the previous FDF and XYZ files
SIESTAstepper.xyz_to_fdf("path/to/XYZ", "path/to/FDF", "path/to/newFDF")

# Runs SIESTA a for given step
SIESTAstepper.run_next("1", "graphene")

# Plots and returns energies from log files
SIESTAstepper.analysis()

# Returns energies from log files without plotting
SIESTAstepper.analysis(plot_ = False)

# Plots and returns energies from log files by setting a path
SIESTAstepper.analysis(path = "path/to/i*/log/files")

# Plots and returns energies from log files by setting a missing files path
SIESTAstepper.analysis(missing = "path/to/missing/log/files")
```

### In terminal
```sh

python -m SIESTAstepper run log

python -m SIESTAstepper run_next log 1 graphene

python -m SIESTAstepper ani_to_fdf path/to/ANI path/to/FDF path/to/newFDF

python -m SIESTAstepper xyz_to_fdf path/to/XYZ path/to/FDF path/to/newFDF

python -m SIESTAstepper analysis log

python -m SIESTAstepper analysis log noplot

python -m SIESTAstepper analysis log path=path/to/i*/log/files

python -m SIESTAstepper analysis log missing=path/to/missing/log/files

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU General Public License v3.0](https://github.com/eftalgezer/SIESTAstepper/blob/master/LICENSE) 
