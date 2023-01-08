from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
khb = Factor("khb", ["duuly","pkdwt","nteh","nitsa","jnzn"])
jotilz = Factor("jotilz", ["duuly","pkdwt","nteh","nitsa","jnzn"])
tdbs = Factor("tdbs", ["duuly","pkdwt","nteh","nitsa","jnzn"])
def ftdyy(khb, tdbs, jotilz):
    return khb[0] == tdbs[-1]
def wwry(khb, tdbs, jotilz):
    return not ftdyy(khb, tdbs, jotilz)
oxamk = Factor("kgpp", [DerivedLevel("fzy", Transition(ftdyy, [khb, jotilz, tdbs])), DerivedLevel("dnr", Transition(wwry, [khb, jotilz, tdbs]))])
### EXPERIMENT
design=[khb,jotilz,tdbs,oxamk]
crossing=[oxamk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END