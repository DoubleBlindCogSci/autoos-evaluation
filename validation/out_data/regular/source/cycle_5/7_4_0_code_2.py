from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
iZOtp = Factor("iZOtp", [Level("yYfWqaYvkZegd", 1), Level("zzTbk", 1), Level("6EBviLCcpDG", 3), Level("SldRo PXU", 1), Level("WiwkykvcfEyD", 1), Level("T*s9(D", 1), Level("Pc<sDukSLP", 1)])
UB_ = Factor("UB9", [Level("IDfaKMD", 1), Level(" [x ^HBB", 1), Level("Gu:", 1), Level("cAJn", 2), Level(")L#8ATLFlJR", 1), Level("CzUJWssX", 1), Level("kk<kwOWnImQEQ", 1)])
GSqpO_C_gi_ = Factor("GSqpO~C1gi7", [Level("wBCCEQ7sinDW", 1), Level("lyss", 1), Level("gt@YCh", 1), Level("SkK0WEnW!TTP", 1), Level("KIuwXw]B", 1), Level("}B}5FVBXJpcY", 1), Level("~nnvN", 1)])
IigMbEZE_B = Factor("IigMbEZE0B", [Level("Am(gmCwehx^l", 1), Level("WX5Uj7qXpr", 1), Level("VXRGDU", 1), Level("Vu!ErD_Tc", 1), Level("e6sBpLbxlWwt ", 1), Level("tO:GLRD", 1), Level("NW{RWkaO*[", 1), Level("wfuQ?ydYw%ZkMN", 1)])

design=[iZOtp,UB_,GSqpO_C_gi_,IigMbEZE_B]
crossing=[iZOtp,UB_,GSqpO_C_gi_,IigMbEZE_B]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_4_0"))

### END
