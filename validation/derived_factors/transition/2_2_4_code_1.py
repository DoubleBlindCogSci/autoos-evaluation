from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
uxje = Factor("uxje", ["hikpm","bgzcrc","zgt","xcjs","jiy","ptmx"])
drz = Factor("drz", ["hikpm","bgzcrc","zgt","xcjs","jiy","ptmx"])
cpvt = Factor("cpvt", ["hikpm","bgzcrc","zgt","xcjs","jiy","ptmx"])
def jirbjm(uxje, drz, cpvt):
    return uxje[0] == drz[-1] and uxje[-1] == cpvt[0]
def giic(uxje, drz, cpvt):
    return not (uxje[0] == drz[-1]) or uxje[-1] != cpvt[0]
hbmke = DerivedLevel("uke", Transition(jirbjm, [uxje, drz, cpvt]))
gehxc = DerivedLevel("dojeo", Transition(giic, [uxje, drz, cpvt]))
azwc = Factor("hft", [hbmke, gehxc])

### EXPERIMENT
design=[uxje,drz,cpvt,azwc]
crossing=[azwc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END