"""
Setup file for SIESTAstepper
"""
from __future__ import absolute_import
from __future__ import with_statement
import os
from setuptools import setup
import io


HERE = pathlib.Path(__file__).parent.resolve()

LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="SIESTAstepper",
    version="2.1.0",
    description="SIESTAstepper runs SIESTA step by step, designed for constrained calculations.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/eftalgezer/SIESTAstepper",
    author="Eftal Gezer",
    author_email="eftal.gezer@astrobiyoloji.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="SIESTA, DFT, molecular calculations, chemistry, physics",
    packages=["SIESTAstepper"],
    install_requires=[
        "sh",
        "matplotlib",
        "scipy",
        "numpy",
        "ANIAnimator"
        ],
    project_urls={
        "Bug Reports": "https://github.com/eftalgezer/SIESTAstepper/issues",
        "Source": "https://github.com/eftalgezer/SIESTAstepper/",
        "Blog": "https://beyondthearistotelian.blogspot.com/search/label/SIESTAstepper",
        "Developer": "https://www.eftalgezer.com/",
    },
)
