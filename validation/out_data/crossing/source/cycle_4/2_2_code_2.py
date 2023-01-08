from sweetpea import *
import os
_dir=os.path.dirname(__file__)
hqvr = Factor("hqvr", ["tzen", "coy"])
ujagxt = Factor("ujagxt", ["cgog", "ufzdj"])
mbg = Factor("mbg", ["dbgrs", "hadedm"])
gokba = Factor("gokba", ["ehywrw", "beod"])
hre = Factor("hre", ["ewm", "buahn"])
ecwe = Factor("ecwe", ["opgm", "cti"])
constraints = []
crossing = [[hqvr, ujagxt], [mbg, gokba, hre, ecwe]]


design=[hqvr,ujagxt,mbg,gokba,hre,ecwe]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2"))

### END