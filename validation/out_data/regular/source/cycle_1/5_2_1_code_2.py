from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
NsqqYlavrf_IlZ= Factor("NsqqYlavrf1IlZ", [Level("I%JSJ", 1), Level("pZX", 1), Level(")RVRs", 1), Level("a9UAMJLkr", 2), Level("sSPdU{WU", 1)])
_yrmvG= Factor(";yrmvG", [Level("0UqUEcb", 10), Level("DWirHPcUJVPR!a", 1), Level("YozSOPeMjrX", 1), Level("arfwGArd", 1), Level("u k~De!X H", 1)])

design=[NsqqYlavrf_IlZ,_yrmvG]
crossing=[NsqqYlavrf_IlZ,_yrmvG]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/5_2_1"))

### END
