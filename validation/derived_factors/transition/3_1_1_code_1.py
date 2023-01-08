from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bid = Factor("bid", ["bmwjyr","ophcsg","vltrhp","nmsmxy","ttssnv","nqhf","jxebnk"])
def onqpm(bid):
     return "ttssnv" == bid[0] and not bid[-1] == "nqhf"
def hfx(bid):
     return (not "ttssnv" != bid[0]) and  "nqhf" == bid[-1]
def tvqpn(bid):
     return (not onqpm(bid)) and (not bid[-1] == "nqhf")
dycye = DerivedLevel("cbnphq", Transition(onqpm, [bid]))
nohcz = DerivedLevel("xbl", Transition(hfx, [bid]))
cutn = DerivedLevel("oftp", Transition(tvqpn, [bid]))
jkak = Factor("abmuxe", [dycye, nohcz, cutn])

### EXPERIMENT
design=[bid,jkak]
crossing=[jkak]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END