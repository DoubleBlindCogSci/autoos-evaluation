from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
med = Factor("med", ["zjbe","enhw","zzeiq","ngeen","tyu","blz","khy","fbcolf"])
def is_bxt_hurev(med):
    return med[-2] == "fbcolf" and med[-1] != "fbcolf"
def is_bxt_axe(med):
    return med[-2] != "fbcolf" and med[-1] == "enhw"
def is_bxt_tuaxow(med):
    return not (is_bxt_hurev(med) or is_bxt_axe(med))
bxt= Factor("bxt", [DerivedLevel("hurev", Window(is_bxt_hurev, [med], 3, 1)), DerivedLevel("axe", Window(is_bxt_axe, [med], 3, 1)), DerivedLevel("tuaxow", Window(is_bxt_tuaxow, [med], 3, 1))])

design=[med,bxt]
crossing=[bxt]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END
