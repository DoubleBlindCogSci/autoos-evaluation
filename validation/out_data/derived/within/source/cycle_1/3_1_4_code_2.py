from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xfow= Factor("xfow", ["rubs","mxu","uup","yrgbu","mvbco","oujomr"])
def is_kktv_htlesb(xfow):
    return xfow == "mxu"
def is_kktv_wcnh(xfow):
    return xfow == "mvbco"
def is_kktv_sjbnde(xfow):
    return not is_kktv_htlesb(xfow) and not is_kktv_wcnh(xfow)
kktv= Factor("kktv", [DerivedLevel("htlesb", WithinTrial(is_kktv_htlesb, [xfow])), DerivedLevel("wcnh", WithinTrial(is_kktv_wcnh, [xfow])), DerivedLevel("sjbnde", WithinTrial(is_kktv_sjbnde, [xfow]))])

design=[xfow,kktv]
crossing=[kktv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END
