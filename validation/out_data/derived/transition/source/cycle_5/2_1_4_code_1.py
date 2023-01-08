from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mgcc = Factor("mgcc", ["ylzbn","lcxh","vkkxfc","hhdo","pkzixb"])
def jldb(mgcc):
    return mgcc[0] == "pkzixb" or mgcc[-1] != "ylzbn"
def qrq(mgcc):
    return not jldb(mgcc)
dlsk = Factor("jdznc", [DerivedLevel("lepnbv", Transition(jldb, [mgcc])), DerivedLevel("euqff", Transition(qrq, [mgcc]))])
### EXPERIMENT
design=[mgcc,dlsk]
crossing=[dlsk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END