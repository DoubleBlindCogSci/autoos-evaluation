from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jvd = Factor("jvd", ["qlov","feiuit","jsy","grr","eewt","ajb","ioroa"])
def is_kxcewo_occdnc(jvd):
    return jvd[-1] != "ajb" or jvd[0] != "grr"
def is_kxcewo_toqqq(jvd):
    return not is_kxcewo_occdnc(jvd)
kxcewo = Factor("kxcewo", [DerivedLevel("occdnc", Transition(is_kxcewo_occdnc, [jvd])), DerivedLevel("toqqq", Transition(is_kxcewo_toqqq, [jvd]))])

design=[jvd,kxcewo]
crossing=[kxcewo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END