from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ldl= Factor("ldl", ["xtgz","acrbvr","jkvqrs","bsmf","ten","ecs"])
def is_gwyg_roopgk(ldl):
    return ldl[-1] != "xtgz" and ldl[0] != "ecs"
def is_gwyg_ehauj(ldl):
    return not is_gwyg_roopgk(ldl)
gwyg= Factor("gwyg", [DerivedLevel("roopgk", Window(is_gwyg_roopgk, [ldl], 2, 1)), DerivedLevel("ehauj", Window(is_gwyg_ehauj, [ldl], 2, 1))])

design=[ldl, gwyg]
crossing=[gwyg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END
