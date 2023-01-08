from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tyi = Factor("tyi", ["oiz","gqm","tdh","jjlisq","etae"])
def fmmk(tyi):
    return tyi[0] == "gqm" or tyi[-3] != "tdh"
def cbkgab(tyi):
    return tyi[0] != "gqm" and not (tyi[-3] != "tdh")
kdaiwk = Factor("qjd", [DerivedLevel("ydytym", Window(fmmk, [tyi],4,1)), DerivedLevel("sehsfj", Window(cbkgab, [tyi],4,1))])
### EXPERIMENT
design=[tyi,kdaiwk]
crossing=[kdaiwk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END