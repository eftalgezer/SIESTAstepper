"""
SIESTAstepper runs SIESTA step by step, designed for constrained calculations.
"""

# meta
__title__ = "SIESTAstepper"
__author__ = "Eftal Gezer"
__license__ = "GNU GPL v3"
__copyright__ = "Copyright 2022, Eftal Gezer"
__version__ = "0.2.0"

from .core import run, run_next, ani_to_fdf, xyz_to_fdf, cwd, analysis, log, cores
