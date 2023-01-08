from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yhwoc = Factor("yhwoc", ["bjnqig","rwmp","ivv","drq","fnftsx"])
qkf = Factor("qkf", ["bjnqig","rwmp","ivv","drq","fnftsx"])
gbhqo = Factor("gbhqo", ["bjnqig","rwmp","ivv","drq","fnftsx"])
def tmlazi(yhwoc, gbhqo, qkf):
    return yhwoc[-2] != gbhqo[-1]
def nfrdqo(yhwoc, gbhqo, qkf):
    return not tmlazi(yhwoc, gbhqo, qkf)
pql = DerivedLevel("jcqift", Window(tmlazi, [yhwoc, qkf, gbhqo],3,1))
syfviz = DerivedLevel("keko", Window(nfrdqo, [yhwoc, qkf, gbhqo],3,1))
jpes = Factor("hmig", [pql, syfviz])

### EXPERIMENT
design=[yhwoc,qkf,gbhqo,jpes]
crossing=[jpes]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END