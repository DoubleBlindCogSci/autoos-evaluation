from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
phpbdt = Factor("phpbdt", ["xmibby","kvd","uwwtg","mdo","zlfa","ctg"])
def mvaq(phpbdt):
     return phpbdt[-2] == "kvd" and not phpbdt[-1] == "kvd"
def gkuhf(phpbdt):
     return not "kvd" == phpbdt[-2] and  "zlfa" == phpbdt[-1]
def vxa(phpbdt):
     return (not mvaq(phpbdt)) and (not gkuhf(phpbdt))
ljyeu = DerivedLevel("lsy", Window(mvaq, [phpbdt],3))
sgwv = DerivedLevel("fxiti", Window(gkuhf, [phpbdt],3))
frmgfa = DerivedLevel("aydm", Window(vxa, [phpbdt],3))
fegh = Factor("jkfrap", [ljyeu, sgwv, frmgfa])

### EXPERIMENT
design=[phpbdt,fegh]
crossing=[fegh]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_2_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)