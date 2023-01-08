from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
lnayb = Factor("lnayb", ["mebsfp","dsyo","npx","yak","zdwh"])
jplz = Factor("jplz", ["mebsfp","dsyo","npx","yak","zdwh"])
tln = Factor("tln", ["mebsfp","dsyo","npx","yak","zdwh"])
def glp(lnayb, tln, jplz):
    return lnayb == tln
def pzogxw(lnayb, tln, jplz):
    return not glp(lnayb, tln, jplz)
wsxs = Factor("fxgl", [DerivedLevel("gmmc", WithinTrial(glp, [lnayb, jplz, tln])), DerivedLevel("lxfgme", WithinTrial(pzogxw, [lnayb, jplz, tln]))])
### EXPERIMENT
design=[lnayb,jplz,tln,wsxs]
crossing=[wsxs]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END