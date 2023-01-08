from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vngg = Factor("vngg", ["vjvce","tzwe","jpsz","yqurrp","lbwqgy","kdk"])
def ewjqx(vngg):
    return vngg[-2] == "kdk" and vngg[-1] == "vjvce"
def gbvix(vngg):
    return not ewjqx(vngg)
zvd = DerivedLevel("lcyt", Window(ewjqx, [vngg],3,1))
uxxyk = DerivedLevel("jndi", Window(gbvix, [vngg],3,1))
nruez = Factor("agmtm", [zvd, uxxyk])

### EXPERIMENT
design=[vngg,nruez]
crossing=[nruez]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END