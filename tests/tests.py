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
    assert ani_to_fdf_tester(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}ANI{os.sep}C-4.ANI",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-0.fdf",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-5.fdf"
    ) == read_file(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-5.fdf")


def test_xyz_to_fdf():
    """Tests for xyz_to_fdf"""
    assert xyz_to_fdf_tester(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}xyz{os.sep}C.xyz",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-0.fdf",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}C-1.fdf"
    ) == read_file(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}fdf{os.sep}C-1.fdf")


def test_merge_ani():
    """Tests for merge_ani"""
    assert merge_ani_tester(label="C", folder="Carbon") == read_file(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}ANI{os.sep}C-merged.ANI"
    )


def test_make_directories():
    """Tests for make_directories"""
    assert make_directories_tester(5) == [
        f"{mpath}{os.sep}tests{os.sep}temp{os.sep}i1",
        f"{mpath}{os.sep}tests{os.sep}temp{os.sep}i2",
        f"{mpath}{os.sep}tests{os.sep}temp{os.sep}i3",
        f"{mpath}{os.sep}tests{os.sep}temp{os.sep}i4",
        f"{mpath}{os.sep}tests{os.sep}temp{os.sep}i5"
    ]


def test_copy_files():
    assert copy_files_tester(
        ["psf, DM, XV"], "C",
        f"{mpath}{os.sep}tests{os.sep}runs{os.sep}Carbon{os.sep}i1",
        f"{mpath}{os.sep}tests{os.sep}temp{os.sep}i2"
    ) == [
               f"{mpath}{os.sep}tests{os.sep}temp{os.sep}i2{os.sep}C.psf",
               f"{mpath}{os.sep}tests{os.sep}temp{os.sep}i2{os.sep}C.DM",
               f"{mpath}{os.sep}tests{os.sep}temp{os.sep}i2{os.sep}C.XV"
           ]


def test_analysis():
    assert analysis_tester(
        "i*",
        f"{mpath}{os.sep}tests{os.sep}runs{os.sep}Carbon"
    ) == [
               (1, -297.982681),
               (2, -299.171055),
               (3, -299.791356),
               (4, -299.845957),
               (5, -299.498399)
           ]


def test_energy_diff():
    assert energy_diff_tester(
        "i*",
        f"{mpath}{os.sep}tests{os.sep}runs{os.sep}Carbon"
    ) == [(-299.845957, -297.982681, 4, 1, 1.8632759999999848)]


def test_get_it():
    assert get_it_tester(files)


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
