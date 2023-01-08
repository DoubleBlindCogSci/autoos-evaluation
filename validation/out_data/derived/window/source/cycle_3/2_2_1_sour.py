from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
crzz = Factor("crzz", ["nke","nkdfh","zzw","jhwwh","ilp","axon"])
svrko = Factor("svrko", ["nke","nkdfh","zzw","jhwwh","ilp","axon"])
yurqow = Factor("yurqow", ["nke","nkdfh","zzw","jhwwh","ilp","axon"])
def vmykz(crzz, yurqow, svrko):
    return crzz[-3] != yurqow[-2] and crzz[-2] != svrko[-3]
def vctfq(crzz, yurqow, svrko):
    return not (crzz[-3] != yurqow[-2]) or crzz[-2] == svrko[-3]
juqg = Factor("vqh", [DerivedLevel("hmks", Window(vmykz, [crzz, svrko, yurqow],4)), DerivedLevel("aqjgfj", Window(vctfq, [crzz, svrko, yurqow],4))])
### EXPERIMENT
design=[crzz,svrko,yurqow,juqg]
crossing=[juqg]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)