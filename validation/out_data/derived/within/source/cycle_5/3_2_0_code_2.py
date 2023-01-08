from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mrajg = Factor("mrajg", ["mfbp","iyoym","igq","liuw","expsg","btfs","jzclr"])
gvlcit = Factor("gvlcit", ["mfbp","iyoym","igq","liuw","expsg","btfs","jzclr"])
obi = Factor("obi", ["mfbp","iyoym","igq","liuw","expsg","btfs","jzclr"])
def is_bjc_ggf(mrajg, gvlcit, obi):
    return mrajg == gvlcit
def is_bjc_jwysy(mrajg, gvlcit, obi):
    return mrajg != gvlcit and obi == mrajg
def is_bjc_mdpjmz(mrajg, gvlcit, obi):
    return not (is_bjc_ggf(mrajg, gvlcit, obi) or is_bjc_jwysy(mrajg, gvlcit, obi))
bjc = Factor("bjc", [DerivedLevel("ggf", WithinTrial(is_bjc_ggf, [mrajg, gvlcit, obi])), DerivedLevel("jwysy", WithinTrial(is_bjc_jwysy, [mrajg, gvlcit, obi])), DerivedLevel("mdpjmz", WithinTrial(is_bjc_mdpjmz, [mrajg, gvlcit, obi]))])

design=[mrajg,gvlcit,obi,bjc]
crossing=[bjc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END