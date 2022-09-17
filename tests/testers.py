"""
Unit testers for the SIESTAstepper library.
"""
import glob
import os
from distutils.dir_util import copy_tree
from SIESTAstepper import __file__ as mfile
from SIESTAstepper.core import run, single_run, run_next, run_interrupted, single_run_interrupted, make_directories, \
    copy_files, \
    ani_to_fdf, xyz_to_fdf, merge_ani, analysis, energy_diff, contfiles, contextensions, update_cwd, update_log, \
    update_cores, update_conda, update_cont, update_siesta
from SIESTAstepper.helpers import create_fdf, read_fdf, read_energy, get_it, print_run, check_restart, \
    check_userbasis, copy_file, sort_, remove_nones

mpath = mfile.replace("/SIESTAstepper/__init__.py", "")


def read_file(file):
    """Read a given file and return its content"""
    with open(file, "r") as f:
        content = f.read()
        f.close()
    return content


def tester_ani_to_fdf(anipath, fdfpath, newfdfpath):
    """Tester function for ani_to_fdf"""
    ani_to_fdf(anipath, fdfpath, newfdfpath)
    return read_file(newfdfpath)


def tester_xyz_to_fdf(xyzpath, fdfpath, newfdfpath):
    """Tester function for xyz_to_fdf"""
    xyz_to_fdf(xyzpath, fdfpath, newfdfpath)
    return read_file(newfdfpath)


def tester_merge_ani(label=None, path=None, folder=None):
    """Tester function for merge_ani"""
    if path is None:
        path = "i*"
    if label is None:
        raise ValueError("ERROR: Please set a label")
    if folder is None:
        raise ValueError("ERROR: Please set a folder")
    copy_tree(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}runs{os.sep}{folder}",
        f"{mpath}{os.sep}tests{os.sep}temp{os.sep}{folder}"
    )
    update_cwd(f"{mpath}{os.sep}tests{os.sep}temp{os.sep}{folder}")
    merge_ani(label=label, path=path)
    return read_file(f"{mpath}{os.sep}tests{os.sep}temp{os.sep}{folder}{os.sep}{label}-merged.ANI")


def tester_make_directories(n):
    """Tester function for make_directories"""
    update_cwd(f"{mpath}{os.sep}tests{os.sep}temp")
    make_directories(n)
    return sort_(list(glob.glob(f"{mpath}{os.sep}tests{os.sep}temp{os.sep}i*")))


def tester_copy_files(extensions, label, source_, destination):
    """Tester function for copy_files"""
    files = None
    copy_files(extensions, label, source_, destination)
    if extensions is not None:
        for ext in extensions:
            if ext == "psf":
                files = glob.glob(f"{destination}{os.sep}*.psf")
            elif ext == "ion":
                files += glob.glob(f"{destination}{os.sep}*.ion")
            else:
                files += glob.glob(f"{destination}{os.sep}{label}.{ext}")
    for cf in contfiles:
        files += glob.glob(f"{destination}{os.sep}{cf}")
    return files


def tester_analysis(path):
    """Tester function for analysis"""
    return analysis(path)


def tester_energy_diff(path):
    """Tester function for energy_diff"""
    return energy_diff(path)


def tester_get_it(files):
    """Tester function for get_it"""
    return get_it(files)


def tester_read_fdf(fdfpath, geo):
    """Tester function for read_fdf"""
    return read_fdf(fdfpath, geo)


def tester_create_fdf(fdf, geo, newfdfpath, number):
    """Tester function for create_fdf"""
    create_fdf(fdf, geo, newfdfpath, number)
    return read_file(newfdfpath)


def tester_check_restart(fdffile, i, label, cwd, cont, contextensions):
    """Tester function for check_restart"""
    check_restart(fdffile, i, label, cwd, cont, contextensions)
    return read_file(fdffile)


def tester_check_userbasis(fdffile):
    """Tester function for check_userbasis"""
    return check_userbasis(fdffile)


def tester_copy_file(sourcefile, destinationfile):
    """Tester function for copy_file"""
    copy_file(sourcefile, destinationfile)
    return glob.glob(destinationfile)


def tester_sort_(files, path, cont):
    """Tester function for sort_"""
    return sort_(files, path, cont)


def tester_remove_nones(files, path, cwd, cont, log):
    """Tester function for remove_nones"""
    remove_nones(files, path, cwd, cont, log)
    return files