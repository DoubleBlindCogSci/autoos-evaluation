from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
opoq = Factor("opoq", ["aonory","ilst","hjph","rsn","ovie","yvqo","fkdakj"])
def qhrvq(opoq):
     return opoq == "rsn"
def qefr(opoq):
     return opoq == "yvqo"
def xro(opoq):
     return (opoq != "rsn") and (opoq != "yvqo")
ged = DerivedLevel("nusuv", WithinTrial(qhrvq, [opoq]))
eto = DerivedLevel("plz", WithinTrial(qefr, [opoq]))
eagyxh = DerivedLevel("hhq", WithinTrial(xro, [opoq]))
vsyap = Factor("ddehh", [ged, eto, eagyxh])

### EXPERIMENT
design=[opoq,vsyap]
crossing=[vsyap]
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