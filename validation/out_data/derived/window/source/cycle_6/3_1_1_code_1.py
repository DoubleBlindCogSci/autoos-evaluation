from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ago = Factor("ago", ["bbbn","dlucvg","xjya","lgu","ezfgig","fhtx","zhcm"])
def pjj(ago):
     return "bbbn" == ago[0] and not ago[-1] == "bbbn"
def faa(ago):
     return not "bbbn" == ago[0] and  "fhtx" == ago[-1]
def otc(ago):
     return (not ago[0] == "bbbn") and (not ago[-1] == "fhtx")
leofyc = Factor("fsgf", [DerivedLevel("pjd", Window(pjj, [ago],2,1)), DerivedLevel("hjqc", Window(faa, [ago],2,1)),DerivedLevel("kqaxgo", Window(otc, [ago],2,1))])
### EXPERIMENT
design=[ago,leofyc]
crossing=[leofyc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END