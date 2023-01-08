from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
letkr = Factor("letkr", ["zil","ukuxyy","xkmrbl","idyql","izyc"])
fsre = Factor("fsre", ["rlsi","baqb","argp","gkfi","vscoiz"])
def grmrkm(letkr, fsre):
    return letkr[0] != "xkmrbl" or fsre[-1] != "argp"
def iixgm(letkr,fsre):
    return not grmrkm(letkr, fsre)
jkqxs = DerivedLevel("zrdges", Window(grmrkm, [letkr, fsre],2,1))
gyjna = DerivedLevel("tnibr", Window(iixgm, [letkr, fsre],2,1))
zzrje = Factor("wzau", [jkqxs, gyjna])

### EXPERIMENT
design=[letkr,fsre,zzrje]
crossing=[zzrje]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END