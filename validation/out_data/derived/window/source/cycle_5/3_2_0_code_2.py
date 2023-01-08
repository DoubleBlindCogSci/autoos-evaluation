from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vusvwj = Factor("vusvwj", ["vbhsbt","reonc","doe","uxo","dpsf","gjsat","yac","nqplwf"])
rqpzlq = Factor("rqpzlq", ["evitfv","xfwdfh","xzjayj","vcmxu","xpsc","rkv","xfmw"])
def is_hkfpd_gqrznp(vusvwj, rqpzlq):
    return vusvwj[-2] == "doe" and rqpzlq[-1] != "xfwdfh"
def is_hkfpd_fha(vusvwj, rqpzlq):
    return vusvwj[-2] != "doe" and rqpzlq[-1] == "xfwdfh"
def is_hkfpd_jkz(vusvwj, rqpzlq):
    return not (is_hkfpd_gqrznp(vusvwj, rqpzlq) or is_hkfpd_fha(vusvwj, rqpzlq))
hkfpd = Factor("hkfpd", [DerivedLevel("gqrznp", Window(is_hkfpd_gqrznp, [vusvwj, rqpzlq], 3, 1)), DerivedLevel("fha", Window(is_hkfpd_fha, [vusvwj, rqpzlq], 3, 1)), DerivedLevel("jkz", Window(is_hkfpd_jkz, [vusvwj, rqpzlq], 3, 1))])

design=[vusvwj,rqpzlq,hkfpd]
crossing=[hkfpd]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END