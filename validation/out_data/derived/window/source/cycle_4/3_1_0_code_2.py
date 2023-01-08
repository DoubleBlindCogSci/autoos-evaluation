from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zdbxi = Factor("zdbxi", ["hcj","pnqr","edln","jtizo","kueg","vid","wzchdg"])
def is_mfnjeh_nud(zdbxi):
    return zdbxi[-1] == "pnqr" and zdbxi[0] != "pnqr"
def is_mfnjeh_uah(zdbxi):
    return zdbxi[-1] != "pnqr" and zdbxi[0] == "edln"
def is_mfnjeh_ugi(zdbxi):
    return not (is_mfnjeh_nud(zdbxi) or is_mfnjeh_uah(zdbxi))
mfnjeh= Factor("mfnjeh", [DerivedLevel("nud", Window(is_mfnjeh_nud, [zdbxi], 2, 1)), DerivedLevel("uah", Window(is_mfnjeh_uah, [zdbxi], 2, 1)), DerivedLevel("ugi", Window(is_mfnjeh_ugi, [zdbxi], 2, 1))])

design=[zdbxi,mfnjeh]
crossing=[mfnjeh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END