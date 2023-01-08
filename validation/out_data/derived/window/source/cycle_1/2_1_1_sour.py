from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
vrh = Factor("vrh", ["omipuk","isgp","ycd","vynlqp","lmylt"])
def som(vrh):
    return vrh[-3] == "isgp" and vrh[0] == "omipuk"
def szkum(vrh):
    return vrh[-3] != "isgp" or not (vrh[0] == "omipuk")
pju = Factor("xtq", [DerivedLevel("jhzoqx", Window(som, [vrh],4)), DerivedLevel("lhbwh", Window(szkum, [vrh],4))])
### EXPERIMENT
design=[vrh,pju]
crossing=[pju]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/2_1_1_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/2_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)