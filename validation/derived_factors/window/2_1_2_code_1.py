from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xgtcl = Factor("xgtcl", ["whmbm","jnj","porzs","mph","sbjdi","hbz","ziya"])
def elho(xgtcl):
    return xgtcl[-1] == "sbjdi" or xgtcl[-2] == "ziya"
def ofohk(xgtcl):
    return not elho(xgtcl)
esghry = DerivedLevel("fkd", Window(elho, [xgtcl],3,1))
lreq = DerivedLevel("hnepud", Window(ofohk, [xgtcl],3,1))
tfahh = Factor("fpqvm", [esghry, lreq])

### EXPERIMENT
design=[xgtcl,tfahh]
crossing=[tfahh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END