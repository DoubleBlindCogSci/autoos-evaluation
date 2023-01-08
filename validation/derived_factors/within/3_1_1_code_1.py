from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bolifi = Factor("bolifi", ["sugkl","zvzumm","udoj","gtd","iixax","tdstz","ndl"])
def mgjxmj(bolifi):
     return bolifi == "tdstz"
def gsezhg(bolifi):
     return "ndl" == bolifi
def wrb(bolifi):
     return (bolifi != "tdstz") and (not bolifi == "ndl")
ukfkbi = Factor("jmerhw", [DerivedLevel("gtlcen", WithinTrial(mgjxmj, [bolifi])), DerivedLevel("ximt", WithinTrial(gsezhg, [bolifi])),DerivedLevel("acwjo", WithinTrial(wrb, [bolifi]))])
### EXPERIMENT
design=[bolifi,ukfkbi]
crossing=[ukfkbi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END