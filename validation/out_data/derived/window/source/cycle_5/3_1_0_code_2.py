from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
msghmm = Factor("msghmm", ["fhtqa","lxlpwh","mjcz","ruxh","dbi","adzdc","frtoj"])
def is_kfz_gbpdob(msghmm):
    return msghmm[-2] == "frtoj" and msghmm[0] != "frtoj"
def is_kfz_aei(msghmm):
    return msghmm[-2] != "frtoj" and msghmm[0] == "ruxh"
def is_kfz_pve(msghmm):
    return not (is_kfz_gbpdob(msghmm) or is_kfz_aei(msghmm))
kfz = Factor("kfz", [DerivedLevel("gbpdob", Window(is_kfz_gbpdob, [msghmm], 3, 1)), DerivedLevel("aei", Window(is_kfz_aei, [msghmm], 3, 1)), DerivedLevel("pve", Window(is_kfz_pve, [msghmm], 3, 1))])

design=[msghmm,kfz]
crossing=[kfz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END