from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ylflj = Factor("ylflj", ["pegaf","elsv","sqfg","ylfirl","ebyn","fixt","oqpnm","zwuv"])
def oxqwz(ylflj):
     return "ebyn" == ylflj
def qbb(ylflj):
     return ylflj == "elsv"
def ufvhz(ylflj):
     return (not oxqwz(ylflj)) and (not ylflj == "elsv")
bfg = Factor("wblgfh", [DerivedLevel("uryw", WithinTrial(oxqwz, [ylflj])), DerivedLevel("cajyd", WithinTrial(qbb, [ylflj])),DerivedLevel("dbul", WithinTrial(ufvhz, [ylflj]))])
### EXPERIMENT
design=[ylflj,bfg]
crossing=[bfg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END