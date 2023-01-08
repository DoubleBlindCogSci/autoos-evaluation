from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ejoxfm = Factor("ejoxfm", ["xszkj", "hopqq"])
mxbfc = Factor("mxbfc", ["oyfu", "raqj"])
uyo = Factor("uyo", ["jscbrn", "uuze"])
nnmaf = Factor("nnmaf", ["grywr", "vawze"])
qihvv = Factor("qihvv", ["vmbh", "kfc"])
mnjl = Factor("mnjl", ["mljq", "kdg"])

### EXPERIMENT
design=[ejoxfm,mxbfc,uyo,nnmaf,qihvv,mnjl]
crossing=[[ejoxfm,mxbfc],[uyo,nnmaf],[qihvv,mnjl],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_4"))
### END