from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zpik = Factor("zpik", ["fmpi","ynxy","xbo","cugq","wkksi"])
hzeny = Factor("hzeny", ["fmpi","ynxy","xbo","cugq","wkksi"])
hajvj = Factor("hajvj", ["fmpi","ynxy","xbo","cugq","wkksi"])
def ppjyq(zpik, hajvj, hzeny):
    return zpik[-1] == hajvj[0]
def tffw(zpik, hajvj, hzeny):
    return not (zpik[-1] == hajvj[0])
plvzj = Factor("eihb", [DerivedLevel("txc", Window(ppjyq, [zpik, hzeny, hajvj],2,1)), DerivedLevel("zkbc", Window(tffw, [zpik, hzeny, hajvj],2,1))])
### EXPERIMENT
design=[zpik,hzeny,hajvj,plvzj]
crossing=[plvzj]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)