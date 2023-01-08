from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rkhed = Factor("rkhed", ["uarmno","isfq","bdzii","dqz","oqw","seanww","uywzva"])
wogtke = Factor("wogtke", ["uarmno","isfq","bdzii","dqz","oqw","seanww","uywzva"])
xato = Factor("xato", ["uarmno","isfq","bdzii","dqz","oqw","seanww","uywzva"])
def yqjp(rkhed, wogtke, xato):
    return rkhed != wogtke and rkhed == xato
def bdhud(rkhed, wogtke, xato):
    return not yqjp(rkhed, wogtke, xato)
rzeqy = DerivedLevel("wxmis", WithinTrial(yqjp, [rkhed, wogtke, xato]))
ppw = DerivedLevel("mjengt", WithinTrial(bdhud, [rkhed, wogtke, xato]))
tzuxy = Factor("uncy", [rzeqy, ppw])

### EXPERIMENT
design=[rkhed,wogtke,xato,tzuxy]
crossing=[tzuxy]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)