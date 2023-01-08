from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
TqnSP = Factor("TqnSP", [Level("pqgnyBtyR", 1), Level("ZqWUWLTqt@Fggx", 1), Level("AJ)", 1)])
_QOKNrcoyYWR = Factor("5QOKNrcoyYWR", [Level("aHL", 4), Level("XpLoczwKvJY", 1), Level("spIJDRGSc3", 1)])

design=[TqnSP,_QOKNrcoyYWR]
crossing=[TqnSP,_QOKNrcoyYWR]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END
