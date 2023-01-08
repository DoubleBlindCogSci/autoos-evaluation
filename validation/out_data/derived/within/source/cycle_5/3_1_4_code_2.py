from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fzwmlt = Factor("fzwmlt", ["kau","dupei","ynipuu","yhumn","nxg","hqv","snbxmi"])
def is_owvic_ultirx(fzwmlt):
    return fzwmlt == "snbxmi"
def is_owvic_fcz(fzwmlt):
    return fzwmlt == "kau"
def is_owvic_vtncwy(fzwmlt):
    return not (is_owvic_ultirx(fzwmlt) or is_owvic_fcz(fzwmlt))
owvic = Factor("owvic", [DerivedLevel("ultirx", WithinTrial(is_owvic_ultirx, [fzwmlt])), DerivedLevel("fcz", WithinTrial(is_owvic_fcz, [fzwmlt])), DerivedLevel("vtncwy", WithinTrial(is_owvic_vtncwy, [fzwmlt]))])

design=[fzwmlt,owvic]
crossing=[owvic]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END