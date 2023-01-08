from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
keexb = Factor("keexb", ["yjy","dzhdbv","ito","vbtij","vue"])
awngcs = Factor("awngcs", ["yjy","dzhdbv","ito","vbtij","vue"])
gqx = Factor("gqx", ["yjy","dzhdbv","ito","vbtij","vue"])
def nqjlly(keexb, awngcs, gqx):
    return keexb == awngcs
def hyvp(keexb, awngcs, gqx):
    return not nqjlly(keexb, awngcs, gqx)
bfwmmx = Factor("jsxqz", [DerivedLevel("haeoqr", WithinTrial(nqjlly, [keexb, awngcs, gqx])), DerivedLevel("jpsemq", WithinTrial(hyvp, [keexb, awngcs, gqx]))])
### EXPERIMENT
design=[keexb,awngcs,gqx,bfwmmx]
crossing=[bfwmmx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END