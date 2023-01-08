from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rbsLJ=['xFJHlWb4FLn}ho','I%FbIaTigmkT',"qfstTQxDzb"]
jXSq=Factor('uN(cFrE',rbsLJ)
JFy4ue2Xd="WcsbWhEfvi"
wQz8l=Factor('XkceEaTGeU0',[JFy4ue2Xd,"Ll5Sd{","Cre5E!UzB2n","dyRyQqCIX"])

### EXPERIMENT
design=[jXSq,wQz8l]
crossing=[jXSq,wQz8l]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END