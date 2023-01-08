from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uN_cFrE = Factor("uN(cFrE", ["xFJHlWb4FLn}ho", "I%FbIaTigmkT", "qfstTQxDzb"])
XkceEaTGeU_ = Factor("XkceEaTGeU0", ["WcsbWhEfvi", "Ll5Sd{", "Cre5E!UzB2n", "dyRyQqCIX"])

design=[uN_cFrE,XkceEaTGeU_]
crossing=[uN_cFrE,XkceEaTGeU_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END
