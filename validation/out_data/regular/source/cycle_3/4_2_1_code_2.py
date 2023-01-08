from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Clt_CF = Factor("Clt[CF", [Level("l22dmT|iW[Wa", 1), Level("IcuLjigs?8", 1), Level("rh;nbLysFxfYop", 3), Level("aWL", 6)])
P_J_L_y = Factor("P|J%L^y", [Level(";oKZhQWhvC", 1), Level("rqF^P;v0I", 1), Level("#iMgXnO:", 6), Level("PVWYarfX", 3)])

design=[Clt_CF,P_J_L_y]
crossing=[Clt_CF,P_J_L_y]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_1"))

### END
