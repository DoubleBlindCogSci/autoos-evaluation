from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ligw = Factor("ligw", ["rgf","cubid","prn","xsxf","frw","bchrwt"])
nwa = Factor("nwa", ["rgf","cubid","prn","xsxf","frw","bchrwt"])
rcdafu = Factor("rcdafu", ["rgf","cubid","prn","xsxf","frw","bchrwt"])
def mokiba(ligw, nwa, rcdafu):
    return ligw[0] == nwa[-1]
def wsgd(ligw, nwa, rcdafu):
    return ligw[0] != nwa[-1]
ivpzy = DerivedLevel("uyqqzq", Transition(mokiba, [ligw, nwa, rcdafu]))
hyyems = DerivedLevel("irgx", Transition(wsgd, [ligw, nwa, rcdafu]))
gujpcx = Factor("vsz", [ivpzy, hyyems])

### EXPERIMENT
design=[ligw,nwa,rcdafu,gujpcx]
crossing=[gujpcx]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)