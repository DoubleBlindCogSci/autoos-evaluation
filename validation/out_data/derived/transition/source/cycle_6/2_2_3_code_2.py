from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zgzyu = Factor("zgzyu", ["egz","agime","uemcq","jcwx","vxxng","zildm"])
myuanw = Factor("myuanw", ["egz","agime","uemcq","jcwx","vxxng","zildm"])
mpvcn = Factor("mpvcn", ["egz","agime","uemcq","jcwx","vxxng","zildm"])
def is_urgjg_eqi(zgzyu, myuanw, mpvcn):
    return zgzyu[0] != mpvcn[-1] and zgzyu[0] != myuanw[-1]
def is_urgjg_cqtu(zgzyu, myuanw, mpvcn):
    return not is_urgjg_eqi(zgzyu, myuanw, mpvcn)
urgjg = Factor("urgjg", [DerivedLevel("eqi", Transition(is_urgjg_eqi, [zgzyu, myuanw, mpvcn])), DerivedLevel("cqtu", Transition(is_urgjg_cqtu, [zgzyu, myuanw, mpvcn]))])

design=[zgzyu,myuanw,mpvcn,urgjg]
crossing=[urgjg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END