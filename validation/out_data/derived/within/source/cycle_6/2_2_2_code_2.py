from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fcq = Factor("fcq", ["dkah","igk","nreq","ryc","szko"])
czust = Factor("czust", ["yddp","rdu","eiolg","ekwa","rkq"])
def is_dvzlc_rnqt(fcq, czust):
    return fcq != "igk" or czust == "rdu"
def is_dvzlc_cijg(fcq, czust):
    return not is_dvzlc_rnqt(fcq, czust)
dvzlc = Factor("dvzlc", [DerivedLevel("rnqt", WithinTrial(is_dvzlc_rnqt, [fcq, czust])), DerivedLevel("cijg", WithinTrial(is_dvzlc_cijg, [fcq, czust]))])

design=[fcq,czust,dvzlc]
crossing=[dvzlc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END