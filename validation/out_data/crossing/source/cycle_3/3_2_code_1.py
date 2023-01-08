from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vxx = Factor("vxx", ["ipqlh", "czkm"])
wvrkd = Factor("wvrkd", ["jwa", "thffyc"])
gyugef = Factor("gyugef", ["cmsnpp", "kwqt"])
hela = Factor("hela", ["qkako", "uqlb"])
revmdb = Factor("revmdb", ["zcnlwb", "lfc"])
zrw = Factor("zrw", ["mhvbfw", "irhrq"])
ekgxsj = Factor("ekgxsj", ["ckhdof", "qmypg"])
cgjwi = Factor("cgjwi", ["lbuo", "vwqj"])
ail = Factor("ail", ["zfb", "tdbehl"])
sfqc = Factor("sfqc", ["ljxwr", "pbxs"])
nevz = Factor("nevz", ["ivad", "zqkn"])

### EXPERIMENT
design=[vxx,wvrkd,gyugef,hela,revmdb,zrw,ekgxsj,cgjwi,ail,sfqc,nevz]
crossing=[[vxx,wvrkd,gyugef,hela],[revmdb,zrw,ekgxsj,cgjwi],[ail,sfqc,nevz],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2"))
### END