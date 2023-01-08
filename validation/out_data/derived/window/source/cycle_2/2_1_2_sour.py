from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
vinn = Factor("vinn", ["ocg","tyc","ajcqj","dwq","eixzwg"])
def gtz(vinn):
    return vinn[-3] != "ocg" or vinn[-2] == "eixzwg"
def zpj(vinn):
    return not (vinn[-3] != "ocg") and vinn[-2] != "eixzwg"
ozytaw = DerivedLevel("iyflel", Window(gtz, [vinn],4))
zcby = DerivedLevel("hnojgz", Window(zpj, [vinn],4))
sfqq = Factor("mktqr", [ozytaw, zcby])

### EXPERIMENT
design=[vinn,sfqq]
crossing=[sfqq]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_2_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)