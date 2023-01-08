from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ctsqk = Factor("ctsqk", ["ghrgkn","aib","udt","enst","thwcoh","gsny","yiaap","gipumh"])
def pqlagk(ctsqk):
     return "thwcoh" == ctsqk
def gagq(ctsqk):
     return "gipumh" == ctsqk
def chy(ctsqk):
     return (not ctsqk == "thwcoh") and (ctsqk != "gipumh")
vkkmy = Factor("qpl", [DerivedLevel("hij", WithinTrial(pqlagk, [ctsqk])), DerivedLevel("uduqbi", WithinTrial(gagq, [ctsqk])),DerivedLevel("vpdbxc", WithinTrial(chy, [ctsqk]))])
### EXPERIMENT
design=[ctsqk,vkkmy]
crossing=[vkkmy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END