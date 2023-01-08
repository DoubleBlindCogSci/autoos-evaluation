from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cnpp = Factor("cnpp", ["kvmnqd","wxxfb","qwtsob","pxolf","wyv","cccj","ktjyt"])
zhunlp = Factor("zhunlp", ["kvmnqd","wxxfb","qwtsob","pxolf","wyv","cccj","ktjyt"])
susug = Factor("susug", ["kvmnqd","wxxfb","qwtsob","pxolf","wyv","cccj","ktjyt"])
def is_bfrrks_jtqqhx(cnpp, zhunlp, susug):
    return cnpp[0] != susug[-1]
def is_bfrrks_muozv(cnpp, zhunlp, susug):
    return not is_bfrrks_jtqqhx(cnpp, zhunlp, susug)
bfrrks= Factor("bfrrks", [DerivedLevel("jtqqhx", Transition(is_bfrrks_jtqqhx, [cnpp, zhunlp, susug])), DerivedLevel("muozv", Transition(is_bfrrks_muozv, [cnpp, zhunlp, susug]))])

design=[cnpp,zhunlp,susug,bfrrks]
crossing=[bfrrks]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END
