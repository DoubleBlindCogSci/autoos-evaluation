from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
oxsma = Factor("oxsma", ["dkmrro","tzl","exofh","oqygum","dztlb","bjsbn","otinn"])
def hajxn(oxsma):
     return oxsma == "dztlb"
def boo(oxsma):
     return "otinn" == oxsma
def yhniz(oxsma):
     return (not oxsma == "dztlb") and (not boo(oxsma))
oudtqf = Factor("aoxnsf", [DerivedLevel("rcyhwr", WithinTrial(hajxn, [oxsma])), DerivedLevel("affy", WithinTrial(boo, [oxsma])),DerivedLevel("echv", WithinTrial(yhniz, [oxsma]))])
### EXPERIMENT
design=[oxsma,oudtqf]
crossing=[oudtqf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END