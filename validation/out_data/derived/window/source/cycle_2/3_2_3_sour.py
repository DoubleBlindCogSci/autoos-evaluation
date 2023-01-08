from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
llppou = Factor("llppou", ["kwx","vpznh","cacm","pmvgq","rromj","wnvo"])
buff = Factor("buff", ["mtp","tegfon","rawjzc","ganf","cgukfq","gbjs","llq","qmkzto"])
def ydd(llppou, buff):
     return "pmvgq" == llppou[0] and not buff[-1] == "rawjzc"
def drf(llppou, buff):
     return "pmvgq" != llppou[0] and  buff[-1] == "rawjzc"
def wnsdrx(llppou, buff):
     return (not ydd(llppou, buff)) and (not drf(llppou, buff))
pbjt = DerivedLevel("odx", Window(ydd, [llppou, buff],2))
wdyckx = DerivedLevel("eqe", Window(drf, [llppou, buff],2))
cdk = DerivedLevel("qygv", Window(wnsdrx, [llppou, buff],2))
mpe = Factor("jwu", [pbjt, wdyckx, cdk])

### EXPERIMENT
design=[llppou,buff,mpe]
crossing=[mpe]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)