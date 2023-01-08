from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lnayb = Factor("lnayb", ["mebsfp","dsyo","npx","yak","zdwh"])
jplz = Factor("jplz", ["mebsfp","dsyo","npx","yak","zdwh"])
tln = Factor("tln", ["mebsfp","dsyo","npx","yak","zdwh"])
def is_fxgl_gmmc(lnayb, tln, jplz):
    return lnayb == tln
def is_fxgl_lxfgme(lnayb, tln, jplz):
    return not is_fxgl_gmmc(lnayb, tln, jplz)
fxgl= Factor("fxgl", [DerivedLevel("gmmc", WithinTrial(is_fxgl_gmmc, [lnayb, tln, jplz])), DerivedLevel("lxfgme", WithinTrial(is_fxgl_lxfgme, [lnayb, tln, jplz]))])

design=[lnayb,jplz,tln,fxgl]
crossing=[fxgl]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END
