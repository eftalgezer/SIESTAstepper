"""
Unit testers for the SIESTAstepper library.
"""
import glob
import os
import shutil
import io
import sys
from SIESTAstepper import __file__ as mfile
from SIESTAstepper.core import run, single_run, run_next, run_interrupted, single_run_interrupted, make_directories, \
    copy_files, ani_to_fdf, xyz_to_fdf, merge_ani, analysis, energy_diff, _command, contfiles, contextensions, \
    update_cwd, update_log, update_cores, update_conda, update_cont, update_siesta, log
from SIESTAstepper.helpers import create_fdf, read_fdf, read_energy, get_it, print_run, check_restart, \
    check_userbasis, copy_file, sort_, remove_nones

mpath = mfile.replace("/SIESTAstepper/__init__.py", "")
fakeproject = None


def read_file(file):
    """Read a given file and return its content"""
    with open(file, "r") as f:
        content = f.read()
        f.close()
    return content


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


def initialise_fake_project():
    """Initialise fake project to test"""
    os.mkdir(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{fakeproject}")
    files = f"{mpath}{os.sep}tests{os.sep}assets{os.sep}runs{os.sep}{fakeproject}{os.sep}*"
    for f in files:
        fname = f.split(os.sep)[-1]
        print(f)
        if os.path.isfile(f):
            print(f"{f}*")
            shutil.copy(f, f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{fakeproject}{os.sep}{fname}")
    print(list(glob.glob(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{fakeproject}{os.sep}*")))


def fake_command(label=None, issingle=False):
    """A fake SIESTA run command"""
    realpath = os.getcwd().replace(f"{os.sep}temp{os.sep}", f"{os.sep}runs{os.sep}")
    with open(f"{realpath}{os.sep}{log}", "r") as reallog:
        with open(f"{os.getcwd()}{os.sep}{log}", "w") as fakelog:
            lines = reallog.readlines()
            for line in lines:
                fakelog.writeline(line)
                print(line)
                if line == "Job completed\n" and issingle is False:
                    run(label)
            fakelog.close()
        reallog.close()


_command = fake_command


def set_fake_project(newfakeproject):
    global fakeproject
    fakeproject = newfakeproject


def get_fake_project():
    return fakeproject


def ani_to_fdf_tester(anipath, fdfpath, newfdfpath):
    """Tester function for ani_to_fdf"""
    ani_to_fdf(anipath, fdfpath, newfdfpath)
    return read_file(newfdfpath)


def xyz_to_fdf_tester(xyzpath, fdfpath, newfdfpath):
    """Tester function for xyz_to_fdf"""
    xyz_to_fdf(xyzpath, fdfpath, newfdfpath)
    return read_file(newfdfpath)


def merge_ani_tester(label=None, path=None, folder=None):
    """Tester function for merge_ani"""
    if path is None:
        path = "i*"
    if label is None:
        raise ValueError("ERROR: Please set a label")
    if folder is None:
        raise ValueError("ERROR: Please set a folder")
    if os.path.exists(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{folder}"):
        shutil.rmtree(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{folder}")
    shutil.copytree(
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}runs{os.sep}{folder}",
        f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{folder}"
    )
    update_cwd(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{folder}")
    merge_ani(label=label, path=path)
    return read_file(f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{folder}{os.sep}{label}-merged.ANI")


def run_tester(label):
    """Tester function for run"""
    capturedoutput = io.StringIO()
    sys.stdout = capturedoutput
    run(label)
    sys.stdout = sys.__stdout__
    return capturedoutput.getvalue()


def make_directories_tester(n):
    """Tester function for make_directories"""
    if "temp" in os.getcwd():
        make_directories(n)
    else:
        raise IOError("ERROR: Tests should be run in 'temp' folder")
    return sort_(
        list(
            glob.glob(
                f"{os.getcwd()}{os.sep}i*")),
        f"{os.getcwd()}{os.sep}i*",
        ""
    )


def copy_files_tester(extensions, label, source_, destination):
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
    return list(files)


def analysis_tester(path, cwd):
    """Tester function for analysis"""
    update_cwd(cwd)
    return analysis(path)


def energy_diff_tester(path, cwd):
    """Tester function for energy_diff"""
    update_cwd(cwd)
    return energy_diff(path)


def get_it_tester(path, cont):
    """Tester function for get_it"""
    files = glob.glob(f"{path}{os.sep}i*")
    files += glob.glob(f"{path}{os.sep}i*{os.sep}{cont}*")
    return get_it(files)


def read_fdf_tester(fdfpath, geo):
    """Tester function for read_fdf"""
    return read_fdf(fdfpath, geo)


def create_fdf_tester(fdf, geo, newfdfpath, number):
    """Tester function for create_fdf"""
    create_fdf(fdf, geo, newfdfpath, number)
    return read_file(newfdfpath)


def read_energy_tester(energies=[], path=None, cont=None, it=[]):
    files = glob.glob(f"{path}{os.sep}i*{os.sep}log")
    files += glob.glob(f"{path}{os.sep}i*{os.sep}{cont}*{os.sep}log")
    files = sort_(files, "i*", cont)
    read_energy(energies, files, it)
    return it, energies


def print_run_tester(for_, cores, conda):
    """Tester function for print_run"""
    capturedoutput = io.StringIO()
    sys.stdout = capturedoutput
    print_run(for_, cores, conda)
    sys.stdout = sys.__stdout__
    return capturedoutput.getvalue()


def check_restart_tester(fdffile, i, label, cwd, cont, context):
    """Tester function for check_restart"""
    file = fdffile.split(os.sep)[-1]
    copy_file(fdffile, f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{file}")
    fdffile = f"{mpath}{os.sep}tests{os.sep}assets{os.sep}temp{os.sep}{file}"
    with open(fdffile, "r+") as f:
        check_restart(f, i, label, cwd, cont, context)
        f.close()
    return read_file(fdffile)


def check_userbasis_tester(fdffile):
    """Tester function for check_userbasis"""
    return check_userbasis(fdffile)


def copy_file_tester(sourcefile, destinationfile):
    """Tester function for copy_file"""
    copy_file(sourcefile, destinationfile)
    return list(glob.glob(destinationfile))


def sort__tester(files, path, cont):
    """Tester function for sort_"""
    return sort_(files, path, cont)


def remove_nones_tester(files, path, cwd, cont, log):
    """Tester function for remove_nones"""
    remove_nones(files, path, cwd, cont, log)
    return files
