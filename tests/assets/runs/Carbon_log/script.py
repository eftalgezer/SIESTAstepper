import SIESTAstepper
import os
SIESTAstepper.settings.set_cwd(os.getcwd())
#SIESTAstepper.conda = "envir" #to work with Anaconda
#SIESTAstepper.cores = 4 #to set number of cores for parallel run
#SIESTAstepper.make_directories(5) #to create folder if you are not created at first
SIESTAstepper.copy_files(["psf"], "C", ".", "i1")
SIESTAstepper.xyz_to_fdf("C.xyz", "C.fdf", "i1/C.fdf")
SIESTAstepper.run("C")
