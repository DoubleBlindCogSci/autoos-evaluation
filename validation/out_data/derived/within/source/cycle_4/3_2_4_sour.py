from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vtn = Factor("vtn", ["aoboa","oxdsji","uewi","liwbka","tdwxt","oqcxu","yjywvu"])
ewjn = Factor("ewjn", ["aoboa","oxdsji","uewi","liwbka","tdwxt","oqcxu","yjywvu"])
bvind = Factor("bvind", ["aoboa","oxdsji","uewi","liwbka","tdwxt","oqcxu","yjywvu"])
def uxk(vtn, ewjn, bvind):
     return vtn == ewjn
def zkm(vtn, ewjn, bvind):
     return ewjn != vtn and bvind == vtn
def pop(vtn, ewjn, bvind):
     return (not uxk(vtn, ewjn, bvind)) and (vtn != bvind)
gysh = Factor("jjev", [DerivedLevel("pbx", WithinTrial(uxk, [vtn, ewjn, bvind])), DerivedLevel("dmhmm", WithinTrial(zkm, [vtn, ewjn, bvind])),DerivedLevel("xegnon", WithinTrial(pop, [vtn, ewjn, bvind]))])
### EXPERIMENT
design=[vtn,ewjn,bvind,gysh]
crossing=[gysh]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)