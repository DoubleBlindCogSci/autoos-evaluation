from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mfkaxd = Factor("mfkaxd", ["bzoi","gfuv","uxog","icyubf","hahmv","uwon","pqrz"])
def is_pebbqo_mrgo(mfkaxd):
    return mfkaxd == "bzoi"
def is_pebbqo_xbs(mfkaxd):
    return mfkaxd == "gfuv"
def is_pebbqo_kndaqf(mfkaxd):
    return not (is_pebbqo_mrgo(mfkaxd) or is_pebbqo_xbs(mfkaxd))
pebbqo = Factor("pebbqo", [DerivedLevel("mrgo", WithinTrial(is_pebbqo_mrgo, [mfkaxd])), DerivedLevel("xbs", WithinTrial(is_pebbqo_xbs, [mfkaxd])), DerivedLevel("kndaqf", WithinTrial(is_pebbqo_kndaqf, [mfkaxd]))])

design=[mfkaxd,pebbqo]
crossing=[pebbqo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END