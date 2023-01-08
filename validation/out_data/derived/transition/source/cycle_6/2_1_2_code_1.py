from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vamcd = Factor("vamcd", ["vrqqx","rfmjl","azx","vlcx","szoehc","lnfm"])
def gyo(vamcd):
    return vamcd[0] == "azx" and vamcd[-1] == "vlcx"
def ypzgc(vamcd):
    return not (vamcd[0] == "azx") or vamcd[-1] != "vlcx"
jir = DerivedLevel("qrcgfn", Transition(gyo, [vamcd]))
gjiuj = DerivedLevel("swse", Transition(ypzgc, [vamcd]))
ckit = Factor("facr", [jir, gjiuj])

### EXPERIMENT
design=[vamcd,ckit]
crossing=[ckit]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END