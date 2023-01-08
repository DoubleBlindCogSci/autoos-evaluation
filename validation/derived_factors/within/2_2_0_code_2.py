from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
aareke = Factor("aareke", ["bfu","pdiaf","bwga","azmitw","yow","dkkhf","ylfcsn"])
mvhs = Factor("mvhs", ["jidpsp","orsy","dov","bqtyzr","okixdp","riq","hrq"])
def is_hjeatg_erjtn(aareke, mvhs):
    return aareke == "azmitw" and mvhs == "orsy"
def is_hjeatg_oqk(aareke, mvhs):
    return not is_hjeatg_erjtn(aareke, mvhs)
hjeatg = Factor("hjeatg", [DerivedLevel("erjtn", WithinTrial(is_hjeatg_erjtn, [aareke, mvhs])), DerivedLevel("oqk", WithinTrial(is_hjeatg_oqk, [aareke, mvhs]))])

design=[aareke,mvhs,hjeatg]
crossing=[hjeatg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END