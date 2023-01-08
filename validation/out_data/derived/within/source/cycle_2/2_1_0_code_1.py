from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nudut = Factor("nudut", ["umzdlz","fvb","qiwyno","ifcuw","niew","kgazg","ptup"])
def sznme(nudut):
    return nudut != "umzdlz"
def erj(nudut):
    return not (nudut != "umzdlz")
udztkq = DerivedLevel("xfdf", WithinTrial(sznme, [nudut]))
vek = DerivedLevel("gwge", WithinTrial(erj, [nudut]))
qzohh = Factor("yveaom", [udztkq, vek])

### EXPERIMENT
design=[nudut,qzohh]
crossing=[qzohh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END