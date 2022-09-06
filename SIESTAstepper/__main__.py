import sys
from .core import run, run_next, ani_to_fdf, xyz_to_fdf, analysis, log, cores

function = sys.argv[1]
for arg in sys.argv:
    if arg.startswith("mpirun="):
        cores = int(arg.split("=")[1])

if function not in ["run", "run_next", "ani_to_fdf", "xyz_to_fdf", "analysis"]:
    raise AttributeError("Command not found. Please use 'run', 'run_next', 'ani_to_fdf', 'xyz_to_fdf', 'analysis'")
elif function == "run":
    log = sys.argv[2]
    run(sys.argv[3])
elif function == "run_next":
    log = sys.argv[2]
    run_next(sys.argv[3], sys.argv[4])
elif function == "ani_to_fdf":
    ani_to_fdf(sys.argv[2], sys.argv[3], sys.argv[4])
elif function == "xyz_to_fdf":
    xyz_to_fdf(sys.argv[2], sys.argv[3], sys.argv[4])
elif function == "analysis":
    log = sys.argv[2]
    plot_ = True
    path = "i*"
    missing = None
    if len(sys.argv) > 4:
        for arg in sys.argv[3:]:
            if arg.startswith("path="):
                path = arg.split("=")[1]
            if arg.startswith("missing="):
                missing = arg.split("=")[1]
            if arg == "noplot":
                plot_ = False
        analysis(path=None, missing=None, plot_=True)
    else:
        analysis()
