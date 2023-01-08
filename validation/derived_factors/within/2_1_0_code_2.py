from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tvzg = Factor("tvzg", ["frf","qjrlhh","hpu","xdpkxt","outoi","yhsj"])
def is_igpbb_aijl(tvzg):
    return tvzg == "hpu" and tvzg == "outoi"
def is_igpbb_ccs(tvzg):
    return not is_igpbb_aijl(tvzg)
igpbb = Factor("igpbb", [DerivedLevel("aijl", WithinTrial(is_igpbb_aijl, [tvzg])), DerivedLevel("ccs", WithinTrial(is_igpbb_ccs, [tvzg]))])

design=[tvzg,igpbb]
crossing=[igpbb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END