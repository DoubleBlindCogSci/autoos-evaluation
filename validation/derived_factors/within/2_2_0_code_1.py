from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
aareke = Factor("aareke", ["bfu","pdiaf","bwga","azmitw","yow","dkkhf","ylfcsn"])
mvhs = Factor("mvhs", ["jidpsp","orsy","dov","bqtyzr","okixdp","riq","hrq"])
def jin(aareke, mvhs):
    return aareke == "azmitw" and mvhs == "orsy"
def pruchg(aareke,mvhs):
    return not jin(aareke, mvhs)
rtunf = Factor("hjeatg", [DerivedLevel("erjtn", WithinTrial(jin, [aareke, mvhs])), DerivedLevel("oqk", WithinTrial(pruchg, [aareke, mvhs]))])
### EXPERIMENT
design=[aareke,mvhs,rtunf]
crossing=[rtunf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END