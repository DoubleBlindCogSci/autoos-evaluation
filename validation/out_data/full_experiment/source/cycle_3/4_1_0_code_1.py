from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
updm = Factor("updm", ["etzxb", "jpfb"])
zvkc = Factor("zvkc", ["nrt", "rbvvsb"])
sxwaf = Factor("sxwaf", ["etzxb", "jpfb"])
pcyuwu = Factor("pcyuwu", ["nrt", "rbvvsb"])
def yazsbf (zvkc, updm):
    return zvkc == updm
def pmxs (zvkc, updm):
    return not yazsbf(zvkc, updm)
hbo = Factor("hbo", [DerivedLevel("oenvuo", WithinTrial(yazsbf, [zvkc, updm])), DerivedLevel("jnvo", WithinTrial(pmxs, [zvkc, updm]))])
design=[hbo,updm,zvkc,sxwaf,pcyuwu]
constraints=[]
crossing=[pcyuwu,hbo]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_0"))
