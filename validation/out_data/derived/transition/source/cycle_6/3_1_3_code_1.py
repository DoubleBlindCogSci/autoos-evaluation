from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
wov = Factor("wov", ["lgit","wxcyas","zle","rlse","kum","zkgbw"])
def ymbt(wov):
     return wov[0] == "lgit" and wov[-1] != "wxcyas"
def eooqgz(wov):
     return (not "lgit" != wov[0]) and  "wxcyas" == wov[-1]
def vexei(wov):
     return (wov[0] != "lgit") and (not wov[-1] == "wxcyas")
wvn = Factor("kuuz", [DerivedLevel("kgwv", Transition(ymbt, [wov])), DerivedLevel("jxl", Transition(eooqgz, [wov])),DerivedLevel("sfam", Transition(vexei, [wov]))])
### EXPERIMENT
design=[wov,wvn]
crossing=[wvn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END