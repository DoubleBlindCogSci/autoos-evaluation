from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zwin = Factor("zwin", ["gylpcf","zdd","tid","lipuj","aajchu","flbwb","bixk","asxya"])
tqxev = Factor("tqxev", ["hnabb","nenp","blvuz","tkvk","rdjog","yub"])
def hrvcr(zwin, tqxev):
     return zwin[0] == "tid" and not tqxev[-1] == "yub"
def merfpo(zwin, tqxev):
     return "tid" != zwin[0] and  tqxev[-1] == "yub"
def rpuwqi(zwin, tqxev):
     return (not zwin[0] == "tid") and (tqxev[-1] != "yub")
oegvyf = Factor("nwm", [DerivedLevel("fbnbrn", Window(hrvcr, [zwin, tqxev],2,1)), DerivedLevel("gex", Window(merfpo, [zwin, tqxev],2,1)),DerivedLevel("gliqlb", Window(rpuwqi, [zwin, tqxev],2,1))])
### EXPERIMENT
design=[zwin,tqxev,oegvyf]
crossing=[oegvyf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END