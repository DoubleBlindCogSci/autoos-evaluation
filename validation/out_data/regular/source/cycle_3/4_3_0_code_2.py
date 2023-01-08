from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
w_wKEQfjtuL = Factor("w]wKEQfjtuL", [Level("dvAL", 1), Level("qU)P", 1), Level("nHGLbkYRAT", 1), Level("iFUGatGZaeVYjl", 1), Level("ejdSnrjVVeqh", 8)])
C_krZwd = Factor("C4krZwd", [Level("Jhlf#sDUj", 1), Level("?hQrS", 1), Level("RuRJCC", 6), Level("vuzr", 1)])
EFRWROtJQG = Factor("EFRWROtJQG", [Level("LKFVp;8MzDY8F", 1), Level("KPZRhqX", 1), Level("Kh{fGMvOjo(Rw", 1), Level("bjJNM%rv", 1)])

design=[w_wKEQfjtuL,C_krZwd,EFRWROtJQG]
crossing=[w_wKEQfjtuL,C_krZwd,EFRWROtJQG]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3_0"))

### END
