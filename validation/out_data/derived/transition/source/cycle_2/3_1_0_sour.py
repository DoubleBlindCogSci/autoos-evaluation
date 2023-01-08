from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
nzeyhy = Factor("nzeyhy", ["qyl","vnxtdl","tjy","mvbc","lvo","gbxcg"])
def grv(nzeyhy):
     return nzeyhy[0] == "gbxcg" and not nzeyhy[-1] == "lvo"
def pdcb(nzeyhy):
     return (nzeyhy[0] != "gbxcg") and  nzeyhy[-1] == "lvo"
def hynib(nzeyhy):
     return (nzeyhy[0] != "gbxcg") and (nzeyhy[-1] != "lvo")
rbyqi = Factor("umf", [DerivedLevel("olado", Transition(grv, [nzeyhy])), DerivedLevel("dxkmeo", Transition(pdcb, [nzeyhy])),DerivedLevel("yedcyl", Transition(hynib, [nzeyhy]))])
### EXPERIMENT
design=[nzeyhy,rbyqi]
crossing=[rbyqi]
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