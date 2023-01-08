from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ojjguv = Factor("ojjguv", ["aemmu","ydur","vlzl","cwzhbe","pyvrq","cfexy","duwul"])
def hmhn(ojjguv):
     return ojjguv == "cwzhbe"
def ookq(ojjguv):
     return ojjguv == "pyvrq"
def ruv(ojjguv):
     return (not ojjguv == "cwzhbe") and (not ookq(ojjguv))
axaixj = Factor("jxrp", [DerivedLevel("wbdi", WithinTrial(hmhn, [ojjguv])), DerivedLevel("bkrpa", WithinTrial(ookq, [ojjguv])),DerivedLevel("jhs", WithinTrial(ruv, [ojjguv]))])
### EXPERIMENT
design=[ojjguv,axaixj]
crossing=[axaixj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END