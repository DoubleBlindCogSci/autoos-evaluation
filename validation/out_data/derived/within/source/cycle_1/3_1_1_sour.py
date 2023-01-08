from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
pbbncw = Factor("pbbncw", ["nmxpb","itt","ijv","imuzj","tjfdht","eumhf","mravi"])
def mddw(pbbncw):
     return pbbncw == "nmxpb"
def lwn(pbbncw):
     return "mravi" == pbbncw
def iuar(pbbncw):
     return (not mddw(pbbncw)) and (not lwn(pbbncw))
rsbjw = Factor("jwgl", [DerivedLevel("yzl", WithinTrial(mddw, [pbbncw])), DerivedLevel("qvxiuo", WithinTrial(lwn, [pbbncw])),DerivedLevel("mqi", WithinTrial(iuar, [pbbncw]))])
### EXPERIMENT
design=[pbbncw,rsbjw]
crossing=[rsbjw]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_1_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)