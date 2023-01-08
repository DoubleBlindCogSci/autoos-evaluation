from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
chim = Factor("chim", ["ljso","ihkf","mtb","sghb","bin","lfwmh"])
qtz = Factor("qtz", ["ljso","ihkf","mtb","sghb","bin","lfwmh"])
mies = Factor("mies", ["ljso","ihkf","mtb","sghb","bin","lfwmh"])
def xps(chim, mies, qtz):
    return chim[0] == mies[-1] or chim[-1] == qtz[0]
def lpx(chim, mies, qtz):
    return chim[0] != mies[-1] and chim[-1] != qtz[0]
oxege = Factor("jkq", [DerivedLevel("wfa", Transition(xps, [chim, qtz, mies])), DerivedLevel("phgv", Transition(lpx, [chim, qtz, mies]))])
### EXPERIMENT
design=[chim,qtz,mies,oxege]
crossing=[oxege]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END