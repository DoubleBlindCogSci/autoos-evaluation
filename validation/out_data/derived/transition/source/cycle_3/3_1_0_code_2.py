from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bsszxa = Factor("bsszxa", ["qbylzt","qwco","mzknpx","vcov","qmkypw","mzhdya","ijd"])
def is_vacdzn_aaiu(bsszxa):
    return bsszxa[0] == "qwco" and bsszxa[-1] != "qbylzt"
def is_vacdzn_plu(bsszxa):
    return bsszxa[0] != "qwco" and bsszxa[-1] == "qbylzt"
def is_vacdzn_gusq(bsszxa):
    return not (is_vacdzn_aaiu(bsszxa) or is_vacdzn_plu(bsszxa))
vacdzn= Factor("vacdzn", [DerivedLevel("aaiu", Transition(is_vacdzn_aaiu, [bsszxa])), DerivedLevel("plu", Transition(is_vacdzn_plu, [bsszxa])), DerivedLevel("gusq", Transition(is_vacdzn_gusq, [bsszxa]))])

design=[bsszxa,vacdzn]
crossing=[vacdzn]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END
