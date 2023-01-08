from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zlk = Factor("zlk", ["ugxjy", "fysw"])
iyq = Factor("iyq", ["zccrb", "lgkpe"])
uoayq = Factor("uoayq", ["mvnkm", "vnd"])
ujtk = Factor("ujtk", ["vdqgzf", "wlnu"])
ciuli = Factor("ciuli", ["erc", "ecac"])
sxg = Factor("sxg", ["glo", "igszl"])

### EXPERIMENT
design=[zlk,iyq,uoayq,ujtk,ciuli,sxg]
crossing=[[zlk,iyq,uoayq,ujtk,ciuli,sxg]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_3"))
### END