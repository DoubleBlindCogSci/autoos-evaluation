from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
GVR3c9Glyc=Factor("}FzSMyl",["m LrDFvap",'wtF<LZFluJ','*qnh(M'])
VA1LOfkJm=Factor("BIwkduEvUm",['~Gq',"LrLs","MstFu~dL4fyrCY"])
Kcztts7_=Factor("pc|AbZlUc",["hhwdX&Y<@","E~ZwGxz","L<YDO"])
TeYpDyHCr_S="0x&gWPPs"
MkdGw21=['qdBmj%qSq4_xfa','jKYT)7ci',TeYpDyHCr_S,'c|!hF:ooQ>ie']
NRkeM=Factor("Qrw?CIO",MkdGw21)

### EXPERIMENT
design=[GVR3c9Glyc,VA1LOfkJm,Kcztts7_,NRkeM]
crossing=[GVR3c9Glyc,VA1LOfkJm,Kcztts7_,NRkeM]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_4_1"))
### END