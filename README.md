# SIESTAstepper
[![PyPI version](https://badge.fury.io/py/SIESTAstepper.svg)](https://badge.fury.io/py/SIESTAstepper)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
[![Python package](https://github.com/eftalgezer/SIESTAstepper/actions/workflows/python-package.yml/badge.svg)](https://github.com/eftalgezer/SIESTAstepper/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/eftalgezer/SIESTAstepper/branch/main/graph/badge.svg?token=Q9TJFIN1U1)](https://codecov.io/gh/eftalgezer/SIESTAstepper)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/4ff526bd45e642bb81b300f2243baef2)](https://www.codacy.com/gh/eftalgezer/SIESTAstepper/dashboard?utm_source=github.com&utm_medium=referral&utm_content=eftalgezer/SIESTAstepper&utm_campaign=Badge_Coverage)
[![PyPI download month](https://img.shields.io/pypi/dm/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
[![PyPI download week](https://img.shields.io/pypi/dw/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
[![PyPI download day](https://img.shields.io/pypi/dd/SIESTAstepper.svg)](https://pypi.python.org/pypi/SIESTAstepper/)
![GitHub all releases](https://img.shields.io/github/downloads/eftalgezer/SIESTAstepper/total?style=flat)
[![GitHub contributors](https://img.shields.io/github/contributors/eftalgezer/SIESTAstepper.svg)](https://github.com/eftalgezer/SIESTAstepper/graphs/contributors/)
[![CodeFactor](https://www.codefactor.io/repository/github/eftalgezer/siestastepper/badge)](https://www.codefactor.io/repository/github/eftalgezer/siestastepper)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/4ff526bd45e642bb81b300f2243baef2)](https://www.codacy.com/gh/eftalgezer/SIESTAstepper/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=eftalgezer/SIESTAstepper&amp;utm_campaign=Badge_Grade)
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
- [SIESTAstepper v2.0.0 tutorial](https://beyondthearistotelian.blogspot.com/2022/09/siestastepper-v200-tutorial.html)

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
SIESTAstepper.settings.set_cwd("path/to/working/directory")

# Sets the name of SIESTA log files (default is "log")
SIESTAstepper.settings.set_log("log")

# Sets number of cores for parallel run
SIESTAstepper.settings.set_cores(4)

# Sets Anaconda environment
SIESTAstepper.settings.set_conda("envir")

# Sets the subfolder name for interrupted calculations (default is "continue")
SIESTAstepper.settings.set_cont("continue")

# Sets the SIESTA command name (default is "siesta")
SIESTAstepper.settings.set_siesta("siesta_p")

#Sets the file type to continue next step (default is "log", possible values are "log", "XV", "ANI")
SIESTAstepper.settings.set_contfrom("ANI")

# Sets the filenames to copy (useful for interrupted calculations)
SIESTAstepper.settings.contfiles.extend(["file1", "file2"])

# Sets the extensions to copy (useful for interrupted calculations, default is ["psf, "fdf"]
SIESTAstepper.settings.contextensions.extend(["DM", "XV", "CG", "LWF"])

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

# Creates GIF file from a given ANI
SIESTAstepper.ani_to_gif(anifile="graphene.ANI")

# Creates GIF file from a given ANI by setting width and height (defaults are 1920 and 1080, respectively)
SIESTAstepper.ani_to_gif(anifile="graphene.ANI", width=1920, height=1080)

# Creates GIF file from a given ANI by setting the bonds between atoms (default is 1.3)
SIESTAstepper.ani_to_gif(anifile="graphene.ANI", bonds_param=1.3)

# Creates GIF file from a given ANI by setting loop (default is 0; 0 means loop, 1 means no loop)
SIESTAstepper.ani_to_gif(anifile="graphene.ANI", loop=1)

# Creates GIF file from a given ANI by setting camera
SIESTAstepper.ani_to_gif(anifile="graphene.ANI", camera=((40, 0, 0),
                                                        (0, 0, 0),
                                                        (0, 1, 0)))

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
SIESTAstepper.energy_analysis()

# Returns energies from log files without plotting
SIESTAstepper.energy_analysis(plot_ = False)

# Plots and returns energies from log files by setting a path
SIESTAstepper.energy_analysis(path = "path/to/i*/log/files")

# Calculates the energy differences between minima and maxima
SIESTAstepper.energy_diff()

# Calculates the energy differences between minima and maxima by setting a path
SIESTAstepper.energy_diff(path = "path/to/i*/log/files")

# Plots and returns forces from log files (defaults are "Tot" and "atomic", respectively)
SIESTAstepper.force_analysis(atomindex="Tot", forcetype="atomic")

# Returns forces from log files without plotting
SIESTAstepper.force_analysis(plot_ = False)

# Plots and returns forces from log files by setting a path
SIESTAstepper.force_analysis(path = "path/to/i*/log/files")

# Calculates the force differences between minima and maxima (defaults are "Tot" and "atomic", respectively)
SIESTAstepper.force_diff(atomindex="Tot", forcetype="atomic")

# Calculates the force differences between minima and maxima by setting a path
SIESTAstepper.force_diff(path = "path/to/i*/log/files")

# Calculates the pair correlation function
SIESTAstepper.pair_correlation_function(label="graphene")

# Calculates the pair correlation function without plotting
SIESTAstepper.pair_correlation_function(label="graphene", plot_=True)

# Calculates the pair correlation function by setting a path
SIESTAstepper.pair_correlation_function(label="graphene", path="path/to/i*")

# Calculates the pair correlation function by setting infinitesimal dr parameter
SIESTAstepper.pair_correlation_function(label="graphene", dr=0.1)
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

$ python -m SIESTAstepper ani_to_gif graphene.ANI 1920 1080 1 1.3

$ python -m SIESTAstepper ani_to_gif graphene.ANI 1920 1080 1 1.3 camera=40,0,0,0,0,0,0,1,0

$ python -m SIESTAstepper energy_analysis log

$ python -m SIESTAstepper energy_analysis log cont=continue

$ python -m SIESTAstepper energy_analysis log noplot

$ python -m SIESTAstepper energy_analysis log path=path/to/i*/log/files

$ python -m SIESTAstepper energy_diff log

$ python -m SIESTAstepper energy_diff log cont=continue

$ python -m SIESTAstepper energy_diff log path=path/to/i*/log/files

$ python -m SIESTAstepper force_analysis log atomic Tot

$ python -m SIESTAstepper force_analysis log atomic Tot cont=continue

$ python -m SIESTAstepper force_analysis log atomic Tot noplot

$ python -m SIESTAstepper force_analysis log atomic Tot path=path/to/i*/log/files

$ python -m SIESTAstepper force_diff log atomic Tot

$ python -m SIESTAstepper energy_diff log atomic Tot cont=continue

$ python -m SIESTAstepper energy_diff log atomic Tot path=path/to/i*/log/files

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Citation
If you are using SIESTAstepper, please citate relevant version. You can find the relevant citation [here](https://doi.org/10.5281/zenodo.7051271).

```bibtex
@software{eftal_gezer_2022_7212472,
  author       = {Eftal Gezer},
  title        = {eftalgezer/SIESTAstepper: v2.1.0},
  month        = oct,
  year         = 2022,
  publisher    = {Zenodo},
  version      = {v2.1.0},
  doi          = {10.5281/zenodo.7212472},
  url          = {https://doi.org/10.5281/zenodo.7212472}
}
```

## License
[GNU General Public License v3.0](https://github.com/eftalgezer/SIESTAstepper/blob/master/LICENSE) 

## Acknowledgments

`ani_to_gif` function uses [ANIAnimator](https://github.com/eftalgezer/ANIAnimator).

## References

Eftal Gezer. (2022). eftalgezer/ANIAnimator: v0.2.1 (v0.2.1). Zenodo. https://doi.org/10.5281/zenodo.7182193
