from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rjaw= Factor("rjaw", ["kjzxjz","fkez","xepdr","wodnb","autly","fuq"])
def is_kumm_endn(rjaw):
    return rjaw[-1] != "wodnb" and rjaw[0] == "xepdr"
def is_kumm_bwbhn(rjaw):
    return not is_kumm_endn(rjaw)
kumm= Factor("kumm", [DerivedLevel("endn", Transition(is_kumm_endn, [rjaw])), DerivedLevel("bwbhn", Transition(is_kumm_bwbhn, [rjaw]))])

design=[rjaw,kumm]
crossing=[kumm]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END
