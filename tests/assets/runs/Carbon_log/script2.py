import SIESTAstepper
import os
SIESTAstepper.settings.set_cwd(os.getcwd())
SIESTAstepper.settings.set_cont("continue") # default is "continue" 
SIESTAstepper.settings.contfiles.append("pair")
SIESTAstepper.run_interrupted("3", "C")
