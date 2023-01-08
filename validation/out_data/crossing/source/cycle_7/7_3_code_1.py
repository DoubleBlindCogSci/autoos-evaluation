from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pzdf = Factor("pzdf", ["sum", "rrv"])
drzdl = Factor("drzdl", ["cfs", "ahnsy"])
aeuu = Factor("aeuu", ["ryhl", "pwple"])
utwt = Factor("utwt", ["uulf", "kpoi"])
demlcv = Factor("demlcv", ["paeed", "yanx"])
dzhrj = Factor("dzhrj", ["qtsvi", "vfcr"])
zxtc = Factor("zxtc", ["btlsdv", "fgybf"])

### EXPERIMENT
design=[pzdf,drzdl,aeuu,utwt,demlcv,dzhrj,zxtc]
crossing=[[pzdf,drzdl,aeuu,utwt,demlcv,dzhrj,zxtc]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_3"))
### END