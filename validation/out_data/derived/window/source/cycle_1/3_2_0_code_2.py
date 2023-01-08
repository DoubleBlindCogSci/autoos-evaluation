from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kpzzs= Factor("kpzzs", ["trnsf","euqvm","eopzt","hruj","aoi","tsrpg","nysyn","yezi"])
yfbw= Factor("yfbw", ["trnsf","euqvm","eopzt","hruj","aoi","tsrpg","nysyn","yezi"])
pelwq= Factor("pelwq", ["trnsf","euqvm","eopzt","hruj","aoi","tsrpg","nysyn","yezi"])
def is_yzrhbj_rlntfd(yfbw, kpzzs):
    return yfbw[0] == kpzzs[-3]
def is_yzrhbj_ipwd(yfbw, kpzzs, pelwq):
    return yfbw[0] != kpzzs[-3] and pelwq[0] == kpzzs[-1]
def is_yzrhbj_crte(yfbw, kpzzs, pelwq):
    return not (is_yzrhbj_rlntfd(yfbw, kpzzs) or is_yzrhbj_ipwd(yfbw, kpzzs, pelwq))
yzrhbj= Factor("yzrhbj", [DerivedLevel("rlntfd", Window(is_yzrhbj_rlntfd, [yfbw, kpzzs], 4, 1)), DerivedLevel("ipwd", Window(is_yzrhbj_ipwd, [yfbw, kpzzs, pelwq], 4, 1)), DerivedLevel("crte", Window(is_yzrhbj_crte, [yfbw, kpzzs, pelwq], 4, 1))])

design=[kpzzs,yfbw,pelwq,yzrhbj]
crossing=[yzrhbj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END
