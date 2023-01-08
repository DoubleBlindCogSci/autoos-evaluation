from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
askal = Factor("askal", ["rkwp","kmd","wwk","pbwgni","rir"])
def drxora(askal):
    return askal != "rir" and askal == "wwk"
def defvs(askal):
    return askal == "rir" or askal != "wwk"
bkisi = Factor("ytik", [DerivedLevel("mwumrz", WithinTrial(drxora, [askal])), DerivedLevel("qtz", WithinTrial(defvs, [askal]))])
### EXPERIMENT
design=[askal,bkisi]
crossing=[bkisi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END