from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jAMzLKub13='NmjVDdgzkkAh'
VqEcbTgz0=Factor('T2hdyKWgNx#aq',['ivFHOCJEx)qy#','a07IdQAQRf',"DRdH nBIO",'<kl#?JvIE#G',"naOZmdGA",Level('%oxVxiI(',1),jAMzLKub13])
ElGn=Level('Y]nhb5joP',2)
Yc73P=Factor('FwK2y^l CGt;U',[Level("DOxJnlZahqkFT",2),"DzXgDP(lo",'ruD}CjaBOIqy','!SqbozoR',ElGn,"qBet1kqGlKW",'l4|IHhKDSk'])

### EXPERIMENT
design=[VqEcbTgz0,Yc73P]
crossing=[VqEcbTgz0,Yc73P]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_2_1_0.csv"))
nr_factors=2
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)