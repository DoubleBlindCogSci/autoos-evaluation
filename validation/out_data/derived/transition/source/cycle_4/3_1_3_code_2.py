from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kgtk = Factor("kgtk", ["rgved","ukpjpb","sfyyo","wcf","jitg","dmwzq","vnuph"])
def is_gkzn_pyxd(kgtk):
    return kgtk[0] == "sfyyo" and kgtk[-1] != "rgved"
def is_gkzn_dlyye(kgtk):
    return kgtk[0] != "sfyyo" and kgtk[-1] == "rgved"
def is_gkzn_yydfj(kgtk):
    return not (is_gkzn_pyxd(kgtk) or is_gkzn_dlyye(kgtk))
gkzn = Factor("gkzn", [DerivedLevel("pyxd", Transition(is_gkzn_pyxd, [kgtk])), DerivedLevel("dlyye", Transition(is_gkzn_dlyye, [kgtk])), DerivedLevel("yydfj", Transition(is_gkzn_yydfj, [kgtk]))])

design=[kgtk,gkzn]
crossing=[gkzn]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END