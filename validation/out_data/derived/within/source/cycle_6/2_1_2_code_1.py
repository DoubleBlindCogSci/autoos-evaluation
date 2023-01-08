from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
fmq = Factor("fmq", ["cvsb","yerlnd","bbnyn","jfg","ivw"])
def auxcng(fmq):
    return fmq != "cvsb" or fmq != "yerlnd"
def xxv(fmq):
    return fmq == "cvsb" and fmq == "yerlnd"
nemurp = DerivedLevel("xldt", WithinTrial(auxcng, [fmq]))
rbseii = DerivedLevel("fxq", WithinTrial(xxv, [fmq]))
rxlaam = Factor("kkvmaj", [nemurp, rbseii])

### EXPERIMENT
design=[fmq,rxlaam]
crossing=[rxlaam]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END