from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
fum = Factor("fum", ["vrgjb","kzdb","otqv","lqyhz","bvfjr","nfueqd"])
def dlzqg(fum):
     return "nfueqd" == fum[0] and not fum[-1] == "otqv"
def jcyiou(fum):
     return (not "nfueqd" != fum[0]) and  fum[-1] == "otqv"
def fmxqvh(fum):
     return (fum[0] != "nfueqd") and (fum[-1] != "otqv")
ieym = Factor("sfk", [DerivedLevel("gthv", Transition(dlzqg, [fum])), DerivedLevel("lyd", Transition(jcyiou, [fum])),DerivedLevel("ctzx", Transition(fmxqvh, [fum]))])
### EXPERIMENT
design=[fum,ieym]
crossing=[ieym]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END