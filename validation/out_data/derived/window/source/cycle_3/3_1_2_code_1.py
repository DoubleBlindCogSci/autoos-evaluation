from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
roi = Factor("roi", ["bgydaq","lgvbd","oyrlk","fdzye","pbyu","sdnyy","tcgzw","yvilsd"])
def jjbzm(roi):
     return "fdzye" == roi[0] and not roi[-3] == "fdzye"
def myfde(roi):
     return roi[0] != "fdzye" and  roi[-3] == "lgvbd"
def xhr(roi):
     return (roi[0] != "fdzye") and (not myfde(roi))
hmi = Factor("gfws", [DerivedLevel("unzl", Window(jjbzm, [roi],4,1)), DerivedLevel("wugp", Window(myfde, [roi],4,1)),DerivedLevel("quuxfe", Window(xhr, [roi],4,1))])
### EXPERIMENT
design=[roi,hmi]
crossing=[hmi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END