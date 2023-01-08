from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jwovfi = Factor("jwovfi", ["khjida","bdyfep","ajxqv","wyfy","hhyd","lvff"])
wouq = Factor("wouq", ["hrfrp","yajjc","frwd","ldxil","vpy","ygs","dpvb"])
def pjpf(jwovfi, wouq):
     return "lvff" == jwovfi[-2] and not wouq[0] == "dpvb"
def nrjrft(jwovfi, wouq):
     return jwovfi[-2] != "lvff" and  wouq[0] == "dpvb"
def uvfzw(jwovfi, wouq):
     return (not jwovfi[-2] == "lvff") and (not nrjrft(jwovfi, wouq))
henb = DerivedLevel("pfim", Window(pjpf, [jwovfi, wouq],3,1))
fizxid = DerivedLevel("suvb", Window(nrjrft, [jwovfi, wouq],3,1))
pvylvp = DerivedLevel("ekb", Window(uvfzw, [jwovfi, wouq],3,1))
icluy = Factor("rvvq", [henb, fizxid, pvylvp])

### EXPERIMENT
design=[jwovfi,wouq,icluy]
crossing=[icluy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END