from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
sdlbze = Factor("sdlbze", ["gar","ydyws","ronryb","kowlow","aduc","yhyj","yepupr","fgzxj"])
def qxn(sdlbze):
     return "gar" == sdlbze[-3] and not sdlbze[-1] == "gar"
def hbf(sdlbze):
     return not "gar" == sdlbze[-3] and  sdlbze[-1] == "aduc"
def jfqp(sdlbze):
     return (sdlbze[-3] != "gar") and (sdlbze[-1] != "aduc")
jmxvrl = Factor("cfa", [DerivedLevel("nrzh", Window(qxn, [sdlbze],4,1)), DerivedLevel("hyzlfw", Window(hbf, [sdlbze],4,1)),DerivedLevel("osuagf", Window(jfqp, [sdlbze],4,1))])
### EXPERIMENT
design=[sdlbze,jmxvrl]
crossing=[jmxvrl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END