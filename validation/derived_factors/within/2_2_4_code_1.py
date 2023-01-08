from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vuwv = Factor("vuwv", ["heqezc","mopvax","qetxx","adc","oxfzjn"])
ojq = Factor("ojq", ["heqezc","mopvax","qetxx","adc","oxfzjn"])
pyl = Factor("pyl", ["heqezc","mopvax","qetxx","adc","oxfzjn"])
def gjyzgy(vuwv, ojq, pyl):
    return vuwv == ojq or vuwv == pyl
def ivjfzr(vuwv, ojq, pyl):
    return not (vuwv == ojq) and vuwv != pyl
crzh = Factor("kcy", [DerivedLevel("qal", WithinTrial(gjyzgy, [vuwv, ojq, pyl])), DerivedLevel("grhrf", WithinTrial(ivjfzr, [vuwv, ojq, pyl]))])
### EXPERIMENT
design=[vuwv,ojq,pyl,crzh]
crossing=[crzh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END