from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oJo_y='StQzaAEqlYBcG'
RAUVKGo9RrX=['{cWC#}YpFdigjr',oJo_y,Level('mdIl!w VJKs',10),"ieUXsItNK^hDW",Level('_YY@y v7l$o&a;',7),"0VXhtnFpwwJfY<"]
jbcGrzS=Factor('oZiPQN',RAUVKGo9RrX)
ZWH1dA=Factor('HDj',[Level("x*C@ICLFE",5),"ckcq","Evukv(T)Sa7tqf",'(rUjEknVcvxXJ','0wKKm'])
B3xvbynqAhr=Factor("Pt nDbEd7{D",["^qmIavOLgtr","SuE","QIixsggv",Level('4b8_',2),"x;}r&yN<"])

### EXPERIMENT
design=[jbcGrzS,ZWH1dA,B3xvbynqAhr]
crossing=[jbcGrzS,ZWH1dA,B3xvbynqAhr]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_3_0_0.csv"))
nr_factors=3
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)