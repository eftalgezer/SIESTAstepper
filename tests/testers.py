"""
Unit testers for the SIESTAstepper library.
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import with_statement
from __future__ import unicode_literals
import contextlib
import glob
import os
import shutil
import io
import sys
import re
from _pytest.monkeypatch import MonkeyPatch
try:
    from unittest.mock import MagicMock, patch
except ImportError:
    from mock import MagicMock, patch
from SIESTAstepper import __file__ as mfile
from SIESTAstepper.core import (
    run,
    single_run,
    run_next,
    run_interrupted,
    single_run_interrupted,
    make_directories,
    copy_files,
    ani_to_fdf,
    xyz_to_fdf,
    xv_to_fdf,
    log_to_fdf,
    xv_to_ani,
    merge_ani,
    energy_analysis,
    force_analysis,
    energy_diff,
    force_diff,
    pair_correlation_function,
    _command,
    settings
)
from SIESTAstepper.helpers import (
    create_fdf,
    read_fdf,
    read_energy,
    get_it,
    print_run,
    check_restart,
    check_userbasis,
    copy_file,
    sort_,
    remove_nones
)

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

mpath = mfile.replace("/SIESTAstepper/__init__.py", "").replace("SIESTAstepperc", "SIESTAstepper")
fakeproject = None


def read_file(file):
    """Read a given file and return its content"""
    with io.open(file, "r", encoding="utf-8") as f:
        content = f.read()
        f.close()
    return content


def clear_temp():
    """Clears the temp folder"""
    for filename in os.listdir("{0}{1}tests{1}assets{1}temp".format(mpath, os.sep)):
        filepath = os.path.join("{0}{1}tests{1}assets{1}temp".format(mpath, os.sep), filename)
        if os.path.isfile(filepath) or os.path.islink(filepath):
            os.unlink(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)


def initialise_fake_project(function="run"):
    """Initialise fake project to test"""
    if function == "run":
        files = glob.glob("{0}{1}tests{1}assets{1}runs{1}{2}{1}*".format(mpath, os.sep, fakeproject))
        for f in files:
            if os.path.isfile(f):
                shutil.copy(f, f.replace("runs", "temp"))
    if function.startswith("run_next") or function.startswith("single_run"):
        i = int(function.split(" ")[1])
        files = glob.glob(
            "{0}{1}tests{1}assets{1}runs{1}{2}{1}i*{1}*".format(mpath, os.sep, fakeproject)
        )
        for f in files:
            fname = f.split(os.sep)[-1]
            match = re.search(
                "{0}{1}tests{1}assets{1}runs{1}{2}{1}i([0-9]+){1}{3}".format(mpath, os.sep, fakeproject, fname),
                f
            )
            if int(match.group(1)) <= i and os.path.isfile(f):
                if not os.path.exists(
                        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i{3}".format(mpath, os.sep, fakeproject, match.group(1))
                ):
                    os.mkdir(
                        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i{3}".format(mpath, os.sep, fakeproject, match.group(1))
                    )
                shutil.copy(f, f.replace("runs", "temp"))
    if function.startswith("run_interrupted") or function.startswith("single_run_interrupted"):
        i = int(function.split(" ")[1])
        c = 0
        try:
            c = int(function.split(" ")[2])
        except Exception:
            c = 1
        files = glob.glob("{0}{1}tests{1}assets{1}runs{1}{2}{1}i*{1}*".format(mpath, os.sep, fakeproject))
        files += glob.glob(
            "{0}{1}tests{1}assets{1}runs{1}{2}{1}".format(mpath, os.sep, fakeproject) +
            "i*{0}{1}*{0}*".format(os.sep, settings.get_cont())
        )
        files = sort_([f for f in files if os.path.isfile(f)], "i*", settings.get_cont())
        for f in files:
            fname = f.split(os.sep)[-1]
            match = re.search(
                "{0}{1}tests{1}assets{1}runs{1}{2}{1}i([0-9]+)".format(mpath, os.sep, fakeproject) +
                "({0}{1}_*[0-9]*)?{0}{2}".format(os.sep, settings.get_cont(), fname),
                f
            )
            if int(match.group(1)) <= i and os.path.isfile(f):
                if not os.path.exists(
                        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i{3}{4}".format(
                            mpath,
                            os.sep,
                            fakeproject,
                            match.group(1),
                            match.group(2) if match.group(2) is not None else ""
                        )
                ):
                    os.mkdir(
                        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i{3}{4}".format(
                            mpath,
                            os.sep,
                            fakeproject,
                            match.group(1),
                            match.group(2) if match.group(2) is not None else ""
                        )
                    )
                shutil.copy(f, f.replace("runs", "temp"))
                if int(match.group(1)) == i and \
                        int("-1"
                            if match.group(2) is None else
                            match.group(2).split("_")[1]
                            if settings.get_cont() + "_" in match.group(2) else
                            "1") > c - 1:
                    shutil.rmtree(
                        "{0}{1}tests{1}assets{1}temp{1}{2}{1}i{3}{4}".format(
                            mpath,
                            os.sep,
                            fakeproject,
                            match.group(1),
                            match.group(2) if match.group(2) is not None else ""
                        )
                    )


def fake_command(monkeypatch=MonkeyPatch()):
    """Monkeypatching _command"""

    def fake__command(label=None, issingle=False):
        """A fake SIESTA run command"""
        realpath = os.getcwd().replace("{0}temp{0}".format(os.sep), "{0}runs{0}".format(os.sep))
        with io.open("{0}{1}{2}".format(realpath, os.sep, settings.get_log()), "r", encoding="utf-8") as reallog:
            with io.open("{0}{1}{2}".format(os.getcwd(), os.sep, settings.get_log()), "w", encoding="utf-8") as fakelog:
                content = reallog.read()
                fakelog.write(content)
                print(content)
                copy_files(["ANI"], "C", realpath, os.getcwd())
                try:
                    copy_files(["XV"], "C", realpath, os.getcwd())
                except FileNotFoundError:
                    pass
                if content.endswith("Job completed\n") and issingle is False:
                    run(label)
                fakelog.close()
            reallog.close()

    monkeypatch.setattr("SIESTAstepper.core._command", fake__command)


def set_fake_project(newfakeproject):
    global fakeproject
    fakeproject = newfakeproject
    if not os.path.exists("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, fakeproject)):
        os.mkdir("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, fakeproject))


def get_fake_project():
    return fakeproject


def run_next_tester(i, label):
    """Tester function for run_next"""
    capturedoutput = io.StringIO()
    sys.stdout = capturedoutput
    run_next(i, label)
    sys.stdout = sys.__stdout__
    return capturedoutput.getvalue()


def single_run_tester(i, label):
    """Tester function for single_run"""
    capturedoutput = io.StringIO()
    sys.stdout = capturedoutput
    single_run(i, label)
    sys.stdout = sys.__stdout__
    return capturedoutput.getvalue()


def ani_to_fdf_tester(anipath, fdfpath, newfdfpath):
    """Tester function for ani_to_fdf"""
    ani_to_fdf(
        anipath,
        fdfpath,
        newfdfpath
    )
    return read_file(newfdfpath)


def xyz_to_fdf_tester(xyzpath, fdfpath, newfdfpath):
    """Tester function for xyz_to_fdf"""
    xyz_to_fdf(xyzpath, fdfpath, newfdfpath)
    return read_file(newfdfpath)


def xv_to_fdf_tester(xvpath, fdfpath, newfdfpath):
    """Tester function for xv_to_fdf"""
    xv_to_fdf(xvpath, fdfpath, newfdfpath)
    return read_file(newfdfpath)


def log_to_fdf_tester(logpath, fdfpath, newfdfpath):
    """Tester function for log_to_fdf"""
    log_to_fdf(
        logpath,
        fdfpath,
        newfdfpath
    )
    return read_file(newfdfpath)


def xv_to_ani_tester(label=None, path="i*", folder=None):
    """Tester function for xv_to_ani"""
    if os.path.exists("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, folder)):
        shutil.rmtree("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, folder))
    shutil.copytree(
        "{0}{1}tests{1}assets{1}runs{1}{2}".format(mpath, os.sep, folder),
        "{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, folder)
    )
    settings.set_cwd("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, folder))
    xv_to_ani(label=label, path=path)
    return read_file("{0}{1}tests{1}assets{1}temp{1}{2}{1}{3}-XV.ANI".format(mpath, os.sep, folder, label))


def merge_ani_tester(label=None, path="i*", folder=None):
    """Tester function for merge_ani"""
    if os.path.exists("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, folder)):
        shutil.rmtree("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, folder))
    shutil.copytree(
        "{0}{1}tests{1}assets{1}runs{1}{2}".format(mpath, os.sep, folder),
        "{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, folder)
    )
    settings.set_cwd("{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, folder))
    merge_ani(label=label, path=path)
    return read_file("{0}{1}tests{1}assets{1}temp{1}{2}{1}{3}-merged.ANI".format(mpath, os.sep, folder, label))


def run_tester(label):
    """Tester function for run"""
    capturedoutput = io.StringIO()
    sys.stdout = capturedoutput
    run(label)
    sys.stdout = sys.__stdout__
    return capturedoutput.getvalue()


def run_interrupted_tester(i, label):
    """Tester function for run_interrupted"""
    capturedoutput = io.StringIO()
    sys.stdout = capturedoutput
    run_interrupted(i, label)
    sys.stdout = sys.__stdout__
    return capturedoutput.getvalue()


def single_run_interrupted_tester(i, label):
    """Tester function for single_run_interrupted"""
    capturedoutput = io.StringIO()
    sys.stdout = capturedoutput
    single_run_interrupted(i, label)
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
                "{0}{1}i*".format(os.getcwd(), os.sep))),
        "{0}{1}i*".format(os.getcwd(), os.sep),
        ""
    )


def copy_files_tester(extensions, label, source_, destination):
    """Tester function for copy_files"""
    files = None
    source_ = source_
    destination = destination
    copy_files(extensions, label, source_, destination)
    if extensions is not None:
        for ext in extensions:
            if ext == "psf":
                files = glob.glob("{0}{1}*.psf".format(destination, os.sep))
            elif ext == "ion":
                files += glob.glob("{0}{1}*.ion".format(destination, os.sep))
            else:
                files += glob.glob("{0}{1}{2}.{3}".format(destination, os.sep, label, ext))
    for cf in settings.contfiles:
        files += glob.glob("{0}{1}{2}".format(destination, os.sep, cf))
    return list(files)


def energy_analysis_tester(energytype="total", path="i*", cwd=None):
    """Tester function for energy_analysis"""
    settings.set_cwd(cwd)
    os.chdir(settings.get_cwd())
    return energy_analysis(energytype=energytype, path=path)


def force_analysis_tester(atomindex="Tot", forcetype="atomic", path="i*", cwd=None):
    """Tester function for test_analysis"""
    settings.set_cwd(cwd)
    os.chdir(settings.get_cwd())
    return force_analysis(atomindex=atomindex, forcetype=forcetype, path=path)


def energy_diff_tester(energytype="total", path="i*", cwd=None):
    """Tester function for energy_diff"""
    settings.set_cwd(cwd)
    os.chdir(settings.get_cwd())
    return energy_diff(energytype=energytype, path=path)


def force_diff_tester(atomindex="Tot", forcetype="atomic", path="i*", cwd=None):
    """Tester function for force_diff"""
    settings.set_cwd(cwd)
    os.chdir(settings.get_cwd())
    return force_diff(atomindex=atomindex, forcetype=forcetype, path=path)


def pair_correlation_function_tester(label=None, path="i*", dr=0.1, plot_=True, cwd=None):
    """Tester function for pair_correlation_function"""
    settings.set_cwd(cwd)
    os.chdir(settings.get_cwd())
    return pair_correlation_function(label=label, path=path, dr=dr, plot_=plot_)


def get_it_tester(path, cont):
    """Tester function for get_it"""
    files = glob.glob("{0}{1}i*".format(path, os.sep))
    files += glob.glob("{0}{1}i*{1}{2}*".format(path, os.sep, cont))
    return get_it(files)


def read_fdf_tester(fdfpath, geo):
    """Tester function for read_fdf"""
    return read_fdf(fdfpath, geo)


def create_fdf_tester(fdf, geo, newfdfpath, number):
    """Tester function for create_fdf"""
    create_fdf(fdf, geo, newfdfpath, number)
    return read_file(newfdfpath)


def read_energy_tester(energies=[], path=None, cont=None, it=[], energytype="total"):
    files = glob.glob("{0}{1}i*{1}{2}".format(path, os.sep, settings.get_log()))
    files += glob.glob("{0}{1}i*{1}{2}*{1}{3}".format(path, os.sep, cont, settings.get_log()))
    files = sort_(files, "i*", cont)
    read_energy(energies, files, it, energytype)
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
    copy_file(fdffile, "{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, file))
    fdffile = "{0}{1}tests{1}assets{1}temp{1}{2}".format(mpath, os.sep, file)
    with io.open(fdffile, "r+", encoding="utf-8") as f:
        check_restart(fdffile=f, i=i, label=label, cwd=cwd, cont=cont, contextensions=context)
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


def main_tester(command):
    fake_command()
    capturedoutput = io.StringIO()
    sys.stdout = capturedoutput
    from SIESTAstepper.__main__ import main as rtmain
    rtmain(args=command.split(" "))
    sys.stdout = sys.__stdout__
    return capturedoutput.getvalue()
