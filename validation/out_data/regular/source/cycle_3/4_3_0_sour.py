from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
AtdO1GnKzF2=[Level("KcW2ZxggE",4),"QBj;_x",'eUB6*Apaft','}OrlEdVL',"dvAL",Level('r f<DtUg{ZNQ',2),Level('nBfilTtc&$M',6)]
ZXZ_Zbz=Factor("w]wKEQfjtuL",[AtdO1GnKzF2[4],"qU)P","nHGLbkYRAT","iFUGatGZaeVYjl",Level('ejdSnrjVVeqh',8)])
RdD7Gj=Factor("C4krZwd",['Jhlf#sDUj','?hQrS',Level("RuRJCC",6),Level("vuzr",1)])
nnv1Z=Factor('EFRWROtJQG',["LKFVp;8MzDY8F","KPZRhqX",'Kh{fGMvOjo(Rw','bjJNM%rv'])

### EXPERIMENT
design=[ZXZ_Zbz,RdD7Gj,nnv1Z]
crossing=[ZXZ_Zbz,RdD7Gj,nnv1Z]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_3_0_0.csv"))
nr_factors=3
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)