from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
etw = Factor("etw", ["havms","sslbut","ogslo","tpi","kcu","bdxbbr","bwj"])
qkmfhd = Factor("qkmfhd", ["havms","sslbut","ogslo","tpi","kcu","bdxbbr","bwj"])
qcftj = Factor("qcftj", ["havms","sslbut","ogslo","tpi","kcu","bdxbbr","bwj"])
def is_uaioe_pozw(etw, qkmfhd, qcftj):
    return qcftj[-1] == etw[0] and etw[-1] != qkmfhd[0]
def is_uaioe_wsm(etw, qkmfhd, qcftj):
    return qcftj[-1] != etw[0] and qkmfhd[0] == etw[-1]
def is_uaioe_azb(etw, qkmfhd, qcftj):
    return not (is_uaioe_pozw(etw, qkmfhd, qcftj) or is_uaioe_wsm(etw, qkmfhd, qcftj))
uaioe = Factor("uaioe", [DerivedLevel("pozw", Transition(is_uaioe_pozw, [etw, qkmfhd, qcftj])), DerivedLevel("wsm", Transition(is_uaioe_wsm, [etw, qkmfhd, qcftj])), DerivedLevel("azb", Transition(is_uaioe_azb, [etw, qkmfhd, qcftj]))])

design=[etw,qkmfhd,qcftj,uaioe]
crossing=[uaioe]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END