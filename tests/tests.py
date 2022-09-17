"""
Unit tests for the SIESTAstepper library.
"""
import os
import shutil
from SIESTAstepper import __file__ as mfile
from .testers import *

mpath = mfile.replace("/SIESTAstepper/__init__.py", "")


def test_ani_to_fdf():
    """Tests for ani_to_fdf"""
    assert tester_ani_to_fdf(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}ANI{os.sep}C-4.ANI",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-0.fdf",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-5.fdf"
    ) == read_file(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-5.fdf")


def test_xyz_to_fdf():
    """Tests for xyz_to_fdf"""
    assert tester_xyz_to_fdf(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}xyz{os.sep}C.xyz",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-0.fdf",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-1.fdf"
    ) == read_file(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-1.fdf")


def test_merge_ani():
    """Tests for merge_ani"""
    assert tester_merge_ani(label="C", folder="Carbon") == read_file(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}ANI{os.sep}C-merged.ANI"
    )


def test_make_directories():
    """Tests for make_directories"""
    assert tester_make_directories(5) == ["i1", "i2", "i3", "i4", "i5"]


def clear_temp():
    """Clears the temp folder"""
    for filename in os.listdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp"):
        filepath = os.path.join(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp", filename)
        try:
            if os.path.isfile(filepath) or os.path.islink(filepath):
                os.unlink(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)
        except Exception as e:
            print(f'Failed to delete {filepath}. Reason: {e}')
