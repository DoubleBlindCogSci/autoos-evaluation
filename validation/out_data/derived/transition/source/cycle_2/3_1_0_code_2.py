from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nzeyhy= Factor("nzeyhy", ["qyl","vnxtdl","tjy","mvbc","lvo","gbxcg"])
def is_umf_olado(nzeyhy):
    return nzeyhy[0] == "gbxcg" and nzeyhy[-1] != "lvo"
def is_umf_dxkmeo(nzeyhy):
    return nzeyhy[0] != "gbxcg" and nzeyhy[-1] == "lvo"
def is_umf_yedcyl(nzeyhy):
    return nzeyhy[0] != "gbxcg" and nzeyhy[-1] != "lvo"
umf= Factor("umf", [DerivedLevel("olado", Transition(is_umf_olado, [nzeyhy])), DerivedLevel("dxkmeo", Transition(is_umf_dxkmeo, [nzeyhy])), DerivedLevel("yedcyl", Transition(is_umf_yedcyl, [nzeyhy]))])

design=[nzeyhy,umf]
crossing=[umf]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END
