from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
DaolP=Factor("mcR",['Mzssd_TXadY','weZOt v<{t',"gFryDiDbE1(aPH",Level("EKm",2),"*YCeDx"])
HXZ8='VWB~wR|S'
EfYq=['anmNZzGN','thussgpEZkkZg',HXZ8,'OPHshJj1Tu)5FF',"vPD","edl&iqq"]
M43mWPZ=Factor('{SsqUA',EfYq)
b7xu90fA=Factor('3!_;XuNGFqGov',['oYJf0aLP(','W_9DZ_ixjQd','qFn*q2FZW6NiV',Level('KWHKDtNR',2),'TX4'])
E2XOvAX=Factor("WzqR3",["RgCOfRe",'TEoHoo_EIR',"frHviA@FbvtiQ","sQ#AYwsY",'wiPL'])

### EXPERIMENT
design=[DaolP,M43mWPZ,b7xu90fA,E2XOvAX]
crossing=[DaolP,M43mWPZ,b7xu90fA,E2XOvAX]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_4_0_0.csv"))
nr_factors=4
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_4_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)