from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jqnhlp= Factor("jqnhlp", ["hyl","qugw","mwgk","ojnya","kpg","zul","mjsx"])
def is_ylw_vszfo(jqnhlp):
    return jqnhlp[0] == "ojnya"
def is_ylw_bqhaz(jqnhlp):
    return jqnhlp[0] == "mjsx"
def is_ylw_ugwna(jqnhlp):
    return not (is_ylw_vszfo(jqnhlp) or is_ylw_bqhaz(jqnhlp))
ylw= Factor("ylw", [DerivedLevel("vszfo", Transition(is_ylw_vszfo, [jqnhlp])), DerivedLevel("bqhaz", Transition(is_ylw_bqhaz, [jqnhlp])), DerivedLevel("ugwna", Transition(is_ylw_ugwna, [jqnhlp]))])

design=[jqnhlp,ylw]
crossing=[ylw]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_2"))

### END
