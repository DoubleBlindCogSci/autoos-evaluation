from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dqmt = Factor("dqmt", ["bybuns","yhy","krc","oovtyl","guq","ctls","plc","wcy"])
rqr = Factor("rqr", ["bybuns","yhy","krc","oovtyl","guq","ctls","plc","wcy"])
mxu = Factor("mxu", ["bybuns","yhy","krc","oovtyl","guq","ctls","plc","wcy"])
def xfoc(dqmt, rqr, mxu):
     return rqr[-2] == dqmt[-3]
def xmc(dqmt, rqr, mxu):
     return rqr[-2] != dqmt[-3] and mxu[-3] == dqmt[-2]
def onvo(dqmt, rqr, mxu):
     return (dqmt[-3] != rqr[-2]) and (dqmt[-2] != mxu[-3])
yngml = DerivedLevel("trma", Window(xfoc, [dqmt, rqr, mxu],4,1))
diseud = DerivedLevel("zvclql", Window(xmc, [dqmt, rqr, mxu],4,1))
xpciw = DerivedLevel("wpip", Window(onvo, [dqmt, rqr, mxu],4,1))
avy = Factor("gtv", [yngml, diseud, xpciw])

### EXPERIMENT
design=[dqmt,rqr,mxu,avy]
crossing=[avy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END