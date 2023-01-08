from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yxskru = Factor("yxskru", ["dlljcl","vrfb","wuhu","wuo","zhwffj","cyv","eougmo"])
xwdi = Factor("xwdi", ["dlljcl","vrfb","wuhu","wuo","zhwffj","cyv","eougmo"])
ybzis = Factor("ybzis", ["dlljcl","vrfb","wuhu","wuo","zhwffj","cyv","eougmo"])
def rish(yxskru, ybzis, xwdi):
     return yxskru[0] == ybzis[-1] and yxskru[-1] != xwdi[0]
def xyep(yxskru, ybzis, xwdi):
     return ybzis[-1] != yxskru[0] and yxskru[-1] == xwdi[0]
def crf(yxskru, ybzis, xwdi):
     return (not rish(yxskru, ybzis, xwdi)) and (not yxskru[-1] == xwdi[0])
wdduca = DerivedLevel("jtwgjn", Transition(rish, [yxskru, xwdi, ybzis]))
thayor = DerivedLevel("hjzs", Transition(xyep, [yxskru, xwdi, ybzis]))
mmvgjj = DerivedLevel("gnrwj", Transition(crf, [yxskru, xwdi, ybzis]))
uooi = Factor("keh", [wdduca, thayor, mmvgjj])

### EXPERIMENT
design=[yxskru,xwdi,ybzis,uooi]
crossing=[uooi]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)