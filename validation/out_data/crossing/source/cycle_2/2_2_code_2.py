from sweetpea import *
import os
_dir=os.path.dirname(__file__)
gtfl = Factor("gtfl", ["exwxvn", "ragbhz"])
aqi = Factor("aqi", ["zmmsru", "xfsm"])
dgudue = Factor("dgudue", ["bvx", "nyaxv"])
aeq = Factor("aeq", ["egjrcj", "jdo"])
bkpuu = Factor("bkpuu", ["bkquvl", "fgrnd"])
constraints = []
crossing = [[gtfl, aqi, dgudue], [aeq, bkpuu]]


design=[gtfl,aqi,dgudue,aeq,bkpuu]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2"))

### END