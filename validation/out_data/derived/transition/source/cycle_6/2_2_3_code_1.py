from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zgzyu = Factor("zgzyu", ["egz","agime","uemcq","jcwx","vxxng","zildm"])
myuanw = Factor("myuanw", ["egz","agime","uemcq","jcwx","vxxng","zildm"])
mpvcn = Factor("mpvcn", ["egz","agime","uemcq","jcwx","vxxng","zildm"])
def xsx(zgzyu, mpvcn, myuanw):
    return zgzyu[0] != mpvcn[-1] and zgzyu[-1] != myuanw[0]
def himr(zgzyu, mpvcn, myuanw):
    return not (zgzyu[0] != mpvcn[-1]) or not (zgzyu[-1] != myuanw[0])
gxatcd = Factor("urgjg", [DerivedLevel("eqi", Transition(xsx, [zgzyu, myuanw, mpvcn])), DerivedLevel("cqtu", Transition(himr, [zgzyu, myuanw, mpvcn]))])
### EXPERIMENT
design=[zgzyu,myuanw,mpvcn,gxatcd]
crossing=[gxatcd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END