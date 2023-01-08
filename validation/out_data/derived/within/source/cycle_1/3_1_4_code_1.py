from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xfow = Factor("xfow", ["rubs","mxu","uup","yrgbu","mvbco","oujomr"])
def ncyj(xfow):
     return "mxu" == xfow
def zrquht(xfow):
     return "mvbco" == xfow
def fogvp(xfow):
     return (xfow != "mxu") and (xfow != "mvbco")
hqvbn = Factor("kktv", [DerivedLevel("htlesb", WithinTrial(ncyj, [xfow])), DerivedLevel("wcnh", WithinTrial(zrquht, [xfow])),DerivedLevel("sjbnde", WithinTrial(fogvp, [xfow]))])
### EXPERIMENT
design=[xfow,hqvbn]
crossing=[hqvbn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END