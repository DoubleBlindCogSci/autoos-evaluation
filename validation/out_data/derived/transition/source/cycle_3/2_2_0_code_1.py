from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cnpp = Factor("cnpp", ["kvmnqd","wxxfb","qwtsob","pxolf","wyv","cccj","ktjyt"])
zhunlp = Factor("zhunlp", ["kvmnqd","wxxfb","qwtsob","pxolf","wyv","cccj","ktjyt"])
susug = Factor("susug", ["kvmnqd","wxxfb","qwtsob","pxolf","wyv","cccj","ktjyt"])
def zkckv(cnpp, susug, zhunlp):
    return cnpp[0] != susug[-1]
def ggx(cnpp, susug, zhunlp):
    return cnpp[0] == susug[-1]
wkff = Factor("bfrrks", [DerivedLevel("jtqqhx", Transition(zkckv, [cnpp, zhunlp, susug])), DerivedLevel("muozv", Transition(ggx, [cnpp, zhunlp, susug]))])
### EXPERIMENT
design=[cnpp,zhunlp,susug,wkff]
crossing=[wkff]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END