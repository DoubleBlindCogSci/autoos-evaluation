from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yytiv= Factor("yytiv", ["pek","csdat","iecoa","wmj","dounsc","mqkox","qmu"])
sjcll= Factor("sjcll", ["cxpc","uaflz","werkd","uaevq","qkmk","gbgkc"])
def is_zmx_fuldp(yytiv, sjcll):
    return yytiv == "qmu" or sjcll != "werkd"
def is_zmx_xopcn(yytiv, sjcll):
    return not is_zmx_fuldp(yytiv, sjcll)
zmx= Factor("zmx", [DerivedLevel("fuldp", WithinTrial(is_zmx_fuldp, [yytiv, sjcll])), DerivedLevel("xopcn", WithinTrial(is_zmx_xopcn, [yytiv, sjcll]))])

design=[yytiv,sjcll, zmx]
crossing=[zmx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END
