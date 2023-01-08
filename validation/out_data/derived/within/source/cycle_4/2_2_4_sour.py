from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jpojl = Factor("jpojl", ["aquqin","ajbzl","vrqlg","ncwxi","qbz"])
ewdzs = Factor("ewdzs", ["aquqin","ajbzl","vrqlg","ncwxi","qbz"])
vwk = Factor("vwk", ["aquqin","ajbzl","vrqlg","ncwxi","qbz"])
def hfcas(jpojl, ewdzs, vwk):
    return jpojl != ewdzs
def bsz(jpojl, ewdzs, vwk):
    return jpojl == ewdzs
rqywut = DerivedLevel("luxv", WithinTrial(hfcas, [jpojl, ewdzs, vwk]))
ung = DerivedLevel("nrhpia", WithinTrial(bsz, [jpojl, ewdzs, vwk]))
krydor = Factor("bjn", [rqywut, ung])

### EXPERIMENT
design=[jpojl,ewdzs,vwk,krydor]
crossing=[krydor]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)