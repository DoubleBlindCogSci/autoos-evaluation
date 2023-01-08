from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
sjige = Factor("sjige", ["bjq", "ohgb"])
pjrglr = Factor("pjrglr", ["nxqcue", "sdaqf"])
uos = Factor("uos", ["avwlf", "qfvz"])
ojj = Factor("ojj", ["zawnq", "ltqf"])
kwy = Factor("kwy", ["xdcz", "oxe"])
xyrff = Factor("xyrff", ["yaaqs", "hojas"])

### EXPERIMENT
design=[sjige,pjrglr,uos,ojj,kwy,xyrff]
crossing=[[sjige,pjrglr,uos],[ojj],[kwy,xyrff],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_4"))
### END