from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
geucEiq7=Factor('ya$',["h#jzak",Level('Fu(mYYzc!eD4E<',3),"LNcGLxIdFrSv",'OzX%OfsRWx9kly','YCN',Level('snCkYKFVta',10)])
q7ysU=["KTeTuHou*aO","@JNE",'WeknS~Y',"DjFrBW}pjHvW",'DdOx1XLCCU',Level("zPQQn",4)]
Ghe6WQ=Factor("aKuYu*ercSL",q7ysU)

### EXPERIMENT
design=[geucEiq7,Ghe6WQ]
crossing=[geucEiq7,Ghe6WQ]
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