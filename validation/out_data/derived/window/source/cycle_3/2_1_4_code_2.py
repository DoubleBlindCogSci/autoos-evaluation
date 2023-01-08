from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hsva = Factor("hsva", ["ksmtfw","ldum","mfr","vxyb","rhjo","wghwmg"])
def is_aizxw_okb(hsva):
    return hsva[0] != "wghwmg" or hsva[-1] != "ksmtfw"
def is_aizxw_atvuk(hsva):
    return not is_aizxw_okb(hsva)
aizxw= Factor("aizxw", [DerivedLevel("okb", Window(is_aizxw_okb, [hsva], 2, 1)), DerivedLevel("atvuk", Window(is_aizxw_atvuk, [hsva], 2, 1))])

design=[hsva,aizxw]
crossing=[aizxw]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END
