from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
wtmrd = Factor("wtmrd", ["ubkei", "emek"])
jqvsip = Factor("jqvsip", ["hziva", "tklmk"])
pvzxug = Factor("pvzxug", ["ubkei", "emek"])
hrycmu = Factor("hrycmu", ["hziva", "tklmk"])
bpf = Factor("bpf", ["wimnk", "vdearw"])
design=[wtmrd,jqvsip,pvzxug,hrycmu,bpf]
constraints=[]
crossing=[wtmrd,bpf]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/5_0_0"))
