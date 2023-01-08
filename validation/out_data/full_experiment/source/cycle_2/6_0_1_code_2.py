from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
bmmkoy = Factor("bmmkoy", ["fbdy", "oobt"])
txl = Factor("txl", ["iato", "wmmzjh"])
tofpnu = Factor("tofpnu", ["fbdy", "oobt"])
xxegfy = Factor("xxegfy", ["iato", "wmmzjh"])
wha = Factor("wha", ["npf", "adl"])
vsmn = Factor("vsmn", ["qdj", "fppmhw"])
constraints = [AtMostKInARow(3, wha)]
crossing = [tofpnu, vsmn]

design=[bmmkoy,txl,tofpnu,xxegfy,wha,vsmn]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_0_1"))
