from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ffp = Factor("ffp", ["fmie","buekwg","cybl","evsdjz","inxtj","rbc"])
def mtdqud(ffp):
     return "rbc" == ffp[-2] and not ffp[-1] == "rbc"
def zbu(ffp):
     return ffp[-2] != "rbc" and  ffp[-1] == "buekwg"
def eap(ffp):
     return (ffp[-2] != "rbc") and (not ffp[-1] == "buekwg")
djaq = DerivedLevel("ydoqi", Window(mtdqud, [ffp],3,1))
ulcv = DerivedLevel("qsap", Window(zbu, [ffp],3,1))
xtbi = DerivedLevel("vgta", Window(eap, [ffp],3,1))
elrio = Factor("pug", [djaq, ulcv, xtbi])

### EXPERIMENT
design=[ffp,elrio]
crossing=[elrio]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END