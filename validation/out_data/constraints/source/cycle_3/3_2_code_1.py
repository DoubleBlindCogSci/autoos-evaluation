from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jpgvuy = Factor("jpgvuy", ["ctsdub", "lhf"])
gwghub = Factor("gwghub", ["qle", "axlm"])
uzdm = Factor("uzdm", ["rqkm","vieyz", "ruptw"])
jexsp = Factor("jexsp", ["rpc", "kmdgwm"])

### EXPERIMENT
constraints=[Exclude((jpgvuy,"lhf")),ExactlyKInARow(3,(gwghub,"axlm")),AtMostKInARow(2,(uzdm,"ruptw"))]
design=[jpgvuy,gwghub,uzdm,jexsp]
crossing=[jexsp]
### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2"))
### END