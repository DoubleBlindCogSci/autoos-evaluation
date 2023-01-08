from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
keexb = Factor("keexb", ["yjy","dzhdbv","ito","vbtij","vue"])
awngcs = Factor("awngcs", ["yjy","dzhdbv","ito","vbtij","vue"])
gqx = Factor("gqx", ["yjy","dzhdbv","ito","vbtij","vue"])
def is_jsxqz_haeoqr(keexb, awngcs, gqx):
    return keexb == awngcs
def is_jsxqz_jpsemq(keexb, awngcs, gqx):
    return not is_jsxqz_haeoqr(keexb, awngcs, gqx)
jsxqz = Factor("jsxqz", [DerivedLevel("haeoqr", WithinTrial(is_jsxqz_haeoqr, [keexb, awngcs, gqx])), DerivedLevel("jpsemq", WithinTrial(is_jsxqz_jpsemq, [keexb, awngcs, gqx]))])

design=[keexb,awngcs,gqx,jsxqz]
crossing=[jsxqz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END