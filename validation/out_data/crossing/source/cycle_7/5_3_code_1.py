from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eghw = Factor("eghw", ["fttaly", "dko"])
hzkh = Factor("hzkh", ["vqx", "uiwst"])
uwrr = Factor("uwrr", ["zhyh", "lnizsc"])
mpj = Factor("mpj", ["vogrim", "zuovg"])
fafja = Factor("fafja", ["xxlyr", "urbs"])

### EXPERIMENT
design=[eghw,hzkh,uwrr,mpj,fafja]
crossing=[[eghw,hzkh,uwrr,mpj,fafja]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_3"))
### END