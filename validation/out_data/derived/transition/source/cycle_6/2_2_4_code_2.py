from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
chim = Factor("chim", ["ljso","ihkf","mtb","sghb","bin","lfwmh"])
qtz = Factor("qtz", ["ljso","ihkf","mtb","sghb","bin","lfwmh"])
mies = Factor("mies", ["ljso","ihkf","mtb","sghb","bin","lfwmh"])
def is_jkq_wfa(chim, qtz, mies):
    return chim[0] == mies[-1] or chim[-1] == qtz[0]
def is_jkq_phgv(chim, qtz, mies):
    return not is_jkq_wfa(chim, qtz, mies)
jkq = Factor("jkq", [DerivedLevel("wfa", Transition(is_jkq_wfa, [chim, qtz, mies])), DerivedLevel("phgv", Transition(is_jkq_phgv, [chim, qtz, mies]))])

design=[chim,qtz,mies,jkq]
crossing=[jkq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END