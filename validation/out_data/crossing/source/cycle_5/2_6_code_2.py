from sweetpea import *
import os
_dir=os.path.dirname(__file__)
grzvek = Factor("grzvek", ["sjt", "rbwp"])
tcd = Factor("tcd", ["nnp", "jol"])
lnogmi = Factor("lnogmi", ["jis", "wfxgop"])
jvvk = Factor("jvvk", ["vezyi", "rkw"])
wudb = Factor("wudb", ["tzv", "alnknm"])
constraints = []
crossing = [[grzvek, tcd, lnogmi], [jvvk, wudb]]


design=[grzvek,tcd,lnogmi,jvvk,wudb]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_6"))

### END