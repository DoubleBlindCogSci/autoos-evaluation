from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
g9DfKoc3=['YoYMAfDGWCod','mj*khW(seuB0Mp','IRZO68p~iOeXU',"CSkbjp?E",Level("NXasskD|L",3),'kv{EgJta{Qt',"2oe9",Level("rOjFiahJWANwA",4)]
lb4EG_=Factor('vtYW<WZFqFRj',g9DfKoc3)
agy1uU8V=Factor(")FhOKmtzJr",["Fz|wopq","KoMHGEg",'Ik)U','rL%a','c$i',"IXZo@Sh","m;UFo:R",'qyy1R'])

### EXPERIMENT
design=[lb4EG_,agy1uU8V]
crossing=[lb4EG_,agy1uU8V]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_2_0_0.csv"))
nr_factors=2
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)