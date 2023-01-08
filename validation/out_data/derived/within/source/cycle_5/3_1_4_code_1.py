from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
fzwmlt = Factor("fzwmlt", ["kau","dupei","ynipuu","yhumn","nxg","hqv","snbxmi"])
def int(fzwmlt):
     return "snbxmi" == fzwmlt
def ezzia(fzwmlt):
     return fzwmlt == "kau"
def snwab(fzwmlt):
     return (not int(fzwmlt)) and (not fzwmlt == "kau")
pjbwn = Factor("owvic", [DerivedLevel("ultirx", WithinTrial(int, [fzwmlt])), DerivedLevel("fcz", WithinTrial(ezzia, [fzwmlt])),DerivedLevel("vtncwy", WithinTrial(snwab, [fzwmlt]))])
### EXPERIMENT
design=[fzwmlt,pjbwn]
crossing=[pjbwn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END