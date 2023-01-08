from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yzz = Factor("yzz", ["pvnjh","lkily","jvreq","bhza","yxte","lymh","ujybz"])
ayjqd = Factor("ayjqd", ["pvnjh","lkily","jvreq","bhza","yxte","lymh","ujybz"])
ulgge = Factor("ulgge", ["pvnjh","lkily","jvreq","bhza","yxte","lymh","ujybz"])
def vpki(yzz, ulgge, ayjqd):
    return yzz != ulgge
def ciiab(yzz, ulgge, ayjqd):
    return yzz == ulgge
jkzs = Factor("ewkf", [DerivedLevel("hxdn", WithinTrial(vpki, [yzz, ayjqd, ulgge])), DerivedLevel("bzwmbv", WithinTrial(ciiab, [yzz, ayjqd, ulgge]))])
### EXPERIMENT
design=[yzz,ayjqd,ulgge,jkzs]
crossing=[jkzs]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END