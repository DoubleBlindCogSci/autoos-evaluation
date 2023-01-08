from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
owxvgu = Factor("owxvgu", ["fank","hxcwvz","ojhyp","agjxdr","bacc","vxp","bfcshl"])
epixg = Factor("epixg", ["fank","hxcwvz","ojhyp","agjxdr","bacc","vxp","bfcshl"])
hwd = Factor("hwd", ["fank","hxcwvz","ojhyp","agjxdr","bacc","vxp","bfcshl"])
def gzmdl(owxvgu, epixg, hwd):
    return owxvgu[0] != epixg[-1]
def aquw(owxvgu, epixg, hwd):
    return not gzmdl(owxvgu, epixg, hwd)
xjt = DerivedLevel("akkuo", Transition(gzmdl, [owxvgu, epixg, hwd]))
znucw = DerivedLevel("gniz", Transition(aquw, [owxvgu, epixg, hwd]))
ubd = Factor("gxrai", [xjt, znucw])

### EXPERIMENT
design=[owxvgu,epixg,hwd,ubd]
crossing=[ubd]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)