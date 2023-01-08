from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cnsld = Factor("cnsld", ["jgq", "tkdc"])
kkw = Factor("kkw", ["pdko", "ssawmy"])
wumf = Factor("wumf", ["flpf", "xmtpe"])
knyg = Factor("knyg", ["cavibs", "jutybp"])

### EXPERIMENT
design=[cnsld,kkw,wumf,knyg]
crossing=[[cnsld,kkw,wumf,knyg]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_6"))
### END