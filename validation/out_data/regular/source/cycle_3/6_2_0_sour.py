from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
snqKMoKbnHg="LfMk7F2"
mDgHC=Factor('aW5XF^Ppl',['CtY',"y2HTrxgQOIGf",snqKMoKbnHg,'D&OxumH>',Level("giokp",5),'lwOE',Level("wp)!M",10)])
ORZfTh=["Gpkk)Z1 c"]
Z4g9CUQo2=["_v0K p6SrNn",ORZfTh[0],"FCw","ImRK",'hklgw',"@fJ",Level('>rEEKoL9{Wd',1)]
l_tbBWNhm=Factor('s;^ttxWvCB',Z4g9CUQo2)

### EXPERIMENT
design=[mDgHC,l_tbBWNhm]
crossing=[mDgHC,l_tbBWNhm]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_2_0_0.csv"))
nr_factors=2
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)