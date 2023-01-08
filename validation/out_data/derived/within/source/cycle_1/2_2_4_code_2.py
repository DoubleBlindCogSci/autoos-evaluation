from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yzz= Factor("yzz", ["pvnjh","lkily","jvreq","bhza","yxte","lymh","ujybz"])
ayjqd= Factor("ayjqd", ["pvnjh","lkily","jvreq","bhza","yxte","lymh","ujybz"])
ulgge= Factor("ulgge", ["pvnjh","lkily","jvreq","bhza","yxte","lymh","ujybz"])
def is_ewkf_hxdn(yzz, ayjqd, ulgge):
    return yzz != ulgge
def is_ewkf_bzwmbv(yzz, ayjqd, ulgge):
    return not is_ewkf_hxdn(yzz, ayjqd, ulgge)
ewkf= Factor("ewkf", [DerivedLevel("hxdn", WithinTrial(is_ewkf_hxdn, [yzz, ayjqd, ulgge])), DerivedLevel("bzwmbv", WithinTrial(is_ewkf_bzwmbv, [yzz, ayjqd, ulgge]))])

design=[yzz,ayjqd,ulgge,ewkf]
crossing=[ewkf]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END
