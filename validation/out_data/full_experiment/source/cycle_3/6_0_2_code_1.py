from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
kqs = Factor("kqs", ["tqou", "zqh"])
xmy = Factor("xmy", ["nepkz", "ntiaq"])
mvcr = Factor("mvcr", ["tqou", "zqh"])
bzowuv = Factor("bzowuv", ["nepkz", "ntiaq"])
abkw = Factor("abkw", ["uil", "kes"])
zeqtq = Factor("zeqtq", ["nhzv", "npofit"])
design=[kqs,xmy,mvcr,bzowuv,abkw,zeqtq]
constraints=[AtLeastKInARow(3, abkw),AtMostKInARow(2, bzowuv)]
crossing=[mvcr,xmy]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_0_2"))
