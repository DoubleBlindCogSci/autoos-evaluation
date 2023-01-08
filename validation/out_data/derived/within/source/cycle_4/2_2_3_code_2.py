from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dtx = Factor("dtx", ["dkx","sjtmx","bmkxcm","xoi","ftcho","xpiwfo"])
wcftzr = Factor("wcftzr", ["dkx","sjtmx","bmkxcm","xoi","ftcho","xpiwfo"])
jdewe = Factor("jdewe", ["dkx","sjtmx","bmkxcm","xoi","ftcho","xpiwfo"])
def is_aumdnp_gazr(dtx, wcftzr, jdewe):
    return dtx != jdewe
def is_aumdnp_kcn(dtx, wcftzr, jdewe):
    return not is_aumdnp_gazr(dtx, wcftzr, jdewe)
aumdnp = Factor("aumdnp", [DerivedLevel("gazr", WithinTrial(is_aumdnp_gazr, [dtx, wcftzr, jdewe])), DerivedLevel("kcn", WithinTrial(is_aumdnp_kcn, [dtx, wcftzr, jdewe]))])

design=[dtx,wcftzr,jdewe,aumdnp]
crossing=[aumdnp]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END