from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wee = Factor("wee", ["zjoqhd", "krk"])
dgz = Factor("dgz", ["wxbpos", "lcne"])
ouvm = Factor("ouvm", ["buliuk", "gsli"])
deh = Factor("deh", ["sfg", "ldnpt"])
neqfot = Factor("neqfot", ["hnppn", "dfgbv"])
aog = Factor("aog", ["cshz", "yovat"])
qfmfp = Factor("qfmfp", ["msqhgh", "ymgtp"])
klty = Factor("klty", ["yglpr", "ncamk"])
keuta = Factor("keuta", ["fxgp", "skmu"])
bejhda = Factor("bejhda", ["hhqy", "nzxijm"])
whd = Factor("whd", ["tertin", "hjt"])
jchi = Factor("jchi", ["zxqfuw", "flxay"])
wvuhk = Factor("wvuhk", ["dtsl", "zqn"])

### EXPERIMENT
design=[wee,dgz,ouvm,deh,neqfot,aog,qfmfp,klty,keuta,bejhda,whd,jchi,wvuhk]
crossing=[[wee,dgz,ouvm,deh],[neqfot,aog,qfmfp,klty],[keuta],[bejhda],[whd,jchi,wvuhk],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1"))
### END