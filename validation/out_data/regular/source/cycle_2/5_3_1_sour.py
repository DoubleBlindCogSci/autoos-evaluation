from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
GltTj47f0=["YzORK#Ylmpt",Level("kuO",7),Level("OaeQ!<GD2Hy",8),'PpMgMBMfTS','0ZwYyryh:Q6n']
mfAl5NlQ8=Factor("ZjRrH?",GltTj47f0)
b7BOq=Factor("Ql9PKY",[Level("QcmrORhdIb",6),Level(";#Gd",3),"GaTNPTp",'Nv#L^cxIB',"iXeRZYLa"])
NYucU=['pAf','Zc rtq;rscX',Level('lbhA&_(&Mz[',8),'zZTBiFQm',Level("pUwc",4)]
vtouic=Factor("VWCMH?L",NYucU)

### EXPERIMENT
design=[mfAl5NlQ8,b7BOq,vtouic]
crossing=[mfAl5NlQ8,b7BOq,vtouic]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_3_1_0.csv"))
nr_factors=3
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)