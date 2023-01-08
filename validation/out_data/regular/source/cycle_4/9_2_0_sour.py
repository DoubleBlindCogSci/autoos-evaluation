from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
HfE5TQG=['eUXQY~UfK|hbdd',"vlaptPlbBJs6"," hk0?xV",'ymMw2JDzWDpRQm',"JqvgY}yQ1aF",'oxnvLAIdAey',Level("tLGjZGyva",2),"tfhpM{TBq"]
IHMB=['9O_rvODulBv3If',"IHVDXja","ZWZpJyrFha9O","@YwzMm5d"]
tIfy2ZKd9D1=Factor("xeT8sUVeZ",['x0jozyEr',"N ?x[i AC","C}eWW%UuhVy",HfE5TQG[4],Level("eHV",2),'J~odOQmitm','dzIh]EyV:ls1nI','H0CpB',IHMB[1],"oAt[QoOzW xm",'BJKUev4xH'])
aFtTJhbEl87=Factor("hF]y:l",["QzWHb<dLIKacrh",'woC%sL','kQQDyLn{o','s>2',"UK1q?",'cqZ8L}SZVT_O','eN51vNrQQ','zGT<yFyyNZ','AypcOqde'])

### EXPERIMENT
design=[tIfy2ZKd9D1,aFtTJhbEl87]
crossing=[tIfy2ZKd9D1,aFtTJhbEl87]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_2_0_0.csv"))
nr_factors=2
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)