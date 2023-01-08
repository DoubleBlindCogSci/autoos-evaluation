from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nudut= Factor("nudut", ["umzdlz","fvb","qiwyno","ifcuw","niew","kgazg","ptup"])
def is_yveaom_xfdf(nudut):
    return nudut != "umzdlz"
def is_yveaom_gwge(nudut):
    return nudut == "umzdlz"
yveaom= Factor("yveaom", [DerivedLevel("xfdf", WithinTrial(is_yveaom_xfdf, [nudut])), DerivedLevel("gwge", WithinTrial(is_yveaom_gwge, [nudut]))])

design=[nudut, yveaom]
crossing=[yveaom]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END
