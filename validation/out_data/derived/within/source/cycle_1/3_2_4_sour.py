from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
jbbsq = Factor("jbbsq", ["bkrmnn","rkkmd","sqjg","kbtst","cui","qmpf"])
xrdnu = Factor("xrdnu", ["bkrmnn","rkkmd","sqjg","kbtst","cui","qmpf"])
hyvj = Factor("hyvj", ["bkrmnn","rkkmd","sqjg","kbtst","cui","qmpf"])
def sdempl(jbbsq, xrdnu, hyvj):
     return jbbsq == xrdnu
def ovfyo(jbbsq, xrdnu, hyvj):
     return xrdnu != jbbsq and jbbsq == hyvj
def zkzjmn(jbbsq, xrdnu, hyvj):
     return (not jbbsq == xrdnu) and (not jbbsq == hyvj)
kpayf = Factor("wdd", [DerivedLevel("xvgc", WithinTrial(sdempl, [jbbsq, xrdnu, hyvj])), DerivedLevel("yfck", WithinTrial(ovfyo, [jbbsq, xrdnu, hyvj])),DerivedLevel("djnv", WithinTrial(zkzjmn, [jbbsq, xrdnu, hyvj]))])
### EXPERIMENT
design=[jbbsq,xrdnu,hyvj,kpayf]
crossing=[kpayf]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)