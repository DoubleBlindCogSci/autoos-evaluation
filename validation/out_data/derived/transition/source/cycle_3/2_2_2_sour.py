from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
los = Factor("los", ["ubxc","wacwp","uywtvx","cflb","hre","clv","qvw"])
wwbpe = Factor("wwbpe", ["qba","sckl","ojtn","avwq","sprqyp","ieh","dnhzuw"])
def riedv(los, wwbpe):
    return los[0] == "hre" and wwbpe[-1] != "qba"
def zgsux(los,wwbpe):
    return not (los[0] == "hre") or not (wwbpe[-1] != "qba")
dsi = DerivedLevel("yfg", Transition(riedv, [los, wwbpe]))
nqiu = DerivedLevel("jzzqzd", Transition(zgsux, [los, wwbpe]))
xbrx = Factor("ejluh", [dsi, nqiu])

### EXPERIMENT
design=[los,wwbpe,xbrx]
crossing=[xbrx]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)