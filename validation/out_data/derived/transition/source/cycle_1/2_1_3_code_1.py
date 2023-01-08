from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
aus = Factor("aus", ["joiup","gnnuy","alus","ijtzt","bpi","utz"])
def lcz(aus):
    return aus[0] == "bpi" or aus[-1] == "joiup"
def bcb(aus):
    return aus[0] != "bpi" and aus[-1] != "joiup"
wyisu = Factor("nsvlgj", [DerivedLevel("yfwz", Transition(lcz, [aus])), DerivedLevel("mhpggi", Transition(bcb, [aus]))])
### EXPERIMENT
design=[aus,wyisu]
crossing=[wyisu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END