from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
sybvjo = Factor("sybvjo", ["twmoh", "vfo"])
ufl = Factor("ufl", ["sltkjj", "pedj"])
xiv = Factor("xiv", ["ldoqwk", "teo"])
ztj = Factor("ztj", ["bdq", "oaxqt"])
hta = Factor("hta", ["yena", "locr"])
klrnqd = Factor("klrnqd", ["qeo", "bwod"])

### EXPERIMENT
design=[sybvjo,ufl,xiv,ztj,hta,klrnqd]
crossing=[[sybvjo,ufl,xiv,ztj,hta,klrnqd]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_0"))
### END