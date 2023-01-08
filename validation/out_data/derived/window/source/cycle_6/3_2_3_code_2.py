from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jwovfi = Factor("jwovfi", ["khjida","bdyfep","ajxqv","wyfy","hhyd","lvff"])
wouq = Factor("wouq", ["hrfrp","yajjc","frwd","ldxil","vpy","ygs","dpvb"])
def is_rvvq_pfim(jwovfi, wouq):
    return jwovfi[-2] == "lvff" and wouq[0] != "dpvb"
def is_rvvq_suvb(jwovfi, wouq):
    return jwovfi[-2] != "lvff" and wouq[0] == "dpvb"
def is_rvvq_ekb(jwovfi, wouq):
    return not (is_rvvq_pfim(jwovfi, wouq) or is_rvvq_suvb(jwovfi, wouq))
rvvq = Factor("rvvq", [DerivedLevel("pfim", Window(is_rvvq_pfim, [jwovfi, wouq], 3, 1)), DerivedLevel("suvb", Window(is_rvvq_suvb, [jwovfi, wouq], 3, 1)), DerivedLevel("ekb", Window(is_rvvq_ekb, [jwovfi, wouq], 3, 1))])

design=[jwovfi,wouq,rvvq]
crossing=[rvvq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END