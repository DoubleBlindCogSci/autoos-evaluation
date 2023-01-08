from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
kpzzs = Factor("kpzzs", ["trnsf","euqvm","eopzt","hruj","aoi","tsrpg","nysyn","yezi"])
yfbw = Factor("yfbw", ["trnsf","euqvm","eopzt","hruj","aoi","tsrpg","nysyn","yezi"])
pelwq = Factor("pelwq", ["trnsf","euqvm","eopzt","hruj","aoi","tsrpg","nysyn","yezi"])
def cootr(kpzzs, yfbw, pelwq):
     return yfbw[-1] == kpzzs[-3]
def okrank(kpzzs, yfbw, pelwq):
     return yfbw[-1] != kpzzs[-3] and pelwq[-3] == kpzzs[-1]
def tius(kpzzs, yfbw, pelwq):
     return (kpzzs[-3] != yfbw[-1]) and (kpzzs[-1] != pelwq[-3])
kfytpp = DerivedLevel("rlntfd", Window(cootr, [kpzzs, yfbw, pelwq],4,1))
cnftpf = DerivedLevel("ipwd", Window(okrank, [kpzzs, yfbw, pelwq],4,1))
qroo = DerivedLevel("crte", Window(tius, [kpzzs, yfbw, pelwq],4,1))
xkry = Factor("yzrhbj", [kfytpp, cnftpf, qroo])

### EXPERIMENT
design=[kpzzs,yfbw,pelwq,xkry]
crossing=[xkry]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END