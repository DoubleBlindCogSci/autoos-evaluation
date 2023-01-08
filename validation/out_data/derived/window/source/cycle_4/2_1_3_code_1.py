from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yctm = Factor("yctm", ["wuvy","gdjl","itmmu","ucfi","vhew","akgbzo","pav"])
def pbke(yctm):
    return yctm[-1] != "vhew" and yctm[0] == "akgbzo"
def exwkc(yctm):
    return yctm[-1] == "vhew" or not (yctm[0] == "akgbzo")
ynu = DerivedLevel("uqzei", Window(pbke, [yctm],2,1))
kdela = DerivedLevel("zlku", Window(exwkc, [yctm],2,1))
cgxrvp = Factor("rvdi", [ynu, kdela])

### EXPERIMENT
design=[yctm,cgxrvp]
crossing=[cgxrvp]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END