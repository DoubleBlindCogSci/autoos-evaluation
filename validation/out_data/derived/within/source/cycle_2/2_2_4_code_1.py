from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yytiv = Factor("yytiv", ["pek","csdat","iecoa","wmj","dounsc","mqkox","qmu"])
sjcll = Factor("sjcll", ["cxpc","uaflz","werkd","uaevq","qkmk","gbgkc"])
def msugnk(yytiv, sjcll):
    return yytiv == "qmu" or sjcll != "werkd"
def jhx(yytiv,sjcll):
    return yytiv != "qmu" and not (sjcll != "werkd")
vjsg = Factor("zmx", [DerivedLevel("fuldp", WithinTrial(msugnk, [yytiv, sjcll])), DerivedLevel("xopcn", WithinTrial(jhx, [yytiv, sjcll]))])
### EXPERIMENT
design=[yytiv,sjcll,vjsg]
crossing=[vjsg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END