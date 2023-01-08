from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hwcri = Factor("hwcri", ["hipky","uwsc","cpkgs","ghvkz","kwxymw","vpz","xgg"])
def puj(hwcri):
     return hwcri[0] == "kwxymw" and not hwcri[-1] == "xgg"
def vtnkc(hwcri):
     return (hwcri[0] != "kwxymw") and  "xgg" == hwcri[-1]
def oohktt(hwcri):
     return (hwcri[0] != "kwxymw") and (hwcri[-1] != "xgg")
xvbtl = Factor("uwmv", [DerivedLevel("duaqe", Transition(puj, [hwcri])), DerivedLevel("axiti", Transition(vtnkc, [hwcri])),DerivedLevel("cco", Transition(oohktt, [hwcri]))])
### EXPERIMENT
design=[hwcri,xvbtl]
crossing=[xvbtl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END