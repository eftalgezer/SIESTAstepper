import sys
from .core import run, single_run, run_next, run_interrupted, single_run_interrupted, make_directories, copy_files, \
    ani_to_fdf, xyz_to_fdf, merge_ani, analysis, log, cores, conda, contfiles

function = sys.argv[1]
for arg in sys.argv:
    if arg.startswith("mpirun="):
        cores = int(arg.split("=")[1])
    if arg.startswith("conda="):
        conda = arg.split("=")[1]
    if arg.startswith("cont="):
        cont = arg.split("=")[1]
    if arg.startswith("contfiles="):
        contfiles.extend(arg.split("=")[1].split(","))

if function not in ["run", "single_run", "run_next", "run_interrupted", "single_run_interrupted", "make_directories",
                    "copy_files", "ani_to_fdf", "xyz_to_fdf", "merge_ani", "analysis"]:
    raise AttributeError(
        """Command not found. Please use 'run', 'single_run', 'run_next', 'run_interrupted', 'single_run_interrupted', 
        'make_directories', 'copy_files', 'ani_to_fdf', 'xyz_to_fdf', 'merge_ani', 'analysis' """
    )
elif function == "run":
    log = sys.argv[2]
    run(sys.argv[3])
elif function == "single_run":
    log = sys.argv[2]
    single_run(sys.argv[3], sys.argv[4])
elif function == "run_next":
    log = sys.argv[2]
    run_next(sys.argv[3], sys.argv[4])
elif function == "run_interrupted":
    log = sys.argv[2]
    run_interrupted(sys.argv[3], sys.argv[4])
elif function == "single_run_interrupted":
    log = sys.argv[2]
    single_run_interrupted(sys.argv[3], sys.argv[4])
elif function == "make_directories":
    make_directories(int(sys.argv[2]))
elif function == "copy_files":
    copy_files([_ for _ in sys.argv[5:] if not _.startswith("contfiles=")], sys.argv[2], sys.argv[3], sys.argv[4])
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
    log = sys.argv[2]
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
