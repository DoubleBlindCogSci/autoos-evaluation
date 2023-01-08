from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jkoa = Factor("jkoa", ["dty","jip","fdhyva","rdrtvh","mrvqki","yip","qhfeku","aao"])
def emfv(jkoa):
     return jkoa[0] == "dty" and not jkoa[-1] == "dty"
def edxcez(jkoa):
     return not "dty" == jkoa[0] and  jkoa[-1] == "rdrtvh"
def rub(jkoa):
     return (not jkoa[0] == "dty") and (not edxcez(jkoa))
oil = DerivedLevel("cwq", Window(emfv, [jkoa],2))
esa = DerivedLevel("uworl", Window(edxcez, [jkoa],2))
btphh = DerivedLevel("xvza", Window(rub, [jkoa],2))
wqa = Factor("rvuld", [oil, esa, btphh])

### EXPERIMENT
design=[jkoa,wqa]
crossing=[wqa]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_3_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)