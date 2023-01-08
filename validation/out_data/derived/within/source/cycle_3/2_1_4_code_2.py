from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
aeckdg = Factor("aeckdg", ["rhdi","uslq","jauqo","tiydi","gpj"])
def is_tpax_auu(aeckdg):
    return aeckdg != "jauqo"
def is_tpax_rurk(aeckdg):
    return not is_tpax_auu(aeckdg)
tpax= Factor("tpax", [DerivedLevel("auu", WithinTrial(is_tpax_auu, [aeckdg])), DerivedLevel("rurk", WithinTrial(is_tpax_rurk, [aeckdg]))])

design=[aeckdg,tpax]
crossing=[tpax]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END
