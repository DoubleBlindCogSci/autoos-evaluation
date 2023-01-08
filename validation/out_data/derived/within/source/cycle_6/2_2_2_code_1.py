from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
fcq = Factor("fcq", ["dkah","igk","nreq","ryc","szko"])
czust = Factor("czust", ["yddp","rdu","eiolg","ekwa","rkq"])
def host(fcq, czust):
    return fcq != "igk" or czust == "rdu"
def rqed(fcq,czust):
    return not (fcq != "igk") and not (czust == "rdu")
ychtqz = Factor("dvzlc", [DerivedLevel("rnqt", WithinTrial(host, [fcq, czust])), DerivedLevel("cijg", WithinTrial(rqed, [fcq, czust]))])
### EXPERIMENT
design=[fcq,czust,ychtqz]
crossing=[ychtqz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END