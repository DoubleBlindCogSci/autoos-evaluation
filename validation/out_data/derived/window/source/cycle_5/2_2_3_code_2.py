from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
letkr = Factor("letkr", ["zil","ukuxyy","xkmrbl","idyql","izyc"])
fsre = Factor("fsre", ["rlsi","baqb","argp","gkfi","vscoiz"])
def is_wzau_zrdges(letkr, fsre):
    return letkr[-1] != "xkmrbl" or fsre[0] != "argp"
def is_wzau_tnibr(letkr, fsre):
    return not is_wzau_zrdges(letkr, fsre)
wzau = Factor("wzau", [DerivedLevel("zrdges", Window(is_wzau_zrdges, [letkr, fsre], 2, 1)), DerivedLevel("tnibr", Window(is_wzau_tnibr, [letkr, fsre], 2, 1))])

design=[letkr,fsre,wzau]
crossing=[wzau]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END