from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pbbncw= Factor("pbbncw", ["nmxpb","itt","ijv","imuzj","tjfdht","eumhf","mravi"])

def is_jwgl_yzl(pbbncw):
    return pbbncw == "nmxpb"
def is_jwgl_qvxiuo(pbbncw):
    return pbbncw == "mravi"
def is_jwgl_mqi(pbbncw):
    return not (is_jwgl_yzl(pbbncw) or is_jwgl_qvxiuo(pbbncw))
jwgl= Factor("jwgl", [DerivedLevel("yzl", WithinTrial(is_jwgl_yzl, [pbbncw])), DerivedLevel("qvxiuo", WithinTrial(is_jwgl_qvxiuo, [pbbncw])), DerivedLevel("mqi", WithinTrial(is_jwgl_mqi, [pbbncw]))])


design=[pbbncw,jwgl]
crossing=[jwgl]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END
