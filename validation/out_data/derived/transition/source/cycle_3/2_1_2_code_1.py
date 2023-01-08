from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
oeiu = Factor("oeiu", ["mjbpsw","mbe","ujudp","hwx","xgi","exofud"])
def arsov(oeiu):
    return oeiu[0] != "ujudp" and oeiu[-1] == "mbe"
def owl(oeiu):
    return not (oeiu[0] != "ujudp") or not (oeiu[0] == "mbe")
krs = DerivedLevel("sopit", Transition(arsov, [oeiu]))
albvlg = DerivedLevel("alor", Transition(owl, [oeiu]))
szgdzb = Factor("qfre", [krs, albvlg])

### EXPERIMENT
design=[oeiu,szgdzb]
crossing=[szgdzb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END