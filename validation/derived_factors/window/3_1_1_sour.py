from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
psxzzw = Factor("psxzzw", ["spa","iigdr","dhsxwz","urwb","sfr","hqigv","noe"])
def hhrnkb(psxzzw):
     return "spa" == psxzzw[-2] and not psxzzw[0] == "spa"
def kyo(psxzzw):
     return psxzzw[-2] != "spa" and  psxzzw[0] == "iigdr"
def rqxl(psxzzw):
     return (psxzzw[-2] != "spa") and (psxzzw[0] != "iigdr")
ngvb = DerivedLevel("sxxi", Window(hhrnkb, [psxzzw],3,1))
ywqddf = DerivedLevel("hsrtsa", Window(kyo, [psxzzw],3,1))
rknz = DerivedLevel("ile", Window(rqxl, [psxzzw],3,1))
eok = Factor("yknaja", [ngvb, ywqddf, rknz])

### EXPERIMENT
design=[psxzzw,eok]
crossing=[eok]
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