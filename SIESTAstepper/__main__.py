"""
SIESTAstepper terminal client
"""
from __future__ import absolute_import
import sys
from .core import (
    run,
    single_run,
    run_next,
    run_interrupted,
    single_run_interrupted,
    make_directories,
    copy_files,
    ani_to_fdf,
    xyz_to_fdf,
    merge_ani,
    analysis,
    energy_diff,
    contfiles,
    contextensions,
    set_log,
    set_cores,
    set_conda,
    set_cont,
    set_siesta
)

function = sys.argv[1]
for arg in sys.argv:
    if arg.startswith("mpirun="):
        set_cores(int(arg.split("=")[1]))
    if arg.startswith("conda="):
        set_conda(arg.split("=")[1])
    if arg.startswith("cont="):
        set_cont(arg.split("=")[1])
    if arg.startswith("contfiles="):
        contfiles.extend(arg.split("=")[1].split(","))
    if arg.startswith("contextensions="):
        contextensions.extend(arg.split("=")[1].split(","))
    if arg.startswith("siesta="):
        set_siesta(arg.split("=")[1])

if function not in ["run", "single_run", "run_next", "run_interrupted", "single_run_interrupted",
                    "make_directories", "copy_files", "ani_to_fdf", "xyz_to_fdf", "merge_ani",
                    "analysis", "energy_diff"]:
    raise AttributeError(
        """Command not found. Please use 'run', 'single_run', 'run_next', 'run_interrupted',
        'single_run_interrupted', 'make_directories', 'copy_files', 'ani_to_fdf', 'xyz_to_fdf',
        'merge_ani', 'analysis', 'energy_diff'""".replace("\n", " ")
    )
if function == "run":
    set_log(sys.argv[2])
    run(sys.argv[3])
elif function == "single_run":
    set_log(sys.argv[2])
    single_run(sys.argv[3], sys.argv[4])
elif function == "run_next":
    set_log(sys.argv[2])
    run_next(sys.argv[3], sys.argv[4])
elif function == "run_interrupted":
    set_log(sys.argv[2])
    run_interrupted(sys.argv[3], sys.argv[4])
elif function == "single_run_interrupted":
    set_log(sys.argv[2])
    single_run_interrupted(sys.argv[3], sys.argv[4])
elif function == "make_directories":
    make_directories(int(sys.argv[2]))
elif function == "copy_files":
    copy_files(
        [_ for _ in sys.argv[5:] if not _.startswith("contfiles=")],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4]
    )
elif function == "ani_to_fdf":
    ani_to_fdf(sys.argv[2], sys.argv[3], sys.argv[4])
elif function == "xyz_to_fdf":
    xyz_to_fdf(sys.argv[2], sys.argv[3], sys.argv[4])
elif function == "merge_ani":
    path = "i*"
    if len(sys.argv) == 3:
        merge_ani(label=sys.argv[2])
    elif len(sys.argv) > 3:
        for arg in sys.argv[3:]:
            if arg.startswith("path="):
                path = arg.split("=")[1]
        merge_ani(label=sys.argv[2], path=path)
elif function == "analysis":
    set_log(sys.argv[2])
    plot_ = True
    path = "i*"
    if len(sys.argv) > 4:
        for arg in sys.argv[3:]:
            if arg.startswith("path="):
                path = arg.split("=")[1]
            if arg == "noplot":
                plot_ = False
        analysis(path=path, plot_=plot_)
    else:
        analysis()
elif function == "energy_diff":
    set_log(sys.argv[2])
    path = "i*"
    if len(sys.argv) > 4:
        for arg in sys.argv[3:]:
            if arg.startswith("path="):
                path = arg.split("=")[1]
        energy_diff(path=path)
    else:
        energy_diff()
