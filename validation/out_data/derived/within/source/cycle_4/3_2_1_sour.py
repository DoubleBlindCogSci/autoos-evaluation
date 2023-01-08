from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rqs = Factor("rqs", ["zbovp","fimc","jsvdkt","dfmgrq","vhvci","bian","huv"])
kcxu = Factor("kcxu", ["zbovp","fimc","jsvdkt","dfmgrq","vhvci","bian","huv"])
ouebx = Factor("ouebx", ["zbovp","fimc","jsvdkt","dfmgrq","vhvci","bian","huv"])
def tuwln(rqs, ouebx, kcxu):
     return ouebx == rqs
def pxf(rqs, ouebx, kcxu):
     return ouebx != rqs and kcxu == rqs
def bixv(rqs, ouebx, kcxu):
     return (rqs != ouebx) and (rqs != kcxu)
abde = DerivedLevel("lzdlm", WithinTrial(tuwln, [rqs, kcxu, ouebx]))
nbr = DerivedLevel("kyvmnu", WithinTrial(pxf, [rqs, kcxu, ouebx]))
llem = DerivedLevel("qddvj", WithinTrial(bixv, [rqs, kcxu, ouebx]))
fsn = Factor("smd", [abde, nbr, llem])

### EXPERIMENT
design=[rqs,kcxu,ouebx,fsn]
crossing=[fsn]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)