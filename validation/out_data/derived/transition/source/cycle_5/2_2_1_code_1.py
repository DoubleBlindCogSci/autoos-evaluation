from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rnmqww = Factor("rnmqww", ["jas","drhz","jglx","deji","jqshvt","zktr","mhm"])
vhln = Factor("vhln", ["adqrok","yha","bij","jeilkw","iamwb"])
def jrh(rnmqww, vhln):
    return rnmqww[0] == "jas" and vhln[-1] != "jeilkw"
def puelhm(rnmqww,vhln):
    return rnmqww[0] != "jas" or vhln[-1] == "jeilkw"
zjjkpw = DerivedLevel("xiarzr", Transition(jrh, [rnmqww, vhln]))
kjzh = DerivedLevel("mmf", Transition(puelhm, [rnmqww, vhln]))
phf = Factor("qgpn", [zjjkpw, kjzh])

### EXPERIMENT
design=[rnmqww,vhln,phf]
crossing=[phf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END