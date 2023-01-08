from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qnydp = Factor("qnydp", ["nervs","yui","exbykd","ofjg","pnkdfj","kpip","gmy","jsno"])
wayn = Factor("wayn", ["ljxc","hdyo","engxux","atdyxi","dtuvgm","zjhnyn","tvb","rinri"])
def gguc(qnydp, wayn):
     return qnydp == "ofjg"
def tljbaz(qnydp, wayn):
     return "ofjg" != qnydp and  wayn == "tvb"
def pssejb(qnydp, wayn):
     return (qnydp != "ofjg") and (not wayn == "tvb")
phvxez = Factor("ltd", [DerivedLevel("xqosw", WithinTrial(gguc, [qnydp, wayn])), DerivedLevel("eortzq", WithinTrial(tljbaz, [qnydp, wayn])),DerivedLevel("czvpgj", WithinTrial(pssejb, [qnydp, wayn]))])
### EXPERIMENT
design=[qnydp,wayn,phvxez]
crossing=[phvxez]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)