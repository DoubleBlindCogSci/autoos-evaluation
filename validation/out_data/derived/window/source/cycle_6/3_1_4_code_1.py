from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pcqwk = Factor("pcqwk", ["kpqzyd","illtb","eqvg","brs","vrjjde","awal","sqdls"])
def ldqxf(pcqwk):
     return "sqdls" == pcqwk[0] and not pcqwk[-1] == "sqdls"
def qrf(pcqwk):
     return not "sqdls" == pcqwk[0] and  "illtb" == pcqwk[-1]
def ubuiq(pcqwk):
     return (pcqwk[0] != "sqdls") and (pcqwk[-1] != "illtb")
lgtga = DerivedLevel("cysage", Window(ldqxf, [pcqwk],2,1))
inxh = DerivedLevel("ayui", Window(qrf, [pcqwk],2,1))
uxqz = DerivedLevel("tevdko", Window(ubuiq, [pcqwk],2,1))
gacayr = Factor("jnvu", [lgtga, inxh, uxqz])

### EXPERIMENT
design=[pcqwk,gacayr]
crossing=[gacayr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END