from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
rtnhuu = Factor("rtnhuu", ["qaplpa","xrxe","iiz","mmack","nif","rnwtsk"])
tabde = Factor("tabde", ["ufjmg","elr","rwngi","qsttxo","iuxn","btxr","oue","lbx"])
def lrvbo(rtnhuu, tabde):
     return "xrxe" == rtnhuu
def hnkj(rtnhuu, tabde):
     return rtnhuu != "xrxe" and  tabde == "oue"
def rbcp(rtnhuu, tabde):
     return (not rtnhuu == "xrxe") and (not tabde == "oue")
jeyb = DerivedLevel("totap", WithinTrial(lrvbo, [rtnhuu, tabde]))
fuc = DerivedLevel("pebd", WithinTrial(hnkj, [rtnhuu, tabde]))
bsyaea = DerivedLevel("jaut", WithinTrial(rbcp, [rtnhuu, tabde]))
ednt = Factor("lpqj", [jeyb, fuc, bsyaea])

### EXPERIMENT
design=[rtnhuu,tabde,ednt]
crossing=[ednt]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)