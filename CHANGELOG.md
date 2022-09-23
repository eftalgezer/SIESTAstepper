# Changelog

## [v2.0.0](https://github.com/eftalgezer/SIESTAstepper/tree/v2.0.0) (2022-09-23)

- Bug fix
- Linting
- `update_cwd`, `update_log`, `update_cores`, `update_conda`, `update_cont`, `update_siesta`, `contfiles`, ND `contextensions` are moved in `SIESTAstepper.settings` and renamed. You can reach those by `SIESTAstepper.settings.set_cwd`, `SIESTAstepper.settings.set_log`, `SIESTAstepper.settings.set_cores`, `SIESTAstepper.settings.set_conda`, `SIESTAstepper.settings.set_cont`, `SIESTAstepper.settings.set_siesta`, `SIESTAstepper.settings.contfiles`, and `SIESTAstepper.settings.contextensions`, respectively.
- `SIESTAstepper.settings.get_cwd`, `SIESTAstepper.settings.get_log`, `SIESTAstepper.settings.get_cores`, `SIESTAstepper.settings.get_conda`, `SIESTAstepper.settings.get_cont`, and `SIESTAstepper.settings.get_siesta` are added.
- The previous version was checking the restart parameters and the `Userbasis` parameter in a fdf file by `.true.` and `.false.`. `T` and `F` support is added.
- More tests are added.
- [A tutorial for SIESTAstepper v2.0.0](https://beyondthearistotelian.blogspot.com/2022/09/siestastepper-v200-tutorial.html) is published.

**Full Changelog**: https://github.com/eftalgezer/SIESTAstepper/compare/v1.2.2...v2.0.0

## [v1.2.3](https://github.com/eftalgezer/SIESTAstepper/tree/v1.2.3) (2022-09-19)

Bug fix

**Full Changelog**: https://github.com/eftalgezer/SIESTAstepper/compare/v1.2.2...v1.2.3

## [v1.2.2](https://github.com/eftalgezer/SIESTAstepper/tree/v1.2.2) (2022-09-19)

- Tests added
- Bug fix

**Full Changelog**: https://github.com/eftalgezer/SIESTAstepper/compare/v1.2.1...v1.2.2

## [v1.2.1](https://github.com/eftalgezer/SIESTAstepper/tree/v1.2.1) (2022-09-16)

Bug fix

**Full Changelog**: https://github.com/eftalgezer/SIESTAstepper/compare/v1.2.0...v1.2.1

## [v1.2.0](https://github.com/eftalgezer/SIESTAstepper/tree/v1.2.0) (2022-09-16)

- CG and LWF support to continue interrupted calculations
- ion support as a pseudopotential file
- `update_siesta` function is added. It is possible to change the SIESTA run command.

For details, please see [What is new in SIESTAstepper v1.2.0?](https://beyondthearistotelian.blogspot.com/2022/09/what-is-new-in-siestastepper-v120.html)

**Full Changelog**: https://github.com/eftalgezer/SIESTAstepper/compare/v1.1.0...v1.2.0

## [v1.1.0](https://github.com/eftalgezer/SIESTAstepper/tree/v1.1.0) (2022-09-15)

- `energy_diff` function is added. It is possible to get energy differences between minima and maxima.
- Bug fixes
- - The bug on the file name sort is fixed.
- - `update_cwd`, `update_log`, `update_cores`, `update_conda`, and `update_cont` functions are added to change the values of `cwd`, `log`, `cores`, `conda`, and `cont`, respectively.
- [A tutorial for v1.1.0 is written](https://beyondthearistotelian.blogspot.com/2022/09/siestastepper-v110-tutorial.html)

**Full Changelog**: https://github.com/eftalgezer/SIESTAstepper/compare/v1.0.0...v1.1.0

## [v1.0.0](https://github.com/eftalgezer/SIESTAstepper/tree/v1.0.0) (2022-09-14)

- `run_interrupted` function is added. It is possible to continue from an interrupted calculation.
- `make_directories` function is added. It is possible to make i* directories massively. 
- Security improvements
- Setting the NumberOfAtoms parameter while creating an fdf file
- `copy_files` function is added. It is possible to copy desired files by extension.
- Print PID on screen
- `contfiles` parameter is added. It is used in the copy_files function to copy files, not by extension.
- Continuations are infinitive. If you kill your job in the "continue" folder, you can continue with the "continue_2", "continue_3" folder, etc.
- Parameter `missing` is removed in the functions `merge_ani`, and `analysis`. These functions will advantage the benefit of the `SIESTAstepper.cont` parameter.
- Improved Windows support
- `single_run` function is added. It is possible to run a step without proceeding to the next step.
- `single_run_interrupted` function is added. It is possible to run an interrupted step without proceeding to the next step.
- CHANGELOG.md is created.
- [A tutorial for v1.0.0 is written.](https://beyondthearistotelian.blogspot.com/2022/09/siestastepper-v100-tutorial.html)
- Bug fixes

Thanks to [toppk](Bug fix) at Stackoverflow for the [help in fixing the bug in the `remove_nones` function](https://stackoverflow.com/questions/73721062/why-the-operator-does-not-work-as-expected-in-python).

**Full Changelog**: https://github.com/eftalgezer/SIESTAstepper/compare/v0.4.2...v1.0.0

## [v0.4.2](https://github.com/eftalgezer/SIESTAstepper/tree/v0.4.2) (2022-09-08)

[Full Changelog](https://github.com/eftalgezer/SIESTAstepper/compare/v0.4.1...v0.4.2)

## [v0.4.1](https://github.com/eftalgezer/SIESTAstepper/tree/v0.4.1) (2022-09-08)

[Full Changelog](https://github.com/eftalgezer/SIESTAstepper/compare/v0.4.0...v0.4.1)

## [v0.4.0](https://github.com/eftalgezer/SIESTAstepper/tree/v0.4.0) (2022-09-07)

[Full Changelog](https://github.com/eftalgezer/SIESTAstepper/compare/v0.3.0...v0.4.0)

## [v0.3.0](https://github.com/eftalgezer/SIESTAstepper/tree/v0.3.0) (2022-09-06)

[Full Changelog](https://github.com/eftalgezer/SIESTAstepper/compare/v0.2.0...v0.3.0)

## [v0.2.0](https://github.com/eftalgezer/SIESTAstepper/tree/v0.2.0) (2022-09-06)

[Full Changelog](https://github.com/eftalgezer/SIESTAstepper/compare/v0.1.0...v0.2.0)

## [v0.1.0](https://github.com/eftalgezer/SIESTAstepper/tree/v0.1.0) (2022-09-05)

[Full Changelog](https://github.com/eftalgezer/SIESTAstepper/compare/5dd28a3654cb1a861d6abf7767d68fd11551a32d...v0.1.0)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
