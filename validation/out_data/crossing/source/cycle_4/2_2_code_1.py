from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hqvr = Factor("hqvr", ["tzen", "coy"])
ujagxt = Factor("ujagxt", ["cgog", "ufzdj"])
mbg = Factor("mbg", ["dbgrs", "hadedm"])
gokba = Factor("gokba", ["ehywrw", "beod"])
hre = Factor("hre", ["ewm", "buahn"])
ecwe = Factor("ecwe", ["opgm", "cti"])

### EXPERIMENT
design=[hqvr,ujagxt,mbg,gokba,hre,ecwe]
crossing=[[hqvr,ujagxt],[mbg,gokba,hre,ecwe],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2"))
### END