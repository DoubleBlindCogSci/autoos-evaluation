from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wnt4p="fTGxLOrXBBhg"
zq_E='Tg}J#Tu'
RVG66926=["ThvR >Zq*moZI"," bsoVKrY?vCP",'pTTS_Cm!|fF',Level("X[fYi5Y",4),'bLQNt','jZCE|M',"lhKZ2"]
pTNrGeQ=Factor('vlaGqWn9o',["QExdHPz",'PxuyEyg',RVG66926[2],zq_E,wnt4p,'AJGXdOyf@ZT','gjQsiXe}npsSB',":kwFkKaYA#^j",Level("]mSaanhOy?GJg",3)])
O6up8C="2QD}PUXxzDy)"
B9W6NPnuQ=["9KwN(~[a T~mM",O6up8C,'AR?UqJjF$A1mT8','2qG(I',"zcyOnK","Gczy","LfhTXQrFnc"]
hJR4xY=Factor("XnN}xX|NLRvh",B9W6NPnuQ)

### EXPERIMENT
design=[pTNrGeQ,hJR4xY]
crossing=[pTNrGeQ,hJR4xY]
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