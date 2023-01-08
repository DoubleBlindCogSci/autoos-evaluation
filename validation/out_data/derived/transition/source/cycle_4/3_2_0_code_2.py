from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jmz = Factor("jmz", ["jihy","vml","ualooh","zwib","okr","ltap"])
sqg = Factor("sqg", ["bxsq","cunuta","nxlob","vmuyd","ysq","xtn"])
def is_zbhiv_puhii(jmz, sqg):
    return jmz[-1] == "jihy" and sqg[0] != "xtn"
def is_zbhiv_wdcu(jmz, sqg):
    return jmz[-1] != "jihy" and sqg[0] == "xtn"
def is_zbhiv_kwuqg(jmz, sqg):
    return not (is_zbhiv_puhii(jmz, sqg) or is_zbhiv_wdcu(jmz, sqg))
zbhiv= Factor("zbhiv", [DerivedLevel("puhii", Transition(is_zbhiv_puhii, [jmz, sqg])), DerivedLevel("wdcu", Transition(is_zbhiv_wdcu, [jmz, sqg])), DerivedLevel("kwuqg", Transition(is_zbhiv_kwuqg, [jmz, sqg]))])

design=[jmz,sqg,zbhiv]
crossing=[zbhiv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END