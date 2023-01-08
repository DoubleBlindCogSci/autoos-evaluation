from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
V_rCn_i = Factor("V)rCn:i", [Level("mi&bhLRWS_oq", 1), Level("M0w$eOVYzN", 1), Level("VNcDo:", 1), Level("teELYLSUURC", 1), Level("opcmuQk!DQ4qfy", 1), Level("aDVr", 1), Level("YanpeBDa", 1), Level("YIoWsLN", 6)])
PHfFDjTYNlH = Factor("PHfFDjTYNlH", [Level("_WteHj", 1), Level("MnE<WDU", 1), Level("rQgD?WwvdIdM;", 1), Level("SURrRd]cbI", 1), Level("VVdSAjDlrWE|", 1), Level("LBMxX{W>H", 1), Level("YhR_pthuX7Q", 10)])

design=[V_rCn_i,PHfFDjTYNlH]
crossing=[V_rCn_i,PHfFDjTYNlH]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_2_0"))

### END
