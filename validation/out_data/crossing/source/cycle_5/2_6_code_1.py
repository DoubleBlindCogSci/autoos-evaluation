from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
grzvek = Factor("grzvek", ["sjt", "rbwp"])
tcd = Factor("tcd", ["nnp", "jol"])
lnogmi = Factor("lnogmi", ["jis", "wfxgop"])
jvvk = Factor("jvvk", ["vezyi", "rkw"])
wudb = Factor("wudb", ["tzv", "alnknm"])

### EXPERIMENT
design=[grzvek,tcd,lnogmi,jvvk,wudb]
crossing=[[grzvek,tcd,lnogmi],[jvvk,wudb],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_6"))
### END