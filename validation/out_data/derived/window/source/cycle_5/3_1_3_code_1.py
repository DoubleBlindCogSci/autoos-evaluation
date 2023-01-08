from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jkoa = Factor("jkoa", ["dty","jip","fdhyva","rdrtvh","mrvqki","yip","qhfeku","aao"])
def emfv(jkoa):
     return jkoa[0] == "dty" and not jkoa[-1] == "dty"
def edxcez(jkoa):
     return not "dty" == jkoa[0] and  jkoa[-1] == "rdrtvh"
def rub(jkoa):
     return (not jkoa[0] == "dty") and (not edxcez(jkoa))
oil = DerivedLevel("cwq", Window(emfv, [jkoa],2,1))
esa = DerivedLevel("uworl", Window(edxcez, [jkoa],2,1))
btphh = DerivedLevel("xvza", Window(rub, [jkoa],2,1))
wqa = Factor("rvuld", [oil, esa, btphh])

### EXPERIMENT
design=[jkoa,wqa]
crossing=[wqa]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END