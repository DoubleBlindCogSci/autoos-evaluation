from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
aocjcc = Factor("aocjcc", ["zorjxn","grm","dtgb","vtqfb","sbywr","cgpu"])
def is_wpwnio_klqixa(aocjcc):
    return aocjcc[-1] != "sbywr" and aocjcc[0] != "cgpu"
def is_wpwnio_meswvx(aocjcc):
    return not is_wpwnio_klqixa(aocjcc)
wpwnio= Factor("wpwnio", [DerivedLevel("klqixa", Transition(is_wpwnio_klqixa, [aocjcc])), DerivedLevel("meswvx", Transition(is_wpwnio_meswvx, [aocjcc]))])

design=[aocjcc,wpwnio]
crossing=[wpwnio]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END
