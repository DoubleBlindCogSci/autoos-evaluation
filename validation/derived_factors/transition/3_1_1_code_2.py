from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bid = Factor("bid", ["bmwjyr","ophcsg","vltrhp","nmsmxy","ttssnv","nqhf","jxebnk"])
def is_abmuxe_cbnphq(bid):
    return bid[-1] == "ttssnv" and bid[0] != "nqhf"
def is_abmuxe_xbl(bid):
    return bid[-1] != "ttssnv" and bid[0] == "nqhf"
def is_abmuxe_oftp(bid):
    return not (is_abmuxe_cbnphq(bid) or is_abmuxe_xbl(bid))
abmuxe = Factor("abmuxe", [DerivedLevel("cbnphq", Transition(is_abmuxe_cbnphq, [bid])), DerivedLevel("xbl", Transition(is_abmuxe_xbl, [bid])), DerivedLevel("oftp", Transition(is_abmuxe_oftp, [bid]))])

design=[bid,abmuxe]
crossing=[abmuxe]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END