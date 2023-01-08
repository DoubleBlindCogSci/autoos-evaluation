from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jkoa = Factor("jkoa", ["dty","jip","fdhyva","rdrtvh","mrvqki","yip","qhfeku","aao"])
def is_rvuld_cwq(jkoa):
    return jkoa[0] == "dty" and jkoa[-1] != "dty"
def is_rvuld_uworl(jkoa):
    return jkoa[0] != "dty" and jkoa[-1] == "rdrtvh"
def is_rvuld_xvza(jkoa):
    return not (is_rvuld_cwq(jkoa) or is_rvuld_uworl(jkoa))
rvuld = Factor("rvuld", [DerivedLevel("cwq", Window(is_rvuld_cwq, [jkoa], 2, 1)), DerivedLevel("uworl", Window(is_rvuld_uworl, [jkoa], 2, 1)), DerivedLevel("xvza", Window(is_rvuld_xvza, [jkoa], 2, 1))])

design=[jkoa,rvuld]
crossing=[rvuld]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END