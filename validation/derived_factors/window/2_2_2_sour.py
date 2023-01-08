from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nftejx = Factor("nftejx", ["slppp","onzvvm","dhzy","syu","sxis"])
zqsk = Factor("zqsk", ["slppp","onzvvm","dhzy","syu","sxis"])
apbr = Factor("apbr", ["slppp","onzvvm","dhzy","syu","sxis"])
def ldsboj(nftejx, apbr, zqsk):
    return nftejx[-2] != apbr[0]
def hrievt(nftejx, apbr, zqsk):
    return not (nftejx[-2] != apbr[0])
upgkr = DerivedLevel("mlr", Window(ldsboj, [nftejx, zqsk, apbr],3,1))
xtihv = DerivedLevel("iypza", Window(hrievt, [nftejx, zqsk, apbr],3,1))
osi = Factor("noe", [upgkr, xtihv])

### EXPERIMENT
design=[nftejx,zqsk,apbr,osi]
crossing=[osi]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)