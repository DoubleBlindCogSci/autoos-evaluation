from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dqmt= Factor("dqmt", ["bybuns","yhy","krc","oovtyl","guq","ctls","plc","wcy"])
rqr= Factor("rqr", ["bybuns","yhy","krc","oovtyl","guq","ctls","plc","wcy"])
mxu= Factor("mxu", ["bybuns","yhy","krc","oovtyl","guq","ctls","plc","wcy"])
def is_gtv_trma(rqr, dqmt):
    return rqr[0] == dqmt[-2]
def is_gtv_zvclql(rqr, dqmt, mxu):
    return rqr[0] != dqmt[-2] and mxu[0] == dqmt[-1]
def is_gtv_wpip(rqr, dqmt, mxu):
    return not (is_gtv_trma(rqr, dqmt) or is_gtv_zvclql(rqr, dqmt, mxu))
gtv= Factor("gtv", [DerivedLevel("trma", Window(is_gtv_trma, [rqr, dqmt], 4, 1)), DerivedLevel("zvclql", Window(is_gtv_zvclql, [rqr, dqmt, mxu], 4, 1)), DerivedLevel("wpip", Window(is_gtv_wpip, [rqr, dqmt, mxu], 4, 1))])

design=[dqmt,rqr,mxu,gtv]
crossing=[gtv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END
