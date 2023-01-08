from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
ydckd = Factor("ydckd", ["augs","eozzc","ezdw","kvuoan","kmosuf"])
frj = Factor("frj", ["rcqr","tuxwtk","ixn","xxoysb","kitwv","zldb","zeg"])
def uegan(ydckd, frj):
    return ydckd[-2] == "ezdw" and frj[0] == "rcqr"
def osps(ydckd,frj):
    return not uegan(ydckd, frj)
mji = Factor("ckfq", [DerivedLevel("vbsggr", Window(uegan, [ydckd, frj],3)), DerivedLevel("qdpq", Window(osps, [ydckd, frj],3))])
### EXPERIMENT
design=[ydckd,frj,mji]
crossing=[mji]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)