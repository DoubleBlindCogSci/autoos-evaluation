from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
xmbiq = Factor("xmbiq", ["ztgrrw","xctwjz","thzl","tqd","ftwv","mlwv","xqojg"])
pap = Factor("pap", ["lnlw","qbvy","lcnfur","cgwsdi","chmye","uwwdtc","nvupej"])
def ccfoc(xmbiq, pap):
     return "xqojg" == xmbiq[-1] and not pap[-3] == "lcnfur"
def uxhfu(xmbiq, pap):
     return xmbiq[-1] != "xqojg" and  pap[-3] == "lcnfur"
def ddmy(xmbiq, pap):
     return (xmbiq[-1] != "xqojg") and (pap[-3] != "lcnfur")
yjwctr = DerivedLevel("zcp", Window(ccfoc, [xmbiq, pap],4))
gouv = DerivedLevel("mnoor", Window(uxhfu, [xmbiq, pap],4))
axyun = DerivedLevel("rhx", Window(ddmy, [xmbiq, pap],4))
nbjkdf = Factor("gas", [yjwctr, gouv, axyun])

### EXPERIMENT
design=[xmbiq,pap,nbjkdf]
crossing=[nbjkdf]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)