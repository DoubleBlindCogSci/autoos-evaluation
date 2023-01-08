from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tjqjy= Factor("tjqjy", ["ezrg","lxhb","spwqj","nigrt","hhzjy","eocn"])
tclqkw= Factor("tclqkw", ["scals","ndjw","rxa","hig","qwlv","svyx","ogwjy"])
def is_otzpw_dkytkh(tjqjy, tclqkw):
    return tjqjy[0] == "lxhb" and tclqkw[-2] != "scals"
def is_otzpw_vfz(tjqjy, tclqkw):
    return tjqjy[0] != "lxhb" and tclqkw[-2] == "scals"
def is_otzpw_hizcf(tjqjy, tclqkw):
    return not (is_otzpw_dkytkh(tjqjy, tclqkw) or is_otzpw_vfz(tjqjy, tclqkw))
otzpw= Factor("otzpw", [DerivedLevel("dkytkh", Window(is_otzpw_dkytkh, [tjqjy, tclqkw], 3, 1)), DerivedLevel("vfz", Window(is_otzpw_vfz, [tjqjy, tclqkw], 3, 1)), DerivedLevel("hizcf", Window(is_otzpw_hizcf, [tjqjy, tclqkw], 3, 1))])

design=[tjqjy,tclqkw,otzpw]
crossing=[otzpw]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END
