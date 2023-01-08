from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
U_CWjYXT_xv = Factor("U0CWjYXT~xv", [Level("lepI?EB[$AvTc", 4), Level("^c5~xvuCTJYu", 7), "t$N@UYjUe!", "ISEvByPGf", "EEcurcEwyyAIAO", "isCI", "{kFp4ZKurdWJ", "HZ0", "MpAWIbWNMMnV"])

design=[U_CWjYXT_xv]
crossing=[U_CWjYXT_xv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_1_0"))

### END
