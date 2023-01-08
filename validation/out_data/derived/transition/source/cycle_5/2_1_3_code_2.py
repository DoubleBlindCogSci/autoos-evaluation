from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jkcaj = Factor("jkcaj", ["nxip","xpdv","rzxvl","tuuxm","emhnjb","yfnjf","ddgpit"])
def is_nmbtmo_sruh(jkcaj):
    return jkcaj[0] == "xpdv" and jkcaj[-1] == "yfnjf"
def is_nmbtmo_wkfzon(jkcaj):
    return not is_nmbtmo_sruh(jkcaj)
nmbtmo = Factor("nmbtmo", [DerivedLevel("sruh", Transition(is_nmbtmo_sruh, [jkcaj])), DerivedLevel("wkfzon", Transition(is_nmbtmo_wkfzon, [jkcaj]))])

design=[jkcaj,nmbtmo]
crossing=[nmbtmo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END