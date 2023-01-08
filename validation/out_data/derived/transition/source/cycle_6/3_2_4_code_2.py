from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wnjfo = Factor("wnjfo", ["teq","sjk","cxac","coz","eoovdf","scwmix","wnlwwg","kny"])
ydczl = Factor("ydczl", ["teq","sjk","cxac","coz","eoovdf","scwmix","wnlwwg","kny"])
ezw = Factor("ezw", ["teq","sjk","cxac","coz","eoovdf","scwmix","wnlwwg","kny"])
def is_gaovt_wpyds(ydczl, wnjfo, ezw):
    return ydczl[-1] == wnjfo[0] and wnjfo[-1] != ezw[0]
def is_gaovt_hjm(ydczl, wnjfo, ezw):
    return ydczl[-1] != wnjfo[0] and wnjfo[-1] == ezw[0]
def is_gaovt_iiyv(ydczl, wnjfo, ezw):
    return not (is_gaovt_wpyds(ydczl, wnjfo, ezw) or is_gaovt_hjm(ydczl, wnjfo, ezw))
gaovt = Factor("gaovt", [DerivedLevel("wpyds", Transition(is_gaovt_wpyds, [ydczl, wnjfo, ezw])), DerivedLevel("hjm", Transition(is_gaovt_hjm, [ydczl, wnjfo, ezw])), DerivedLevel("iiyv", Transition(is_gaovt_iiyv, [ydczl, wnjfo, ezw]))])

design=[wnjfo,ydczl,ezw,gaovt]
crossing=[gaovt]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END