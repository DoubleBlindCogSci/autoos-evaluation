from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ush = Factor("ush", ["mtzxp","tdgw","szz","asc","pjni","umob","vhrm"])
roxpg = Factor("roxpg", ["mtzxp","tdgw","szz","asc","pjni","umob","vhrm"])
rpnreo = Factor("rpnreo", ["mtzxp","tdgw","szz","asc","pjni","umob","vhrm"])
def xyes(ush, roxpg, rpnreo):
     return roxpg == ush
def cfbw(ush, roxpg, rpnreo):
     return roxpg != ush and rpnreo == ush
def vod(ush, roxpg, rpnreo):
     return (not ush == roxpg) and (ush != rpnreo)
xhgsgi = Factor("mvsa", [DerivedLevel("znieko", WithinTrial(xyes, [ush, roxpg, rpnreo])), DerivedLevel("oyeh", WithinTrial(cfbw, [ush, roxpg, rpnreo])),DerivedLevel("fhn", WithinTrial(vod, [ush, roxpg, rpnreo]))])
### EXPERIMENT
design=[ush,roxpg,rpnreo,xhgsgi]
crossing=[xhgsgi]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)