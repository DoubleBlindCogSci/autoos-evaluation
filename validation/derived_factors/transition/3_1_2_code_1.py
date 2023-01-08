from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
gaxb = Factor("gaxb", ["vivjme","krlvjt","morfp","ospaky","cili","vpg","olw"])
def veae(gaxb):
     return gaxb[0] == "olw" and gaxb[-1] != "cili"
def etcf(gaxb):
     return (not "olw" != gaxb[0]) and  "cili" == gaxb[-1]
def safbnz(gaxb):
     return (not gaxb[0] == "olw") and (gaxb[-1] != "cili")
azbsj = Factor("pwzb", [DerivedLevel("ihbfvl", Transition(veae, [gaxb])), DerivedLevel("xtkg", Transition(etcf, [gaxb])),DerivedLevel("ffqxlr", Transition(safbnz, [gaxb]))])
### EXPERIMENT
design=[gaxb,azbsj]
crossing=[azbsj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END