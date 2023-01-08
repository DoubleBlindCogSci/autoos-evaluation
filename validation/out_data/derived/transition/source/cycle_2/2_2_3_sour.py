from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
khb = Factor("khb", ["duuly","pkdwt","nteh","nitsa","jnzn"])
jotilz = Factor("jotilz", ["duuly","pkdwt","nteh","nitsa","jnzn"])
tdbs = Factor("tdbs", ["duuly","pkdwt","nteh","nitsa","jnzn"])
def ftdyy(khb, tdbs, jotilz):
    return khb[0] == tdbs[-1]
def wwry(khb, tdbs, jotilz):
    return not ftdyy(khb, tdbs, jotilz)
oxamk = Factor("kgpp", [DerivedLevel("fzy", Transition(ftdyy, [khb, jotilz, tdbs])), DerivedLevel("dnr", Transition(wwry, [khb, jotilz, tdbs]))])
### EXPERIMENT
design=[khb,jotilz,tdbs,oxamk]
crossing=[oxamk]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)