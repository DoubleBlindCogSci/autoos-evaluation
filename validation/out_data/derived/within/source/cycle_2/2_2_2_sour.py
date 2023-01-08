from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
dyvxp = Factor("dyvxp", ["lori","cmqw","xrrl","npa","mae"])
akpu = Factor("akpu", ["eced","nvksz","lyct","mamgi","sednn"])
def hbb(dyvxp, akpu):
    return dyvxp != "xrrl" or akpu != "mamgi"
def tglx(dyvxp,akpu):
    return not (dyvxp != "xrrl") and akpu == "mamgi"
wlu = Factor("ekia", [DerivedLevel("qotj", WithinTrial(hbb, [dyvxp, akpu])), DerivedLevel("iacg", WithinTrial(tglx, [dyvxp, akpu]))])
### EXPERIMENT
design=[dyvxp,akpu,wlu]
crossing=[wlu]
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