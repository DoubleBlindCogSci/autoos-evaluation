from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zgreiu = Factor("zgreiu", ["tnhg","ychk","lcb","nuk","gmao"])
def is_eagfi_elbbb(zgreiu):
    return zgreiu == "ychk"
def is_eagfi_pcpop(zgreiu):
    return not is_eagfi_elbbb(zgreiu)
eagfi = Factor("eagfi", [DerivedLevel("elbbb", WithinTrial(is_eagfi_elbbb, [zgreiu])), DerivedLevel("pcpop", WithinTrial(is_eagfi_pcpop, [zgreiu]))])

design=[zgreiu,eagfi]
crossing=[eagfi]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END