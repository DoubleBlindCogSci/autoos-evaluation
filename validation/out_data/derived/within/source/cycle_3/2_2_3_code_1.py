from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
biu = Factor("biu", ["sassd","gotujg","elrdw","umju","kdzoug"])
fva = Factor("fva", ["sassd","gotujg","elrdw","umju","kdzoug"])
xpdbm = Factor("xpdbm", ["sassd","gotujg","elrdw","umju","kdzoug"])
def lgusp(biu, xpdbm, fva):
    return biu != xpdbm and biu == fva
def ekz(biu, xpdbm, fva):
    return not lgusp(biu, xpdbm, fva)
tftezd = Factor("zaab", [DerivedLevel("btyx", WithinTrial(lgusp, [biu, fva, xpdbm])), DerivedLevel("mbxq", WithinTrial(ekz, [biu, fva, xpdbm]))])
### EXPERIMENT
design=[biu,fva,xpdbm,tftezd]
crossing=[tftezd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END