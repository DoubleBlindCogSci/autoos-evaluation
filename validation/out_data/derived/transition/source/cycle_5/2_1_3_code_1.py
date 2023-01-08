from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jkcaj = Factor("jkcaj", ["nxip","xpdv","rzxvl","tuuxm","emhnjb","yfnjf","ddgpit"])
def hckmrc(jkcaj):
    return jkcaj[0] == "xpdv" and jkcaj[-1] == "yfnjf"
def tbr(jkcaj):
    return not (jkcaj[0] == "xpdv") or not (jkcaj[0] == "yfnjf")
yehnk = Factor("nmbtmo", [DerivedLevel("sruh", Transition(hckmrc, [jkcaj])), DerivedLevel("wkfzon", Transition(tbr, [jkcaj]))])
### EXPERIMENT
design=[jkcaj,yehnk]
crossing=[yehnk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END