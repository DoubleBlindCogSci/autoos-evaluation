from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
d2g1q='ZxrHgV'
_f9AL0l2=Factor('Nu9hsR7)QRVyT',["XKlO:PTn",'iI)Jf2',"XALFi~H%HMIkby",'HVrd6cQVJP',d2g1q,"ndXyv",Level('?ZBCNvSe',6),'APKM#d','e8PrYt{v%JH *D'])
wrLypab=Factor("W!cIisM8FtnMmD",[Level('~BBHICUcD',7),"kScn0s","KypU",Level("<VVbyuZ4or",6),Level('BAfAY@ct)KUy',1),Level("ckxe3",3),'BfZFF',"ZKiVYkip"])

### EXPERIMENT
design=[_f9AL0l2,wrLypab]
crossing=[_f9AL0l2,wrLypab]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_2_1_0.csv"))
nr_factors=2
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)