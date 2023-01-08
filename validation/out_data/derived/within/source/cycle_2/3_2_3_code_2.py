from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ohixrc= Factor("ohixrc", ["vmna","bszyfq","prscsd","ecy","jiku","yfnk","njjxli"])
dyt= Factor("dyt", ["vmna","bszyfq","prscsd","ecy","jiku","yfnk","njjxli"])
pef= Factor("pef", ["vmna","bszyfq","prscsd","ecy","jiku","yfnk","njjxli"])
def is_zfoyvj_lqk(ohixrc, dyt, pef):
    return ohixrc == pef
def is_zfoyvj_skpe(ohixrc, dyt, pef):
    return ohixrc == dyt
def is_zfoyvj_yudp(ohixrc, dyt, pef):
    return ohixrc != pef and ohixrc != dyt
zfoyvj= Factor("zfoyvj", [DerivedLevel("lqk", WithinTrial(is_zfoyvj_lqk, [ohixrc, dyt, pef])), DerivedLevel("skpe", WithinTrial(is_zfoyvj_skpe, [ohixrc, dyt, pef])), DerivedLevel("yudp", WithinTrial(is_zfoyvj_yudp, [ohixrc, dyt, pef]))])

design=[ohixrc,dyt,pef, zfoyvj]
crossing=[zfoyvj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END
