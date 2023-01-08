from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ush = Factor("ush", ["mtzxp","tdgw","szz","asc","pjni","umob","vhrm"])
roxpg = Factor("roxpg", ["mtzxp","tdgw","szz","asc","pjni","umob","vhrm"])
rpnreo = Factor("rpnreo", ["mtzxp","tdgw","szz","asc","pjni","umob","vhrm"])
def xyes(ush, roxpg, rpnreo):
     return roxpg == ush
def cfbw(ush, roxpg, rpnreo):
     return roxpg != ush and rpnreo == ush
def vod(ush, roxpg, rpnreo):
     return (not ush == roxpg) and (ush != rpnreo)
xhgsgi = Factor("mvsa", [DerivedLevel("znieko", WithinTrial(xyes, [ush, roxpg, rpnreo])), DerivedLevel("oyeh", WithinTrial(cfbw, [ush, roxpg, rpnreo])),DerivedLevel("fhn", WithinTrial(vod, [ush, roxpg, rpnreo]))])
### EXPERIMENT
design=[ush,roxpg,rpnreo,xhgsgi]
crossing=[xhgsgi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END