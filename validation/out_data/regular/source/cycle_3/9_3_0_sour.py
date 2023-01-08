from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jKzX=Factor('UHiOjqnbU',[Level('rp1lOL#evEP3x',7),Level('T]Tjhxzd~',2),'hGqjd?wPSNcdq',"znsmPHpfA","^f;!","oE]lhEJxf",Level('lVUpk',1),'hJBMJ|g',"AJbGE"])
sahk4ycA3V='VMyuf}:$TQW'
AFJogAp=["BJSEyvvX","OkJ{O",Level('_QsjOpSwu(',2),'PpzE#N99U^RSMB','FnUpZw5aO%',Level('FfMi',7),'I%n',sahk4ycA3V,'YWy&]',Level('xKWkchXMInY',2)]
GrXPfeSP6=Factor("NjyastzmSRtAD",AFJogAp)
cHmXM7=Factor('HpsJeGNB',['8WM)BAZKaV',"&OfvK{",Level("TYZ",7),"Vz3X3yXZcA",'i_B',"DEAFokd",Level("wZJuZQSMLLOrgt",1),'CYwOs e]Rb','|k9z WS*VG~'])

### EXPERIMENT
design=[jKzX,GrXPfeSP6,cHmXM7]
crossing=[jKzX,GrXPfeSP6,cHmXM7]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_3_0_0.csv"))
nr_factors=3
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)