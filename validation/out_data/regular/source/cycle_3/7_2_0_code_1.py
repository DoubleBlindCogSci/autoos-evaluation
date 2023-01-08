from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
EjMnRIlyZSV=Level('YIoWsLN',6)
b89AVX=Factor("V)rCn:i",["mi&bhLRWS_oq",'M0w$eOVYzN','VNcDo:','teELYLSUURC','opcmuQk!DQ4qfy','aDVr','YanpeBDa',EjMnRIlyZSV])
S1p4zPbBYsA=Factor("PHfFDjTYNlH",["_WteHj",'MnE<WDU',"rQgD?WwvdIdM;",'SURrRd]cbI',Level('VVdSAjDlrWE|',1),"LBMxX{W>H",Level('YhR_pthuX7Q',10)])

### EXPERIMENT
design=[b89AVX,S1p4zPbBYsA]
crossing=[b89AVX,S1p4zPbBYsA]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_2_0"))
### END