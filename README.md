# SIESTAstepper
[![PyPI version](https://badge.fury.io/py/SIESTAstepper.svg)](https://badge.fury.io/py/SIESTAstepper)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
[![PyPI download month](https://img.shields.io/pypi/dm/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
[![PyPI download week](https://img.shields.io/pypi/dw/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
[![PyPI download day](https://img.shields.io/pypi/dd/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
![GitHub all releases](https://img.shields.io/github/downloads/eftalgezer/SIESTAstepper/total?style=flat)
[![GitHub contributors](https://img.shields.io/github/contributors/eftalgezer/SIESTAstepper.svg)](https://github.com/eftalgezer/SIESTAstepper/graphs/contributors/)
[![PyPI license](https://img.shields.io/pypi/l/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
[![DOI](https://zenodo.org/badge/532944393.svg)](https://zenodo.org/badge/latestdoi/532944393)

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

## Citation
```bibtex
@software{eftal_gezer_2022_7051272,
  author       = {Eftal Gezer},
  title        = {eftalgezer/SIESTAstepper: v0.1.0},
  month        = sep,
  year         = 2022,
  publisher    = {Zenodo},
  version      = {v0.1.0},
  doi          = {10.5281/zenodo.7051272},
  url          = {https://doi.org/10.5281/zenodo.7051272}
}
```

## License
[GNU General Public License v3.0](https://github.com/eftalgezer/SIESTAstepper/blob/master/LICENSE) 
