from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
aus = Factor("aus", ["joiup","gnnuy","alus","ijtzt","bpi","utz"])
def lcz(aus):
    return aus[0] == "bpi" or aus[-1] == "joiup"
def bcb(aus):
    return aus[0] != "bpi" and aus[-1] != "joiup"
wyisu = Factor("nsvlgj", [DerivedLevel("yfwz", Transition(lcz, [aus])), DerivedLevel("mhpggi", Transition(bcb, [aus]))])
### EXPERIMENT
design=[aus,wyisu]
crossing=[wyisu]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_3_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)