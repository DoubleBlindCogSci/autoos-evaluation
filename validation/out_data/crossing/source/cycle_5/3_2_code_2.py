from sweetpea import *
import os
_dir=os.path.dirname(__file__)
nhsc = Factor("nhsc", ["hbvvrp", "ioeya"])
hfxlmo = Factor("hfxlmo", ["wmgn", "poq"])
mwp = Factor("mwp", ["yziwti", "rns"])
tch = Factor("tch", ["whev", "fnfqa"])
zqb = Factor("zqb", ["arwngo", "lif"])
xtk = Factor("xtk", ["gyf", "cooh"])
pyvkfe = Factor("pyvkfe", ["upuuq", "osle"])
kfks = Factor("kfks", ["dnfel", "zslzc"])
constraints = []
crossing = [[nhsc, hfxlmo, mwp], [tch, zqb, xtk], [pyvkfe, kfks]]


design=[nhsc,hfxlmo,mwp,tch,zqb,xtk,pyvkfe,kfks]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2"))

### END