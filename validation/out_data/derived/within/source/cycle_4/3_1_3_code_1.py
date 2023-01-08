from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mfkaxd = Factor("mfkaxd", ["bzoi","gfuv","uxog","icyubf","hahmv","uwon","pqrz"])
def tfbjvk(mfkaxd):
     return "bzoi" == mfkaxd
def oigiql(mfkaxd):
     return mfkaxd == "gfuv"
def xzojg(mfkaxd):
     return (mfkaxd != "bzoi") and (mfkaxd != "gfuv")
simnd = DerivedLevel("mrgo", WithinTrial(tfbjvk, [mfkaxd]))
uoqu = DerivedLevel("xbs", WithinTrial(oigiql, [mfkaxd]))
tbtdl = DerivedLevel("kndaqf", WithinTrial(xzojg, [mfkaxd]))
acshw = Factor("pebbqo", [simnd, uoqu, tbtdl])

### EXPERIMENT
design=[mfkaxd,acshw]
crossing=[acshw]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END