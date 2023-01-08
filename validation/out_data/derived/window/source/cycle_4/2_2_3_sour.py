from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ouggqp = Factor("ouggqp", ["lstjle","jvni","cnhe","xzduk","erim","umsm"])
eylw = Factor("eylw", ["lstjle","jvni","cnhe","xzduk","erim","umsm"])
iji = Factor("iji", ["lstjle","jvni","cnhe","xzduk","erim","umsm"])
def cbhf(ouggqp, eylw, iji):
    return ouggqp[0] == eylw[-2]
def ugb(ouggqp, eylw, iji):
    return not cbhf(ouggqp, eylw, iji)
gsgqmk = DerivedLevel("jteux", Window(cbhf, [ouggqp, eylw, iji],3))
lsom = DerivedLevel("oknyrj", Window(ugb, [ouggqp, eylw, iji],3))
vapd = Factor("orl", [gsgqmk, lsom])

### EXPERIMENT
design=[ouggqp,eylw,iji,vapd]
crossing=[vapd]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)