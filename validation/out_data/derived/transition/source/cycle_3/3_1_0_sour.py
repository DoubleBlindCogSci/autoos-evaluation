from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bsszxa = Factor("bsszxa", ["qbylzt","qwco","mzknpx","vcov","qmkypw","mzhdya","ijd"])
def kpyp(bsszxa):
     return bsszxa[0] == "qwco" and bsszxa[-1] != "qbylzt"
def phz(bsszxa):
     return (bsszxa[0] != "qwco") and  bsszxa[-1] == "qbylzt"
def ssciw(bsszxa):
     return (bsszxa[0] != "qwco") and (not bsszxa[-1] == "qbylzt")
duxz = Factor("vacdzn", [DerivedLevel("aaiu", Transition(kpyp, [bsszxa])), DerivedLevel("plu", Transition(phz, [bsszxa])),DerivedLevel("gusq", Transition(ssciw, [bsszxa]))])
### EXPERIMENT
design=[bsszxa,duxz]
crossing=[duxz]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_0_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)