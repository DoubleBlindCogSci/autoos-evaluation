from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
khb= Factor("khb", ["duuly","pkdwt","nteh","nitsa","jnzn"])
jotilz= Factor("jotilz", ["duuly","pkdwt","nteh","nitsa","jnzn"])
tdbs= Factor("tdbs", ["duuly","pkdwt","nteh","nitsa","jnzn"])
def is_kgpp_fzy(khb, jotilz, tdbs):
    return khb[0] == tdbs[-1]
def is_kgpp_dnr(khb, jotilz, tdbs):
    return not is_kgpp_fzy(khb, jotilz, tdbs)
kgpp= Factor("kgpp", [DerivedLevel("fzy", Transition(is_kgpp_fzy, [khb, jotilz, tdbs])), DerivedLevel("dnr", Transition(is_kgpp_dnr, [khb, jotilz, tdbs]))])

design=[khb,jotilz,tdbs,kgpp]
crossing=[kgpp]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END
