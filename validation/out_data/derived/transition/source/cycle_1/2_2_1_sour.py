from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
ufgywf = Factor("ufgywf", ["xmtfpe","ehji","ayiczf","izdsqj","snhh","cxpgi","hyshb"])
rudnb = Factor("rudnb", ["xmtfpe","ehji","ayiczf","izdsqj","snhh","cxpgi","hyshb"])
inb = Factor("inb", ["xmtfpe","ehji","ayiczf","izdsqj","snhh","cxpgi","hyshb"])
def jfskg(ufgywf, rudnb, inb):
    return ufgywf[0] == rudnb[-1]
def ncwv(ufgywf, rudnb, inb):
    return ufgywf[0] != rudnb[-1]
cqzpz = Factor("jxoudi", [DerivedLevel("epi", Transition(jfskg, [ufgywf, rudnb, inb])), DerivedLevel("oeefb", Transition(ncwv, [ufgywf, rudnb, inb]))])
### EXPERIMENT
design=[ufgywf,rudnb,inb,cqzpz]
crossing=[cqzpz]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)