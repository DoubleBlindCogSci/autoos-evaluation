from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mrajg = Factor("mrajg", ["mfbp","iyoym","igq","liuw","expsg","btfs","jzclr"])
gvlcit = Factor("gvlcit", ["mfbp","iyoym","igq","liuw","expsg","btfs","jzclr"])
obi = Factor("obi", ["mfbp","iyoym","igq","liuw","expsg","btfs","jzclr"])
def yylf(mrajg, gvlcit, obi):
     return mrajg == gvlcit
def wrayup(mrajg, gvlcit, obi):
     return gvlcit != mrajg and obi == mrajg
def pngugw(mrajg, gvlcit, obi):
     return (mrajg != gvlcit) and (not wrayup(mrajg, gvlcit, obi))
sqcmon = Factor("bjc", [DerivedLevel("ggf", WithinTrial(yylf, [mrajg, gvlcit, obi])), DerivedLevel("jwysy", WithinTrial(wrayup, [mrajg, gvlcit, obi])),DerivedLevel("mdpjmz", WithinTrial(pngugw, [mrajg, gvlcit, obi]))])
### EXPERIMENT
design=[mrajg,gvlcit,obi,sqcmon]
crossing=[sqcmon]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END