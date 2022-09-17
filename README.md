# SIESTAstepper
[![PyPI version](https://badge.fury.io/py/SIESTAstepper.svg)](https://badge.fury.io/py/SIESTAstepper)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
[![Python package](https://github.com/eftalgezer/SIESTAstepper/actions/workflows/python-package.yml/badge.svg)](https://github.com/eftalgezer/SIESTAstepper/actions/workflows/python-package.yml)
[![PyPI download month](https://img.shields.io/pypi/dm/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
[![PyPI download week](https://img.shields.io/pypi/dw/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
[![PyPI download day](https://img.shields.io/pypi/dd/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
![GitHub all releases](https://img.shields.io/github/downloads/eftalgezer/SIESTAstepper/total?style=flat)
[![GitHub contributors](https://img.shields.io/github/contributors/eftalgezer/SIESTAstepper.svg)](https://github.com/eftalgezer/SIESTAstepper/graphs/contributors/)
[![CodeFactor](https://www.codefactor.io/repository/github/eftalgezer/siestastepper/badge)](https://www.codefactor.io/repository/github/eftalgezer/siestastepper)
[![PyPI license](https://img.shields.io/pypi/l/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
[![DOI](https://zenodo.org/badge/532944393.svg)](https://zenodo.org/badge/latestdoi/532944393)

SIESTAstepper runs SIESTA step by step, designed for constrained calculations.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install SIESTAstepper.

```bash
$ pip install SIESTAstepper

# to make sure you have the latest version
$ pip install -U SIESTAstepper

# latest available code base
$ pip install -U git+https://github.com/eftalgezer/SIESTAstepper.git
```

## Tutorial

- [SIESTAstepper v1.0.0 tutorial](https://beyondthearistotelian.blogspot.com/2022/09/siestastepper-v100-tutorial.html)
- [SIESTAstepper v1.1.0 tutorial](https://beyondthearistotelian.blogspot.com/2022/09/siestastepper-v110-tutorial.html)
- [What is new in SIESTAstepper v1.2.0?](https://beyondthearistotelian.blogspot.com/2022/09/what-is-new-in-siestastepper-v120.html)

## Usage

All SIESTA working directories must be named as i1, i2, i3 ... and so on.

### In code

#### Simple usage

```python
SIESTAstepper.run("graphene")

```

#### Advance usage

```python
import SIESTAstepper

# Sets the path of the working directory
SIESTAstepper.update_cwd("path/to/working/directory")

# Sets the name of SIESTA log files (default is "log")
SIESTAstepper.update_log("log")

# Sets number of cores for parallel run
SIESTAstepper.update_cores(4)

# Sets Anaconda environment
SIESTAstepper.update_conda("envir")

# Sets the subfolder name for interrupted calculations (default is "continue")
SIESTAstepper.update_cont("continue")

# Sets the SIESTA command name (default is "siesta")
SIESTAstepper.update_siesta("siesta_p")

# Sets the filenames to copy (useful for interrupted calculations)
SIESTAstepper.contfiles.extend(["file1", "file2"])

# Sets the extensions to copy (useful for interrupted calculations, default is ["psf, "fdf"]
SIESTAstepper.contextensions.extend(["DM", "XV", "CG", "LWF"])

# Runs SIESTA step by step
SIESTAstepper.run("graphene")

# Converts last geometry of an ANI to FDF by using the previous FDF and ANI files
SIESTAstepper.ani_to_fdf("path/to/ANI", "path/to/FDF", "path/to/newFDF")

# Converts XYZ to FDF by using the previous FDF and XYZ files
SIESTAstepper.xyz_to_fdf("path/to/XYZ", "path/to/FDF", "path/to/newFDF")

# Merges ANI files
SIESTAstepper.merge_ani(label = "graphene")

# Merges ANI files by setting a path
SIESTAstepper.merge_ani(label = "graphene", path = "path/to/i*/ANI/files")

# Runs SIESTA for a given step
SIESTAstepper.run_next("1", "graphene")

# Runs SIESTA for a given step without continuing to next step
SIESTAstepper.single_run("1", "graphene")

# Continues to an interrupted calculation without continuing to next step
SIESTAstepper.single_run_interrupted("1", "graphene")

# Continues to an interrupted calculation
SIESTAstepper.run_interrupted("1", "graphene")

# Creates folders named i1, i2, i3, i4, i5, ...
SIESTAstepper.make_directories(5)

# Copies files from i1 to i2
SIESTAstepper.copy_files(["psf", "fdf", "XV", "DM"], "graphene", "path/to/i1", "path/to/i2")

# Plots and returns energies from log files
SIESTAstepper.analysis()

# Returns energies from log files without plotting
SIESTAstepper.analysis(plot_ = False)

# Plots and returns energies from log files by setting a path
SIESTAstepper.analysis(path = "path/to/i*/log/files")

# Calculates the energy differences between minima and maxima
SIESTAstepper.energy_diff()

# Calculates the energy differences between minima and maxima by setting a path
SIESTAstepper.energy_diff(path = "path/to/i*/log/files")
```

### In terminal

#### Simple usage

```sh
$ python -m SIESTAstepper run log graphene
```

#### Advance usage

```sh
$ python -m SIESTAstepper run log graphene

$ python -m SIESTAstepper run log graphene contfiles=file1,file2 contextensions=DM,XV,CG,LWF

$ python -m SIESTAstepper run log graphene mpirun=4

$ python -m SIESTAstepper run log graphene conda=envir

$ python -m SIESTAstepper run log graphene siesta=siesta_p

$ python -m SIESTAstepper run_next log 1 graphene

$ python -m SIESTAstepper run_next log 1 graphene contfiles=file1,file2 contextensions=DM,XV,CG,LWF

$ python -m SIESTAstepper run_next log 1 graphene mpirun=4

$ python -m SIESTAstepper run_next log 1 graphene conda=envir

$ python -m SIESTAstepper run_next log 1 graphene siesta=siesta_p

$ python -m SIESTAstepper single_run log 1 graphene

$ python -m SIESTAstepper single_run log 1 graphene mpirun=4

$ python -m SIESTAstepper single_run log 1 graphene conda=envir

$ python -m SIESTAstepper single_run log 1 graphene siesta=siesta_p

$ python -m SIESTAstepper run_interrupted log 1 graphene cont=continue

$ python -m SIESTAstepper run_interrupted log 1 graphene cont=continue contfiles=file1,file2 contextensions=DM,XV,CG,LWF

$ python -m SIESTAstepper run_interrupted log 1 graphene mpirun=4 cont=continue

$ python -m SIESTAstepper run_interrupted log 1 graphene conda=envir cont=continue

$ python -m SIESTAstepper run_interrupted log 1 graphene siesta=siesta_p cont=continue

$ python -m SIESTAstepper single_run_interrupted log 1 graphene cont=continue

$ python -m SIESTAstepper single_run_interrupted log 1 graphene mpirun=4 cont=continue

$ python -m SIESTAstepper single_run_interrupted log 1 graphene conda=envir cont=continue

$ python -m SIESTAstepper single_run_interrupted log 1 graphene siesta=siesta_p cont=continue

$ python -m SIESTAstepper make_directories 5

$ python -m SIESTAstepper copy_files graphene path/to/i1 path/to/i2 psf fdf XV DM

$ python -m SIESTAstepper copy_files graphene path/to/i1 path/to/i2 psf fdf XV DM

$ python -m SIESTAstepper ani_to_fdf path/to/ANI path/to/FDF path/to/newFDF

$ python -m SIESTAstepper xyz_to_fdf path/to/XYZ path/to/FDF path/to/newFDF

$ python -m SIESTAstepper merge_ani graphene

$ python -m SIESTAstepper merge_ani graphene cont=continue

$ python -m SIESTAstepper merge_ani graphene path=path/to/i*/ANI/files

$ python -m SIESTAstepper analysis log

$ python -m SIESTAstepper analysis log cont=continue

$ python -m SIESTAstepper analysis log noplot

$ python -m SIESTAstepper analysis log path=path/to/i*/log/files

$ python -m SIESTAstepper energy_diff log

$ python -m SIESTAstepper energy_diff log cont=continue

$ python -m SIESTAstepper energy_diff log path=path/to/i*/log/files

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Citation
If you are using SIESTAstepper, please citate relevant version. You can find the relevant citation [here](https://doi.org/10.5281/zenodo.7051271).

```bibtex
@software{eftal_gezer_2022_7085961,
  author       = {Eftal Gezer},
  title        = {eftalgezer/SIESTAstepper: v1.2.1},
  month        = sep,
  year         = 2022,
  publisher    = {Zenodo},
  version      = {v1.2.1},
  doi          = {10.5281/zenodo.7085961},
  url          = {https://doi.org/10.5281/zenodo.7085961}
}
```

## License
[GNU General Public License v3.0](https://github.com/eftalgezer/SIESTAstepper/blob/master/LICENSE) 
