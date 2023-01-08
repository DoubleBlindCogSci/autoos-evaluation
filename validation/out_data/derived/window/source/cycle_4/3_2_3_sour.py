from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rwrsdm = Factor("rwrsdm", ["aces","wra","fmka","yel","asnf","toojjb","tzjfni"])
rxykvf = Factor("rxykvf", ["aces","wra","fmka","yel","asnf","toojjb","tzjfni"])
vmyy = Factor("vmyy", ["aces","wra","fmka","yel","asnf","toojjb","tzjfni"])
def ykfx(rwrsdm, rxykvf, vmyy):
     return rxykvf[-3] == rwrsdm[-1] and rwrsdm[-3] != vmyy[-1]
def zjd(rwrsdm, rxykvf, vmyy):
     return rxykvf[-3] != rwrsdm[-1] and vmyy[-1] == rwrsdm[-3]
def psoh(rwrsdm, rxykvf, vmyy):
     return (not ykfx(rwrsdm, rxykvf, vmyy)) and (not rwrsdm[-3] == vmyy[-1])
ukbc = Factor("dzcim", [DerivedLevel("qsaeu", Window(ykfx, [rwrsdm, rxykvf, vmyy],4)), DerivedLevel("ehbbeo", Window(zjd, [rwrsdm, rxykvf, vmyy],4)),DerivedLevel("lec", Window(psoh, [rwrsdm, rxykvf, vmyy],4))])
### EXPERIMENT
design=[rwrsdm,rxykvf,vmyy,ukbc]
crossing=[ukbc]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)