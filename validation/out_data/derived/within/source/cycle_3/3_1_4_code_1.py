from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
suhen = Factor("suhen", ["krpr","ufomf","nypxj","ezhsn","cjidu","jkpx","mhdkzw","bzj"])
def kammmt(suhen):
     return "ezhsn" == suhen
def yvo(suhen):
     return suhen == "cjidu"
def eydyd(suhen):
     return (not suhen == "ezhsn") and (suhen != "cjidu")
zfz = Factor("vuff", [DerivedLevel("pfj", WithinTrial(kammmt, [suhen])), DerivedLevel("wdgbc", WithinTrial(yvo, [suhen])),DerivedLevel("vnmvgi", WithinTrial(eydyd, [suhen]))])
### EXPERIMENT
design=[suhen,zfz]
crossing=[zfz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END