from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lMvkinK=Factor("sLRSmrw~wog",["JusJqs2B2z",'BLQjTh',';CElSNCU',"ZxEvrF"])
DTS5Sdi="mHeP:rTHbt"
DJ1VZX='rwLHf'
r5xFAZG1=[DTS5Sdi,"~efWGJ",'ZLXzE(0 T?q',"e{!VchU8",'HIXEsBPUdXuUON',DJ1VZX]
NBtS=Factor('wEcCabp*bARhA',r5xFAZG1)
l5tij5jE7i3=Factor("W;CkWTrgStL",['gMfiFPym~VMigr','Q;FEmr?ErxTmy',"I[gQ",'#Me@PasrN'])

### EXPERIMENT
design=[lMvkinK,NBtS,l5tij5jE7i3]
crossing=[lMvkinK,NBtS,l5tij5jE7i3]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_3_1_0.csv"))
nr_factors=3
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)