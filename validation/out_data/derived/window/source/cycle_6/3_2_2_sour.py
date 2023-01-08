from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mch = Factor("mch", ["qcorlu","iufm","uqj","vba","cid","wdpce"])
yno = Factor("yno", ["mfzqrp","sqaa","lgpdao","pkosa","oyid","wtitea","kzgaih"])
def fgdj(mch, yno):
     return "cid" == mch[-1] and not yno[-2] == "wtitea"
def qrevi(mch, yno):
     return "cid" != mch[-1] and  yno[-2] == "wtitea"
def jir(mch, yno):
     return (mch[-1] != "cid") and (not yno[-2] == "wtitea")
anel = Factor("rlxwtt", [DerivedLevel("yrk", Window(fgdj, [mch, yno],3)), DerivedLevel("uvv", Window(qrevi, [mch, yno],3)),DerivedLevel("hgdxmx", Window(jir, [mch, yno],3))])
### EXPERIMENT
design=[mch,yno,anel]
crossing=[anel]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)