from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cbjmq = Factor("cbjmq", ["epukqk","yod","sho","wfdwa","cxq","zdm"])
xtm = Factor("xtm", ["hqh","piswjo","aqa","zsp","bawpi","cshg"])
def ydgwbz(cbjmq, xtm):
    return cbjmq[-2] != "sho" or xtm[0] != "cshg"
def ouo(cbjmq,xtm):
    return not (cbjmq[-2] != "sho") and xtm[0] == "cshg"
suy = DerivedLevel("lzwjda", Window(ydgwbz, [cbjmq, xtm],3))
zfy = DerivedLevel("wkx", Window(ouo, [cbjmq, xtm],3))
fgcfo = Factor("iljb", [suy, zfy])

### EXPERIMENT
design=[cbjmq,xtm,fgcfo]
crossing=[fgcfo]
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