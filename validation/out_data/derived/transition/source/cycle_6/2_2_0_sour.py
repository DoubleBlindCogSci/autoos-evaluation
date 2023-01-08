from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yqdhvs = Factor("yqdhvs", ["irtmze","ngco","qywt","nkzvpy","gkan","jufgk","noccgo"])
jfb = Factor("jfb", ["irtmze","ngco","qywt","nkzvpy","gkan","jufgk","noccgo"])
zepq = Factor("zepq", ["irtmze","ngco","qywt","nkzvpy","gkan","jufgk","noccgo"])
def bzh(yqdhvs, jfb, zepq):
    return yqdhvs[0] != jfb[-1] or yqdhvs[-1] != zepq[0]
def quvv(yqdhvs, jfb, zepq):
    return yqdhvs[0] == jfb[-1] and yqdhvs[-1] == zepq[0]
kwpbs = DerivedLevel("jhu", Transition(bzh, [yqdhvs, jfb, zepq]))
obwjl = DerivedLevel("fxycq", Transition(quvv, [yqdhvs, jfb, zepq]))
wyhxus = Factor("hsus", [kwpbs, obwjl])

### EXPERIMENT
design=[yqdhvs,jfb,zepq,wyhxus]
crossing=[wyhxus]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)