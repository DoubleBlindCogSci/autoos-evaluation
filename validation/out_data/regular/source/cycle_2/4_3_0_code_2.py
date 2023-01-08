from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZPWrVc = Factor("ZPWrVc", [Level("CNgNhGHCCZHip", 10), Level("kFEKuvBWnTg?3c", 1), Level("YtThQKPVniM~", 8), Level("Aq#{UhDtH", 1)])
eqGmUptsi = Factor("eqGmUptsi", [Level("oC7Sfpibdy", 1), Level("VQPBA", 1), Level("tJRJlVUb~yL", 7), Level("VNZNo0p", 1), Level("RBL5P?dedH", 1)])
v_Vy = Factor("v}Vy", [Level("2hy>", 1), Level("MHU", 1), Level("UwsYZMnPe", 4), Level("ZMLL#T", 2)])

design=[ZPWrVc,eqGmUptsi,v_Vy]
crossing=[ZPWrVc,eqGmUptsi,v_Vy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3_0"))

### END
