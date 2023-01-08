from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
updm = Factor("updm", ["etzxb", "jpfb"])
zvkc = Factor("zvkc", ["nrt", "rbvvsb"])
sxwaf = Factor("sxwaf", ["etzxb", "jpfb"])
pcyuwu = Factor("pcyuwu", ["nrt", "rbvvsb"])
def is_hbo_oenvuo(zvkc, updm):
    return zvkc == updm
def is_hbo_jnvo(zvkc, updm):
    return not is_hbo_oenvuo(zvkc, updm)
hbo = Factor("hbo", [DerivedLevel("oenvuo", WithinTrial(is_hbo_oenvuo, [zvkc, updm])), DerivedLevel("jnvo", WithinTrial(is_hbo_jnvo, [zvkc, updm]))])
constraints = []
crossing = [pcyuwu, hbo]

design=[updm,zvkc,sxwaf,pcyuwu,hbo]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_0"))
