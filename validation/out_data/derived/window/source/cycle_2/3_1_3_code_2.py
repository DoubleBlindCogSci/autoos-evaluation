from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mcfe= Factor("mcfe", ["cjd","pdhx","gxwuy","kwmu","jjuu","pzqea","llbj"])
def is_ewfej_jozju(mcfe):
    return mcfe[-3] == "jjuu" and mcfe[0] != "jjuu"
def is_ewfej_tozb(mcfe):
    return mcfe[-3] != "jjuu" and mcfe[0] == "cjd"
def is_ewfej_qpbcog(mcfe):
    return not (is_ewfej_jozju(mcfe) or is_ewfej_tozb(mcfe))
ewfej= Factor("ewfej", [DerivedLevel("jozju", Window(is_ewfej_jozju, [mcfe], 4, 1)), DerivedLevel("tozb", Window(is_ewfej_tozb, [mcfe], 4, 1)), DerivedLevel("qpbcog", Window(is_ewfej_qpbcog, [mcfe], 4, 1))])

design=[mcfe,ewfej]
crossing=[ewfej]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END
