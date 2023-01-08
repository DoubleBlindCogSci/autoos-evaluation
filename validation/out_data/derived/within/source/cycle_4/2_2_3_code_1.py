from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dtx = Factor("dtx", ["dkx","sjtmx","bmkxcm","xoi","ftcho","xpiwfo"])
wcftzr = Factor("wcftzr", ["dkx","sjtmx","bmkxcm","xoi","ftcho","xpiwfo"])
jdewe = Factor("jdewe", ["dkx","sjtmx","bmkxcm","xoi","ftcho","xpiwfo"])
def bxu(dtx, jdewe, wcftzr):
    return dtx != jdewe
def qkumf(dtx, jdewe, wcftzr):
    return dtx == jdewe
czdb = Factor("aumdnp", [DerivedLevel("gazr", WithinTrial(bxu, [dtx, wcftzr, jdewe])), DerivedLevel("kcn", WithinTrial(qkumf, [dtx, wcftzr, jdewe]))])
### EXPERIMENT
design=[dtx,wcftzr,jdewe,czdb]
crossing=[czdb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END