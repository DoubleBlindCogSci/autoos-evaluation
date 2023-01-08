from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
leyw = Factor("leyw", ["dnxv","vzpmsy","zwxz","wtv","ejuqc","dgd"])
luzdp = Factor("luzdp", ["dnxv","vzpmsy","zwxz","wtv","ejuqc","dgd"])
bqup = Factor("bqup", ["dnxv","vzpmsy","zwxz","wtv","ejuqc","dgd"])
def kpnw(leyw, bqup, luzdp):
    return leyw[-2] == bqup[-1]
def dradq(leyw, bqup, luzdp):
    return leyw[-2] != bqup[-1]
pqksg = Factor("xlqpo", [DerivedLevel("abfhmd", Window(kpnw, [leyw, luzdp, bqup],3,1)), DerivedLevel("xfaret", Window(dradq, [leyw, luzdp, bqup],3,1))])
### EXPERIMENT
design=[leyw,luzdp,bqup,pqksg]
crossing=[pqksg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END