from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nhsc = Factor("nhsc", ["hbvvrp", "ioeya"])
hfxlmo = Factor("hfxlmo", ["wmgn", "poq"])
mwp = Factor("mwp", ["yziwti", "rns"])
tch = Factor("tch", ["whev", "fnfqa"])
zqb = Factor("zqb", ["arwngo", "lif"])
xtk = Factor("xtk", ["gyf", "cooh"])
pyvkfe = Factor("pyvkfe", ["upuuq", "osle"])
kfks = Factor("kfks", ["dnfel", "zslzc"])

### EXPERIMENT
design=[nhsc,hfxlmo,mwp,tch,zqb,xtk,pyvkfe,kfks]
crossing=[[nhsc,hfxlmo,mwp],[tch,zqb,xtk],[pyvkfe,kfks],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2"))
### END