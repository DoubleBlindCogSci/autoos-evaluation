from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ouAk=['V|eCcW',"Vt:LhBYQ",'j9z',Level('VuIL>jwMLWPA8L',3),"mjeM6wMKYIK",Level("SDC",6),'OGgiFCbX',Level('fIRynxfuQO(',9),'tkF9[u*Cs&HjP']
WTW0SiRNb0g=Factor('9Hbo',[ouAk[4],"UqULnkQ_jBt",Level("ueEbBR$NX1kV}i",4),'X[nF$w;:g','tMGI','SGm',"FBovs"])

### EXPERIMENT
design=[WTW0SiRNb0g]
crossing=[WTW0SiRNb0g]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_1_0"))
### END