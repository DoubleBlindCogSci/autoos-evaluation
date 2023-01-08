from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
etw = Factor("etw", ["havms","sslbut","ogslo","tpi","kcu","bdxbbr","bwj"])
qkmfhd = Factor("qkmfhd", ["havms","sslbut","ogslo","tpi","kcu","bdxbbr","bwj"])
qcftj = Factor("qcftj", ["havms","sslbut","ogslo","tpi","kcu","bdxbbr","bwj"])
def tmb(etw, qcftj, qkmfhd):
     return qcftj[-1] == etw[0] and etw[-1] != qkmfhd[0]
def jge(etw, qcftj, qkmfhd):
     return qcftj[-1] != etw[0] and qkmfhd[0] == etw[-1]
def ljm(etw, qcftj, qkmfhd):
     return (not tmb(etw, qcftj, qkmfhd)) and (not jge(etw, qcftj, qkmfhd))
ggfx = Factor("uaioe", [DerivedLevel("pozw", Transition(tmb, [etw, qkmfhd, qcftj])), DerivedLevel("wsm", Transition(jge, [etw, qkmfhd, qcftj])),DerivedLevel("azb", Transition(ljm, [etw, qkmfhd, qcftj]))])
### EXPERIMENT
design=[etw,qkmfhd,qcftj,ggfx]
crossing=[ggfx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END