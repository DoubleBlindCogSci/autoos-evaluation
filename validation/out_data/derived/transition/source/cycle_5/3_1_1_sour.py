from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
uano = Factor("uano", ["hspapo","hlyj","swp","motz","okbuz","scxcn"])
def qei(uano):
     return uano[0] == "hspapo" and uano[-1] != "okbuz"
def tvozp(uano):
     return (not "hspapo" != uano[0]) and  uano[-1] == "okbuz"
def msqg(uano):
     return (uano[0] != "hspapo") and (not uano[-1] == "okbuz")
lem = DerivedLevel("szyjh", Transition(qei, [uano]))
ydozt = DerivedLevel("xogpak", Transition(tvozp, [uano]))
ruinsa = DerivedLevel("fkkgx", Transition(msqg, [uano]))
hmz = Factor("zzbnv", [lem, ydozt, ruinsa])

### EXPERIMENT
design=[uano,hmz]
crossing=[hmz]
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