from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vusvwj = Factor("vusvwj", ["vbhsbt","reonc","doe","uxo","dpsf","gjsat","yac","nqplwf"])
rqpzlq = Factor("rqpzlq", ["evitfv","xfwdfh","xzjayj","vcmxu","xpsc","rkv","xfmw"])
def hyar(vusvwj, rqpzlq):
     return vusvwj[-2] == "doe" and rqpzlq[-1] != "xfwdfh"
def aduv(vusvwj, rqpzlq):
     return vusvwj[-2] != "doe" and  rqpzlq[-1] == "xfwdfh"
def auy(vusvwj, rqpzlq):
     return (not hyar(vusvwj, rqpzlq)) and (rqpzlq[-1] != "xfwdfh")
hxb = DerivedLevel("gqrznp", Window(hyar, [vusvwj, rqpzlq],3,1))
eajlk = DerivedLevel("fha", Window(aduv, [vusvwj, rqpzlq],3,1))
rlg = DerivedLevel("jkz", Window(auy, [vusvwj, rqpzlq],3,1))
wruaj = Factor("hkfpd", [hxb, eajlk, rlg])

### EXPERIMENT
design=[vusvwj,rqpzlq,wruaj]
crossing=[wruaj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END