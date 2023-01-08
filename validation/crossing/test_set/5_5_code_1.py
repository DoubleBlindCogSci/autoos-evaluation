from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bpew = Factor("bpew", ["kfsej", "ijufxg"])
krdkp = Factor("krdkp", ["ybr", "ibw"])
pjz = Factor("pjz", ["akr", "pzknju"])
heazj = Factor("heazj", ["ntajmm", "xic"])
vczl = Factor("vczl", ["qhksl", "wbawyv"])

### EXPERIMENT
design=[bpew,krdkp,pjz,heazj,vczl]
crossing=[[bpew,krdkp,pjz,heazj,vczl]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_5"))
### END