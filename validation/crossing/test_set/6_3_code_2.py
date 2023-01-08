from sweetpea import *
import os
_dir=os.path.dirname(__file__)
zlk = Factor("zlk", ["ugxjy", "fysw"])
iyq = Factor("iyq", ["zccrb", "lgkpe"])
uoayq = Factor("uoayq", ["mvnkm", "vnd"])
ujtk = Factor("ujtk", ["vdqgzf", "wlnu"])
ciuli = Factor("ciuli", ["erc", "ecac"])
sxg = Factor("sxg", ["glo", "igszl"])
constraints = []
crossing = [zlk, iyq, uoayq, ujtk, ciuli, sxg]


design=[zlk,iyq,uoayq,ujtk,ciuli,sxg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_3"))

### END