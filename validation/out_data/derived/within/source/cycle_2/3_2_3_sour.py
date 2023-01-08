from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
ohixrc = Factor("ohixrc", ["vmna","bszyfq","prscsd","ecy","jiku","yfnk","njjxli"])
dyt = Factor("dyt", ["vmna","bszyfq","prscsd","ecy","jiku","yfnk","njjxli"])
pef = Factor("pef", ["vmna","bszyfq","prscsd","ecy","jiku","yfnk","njjxli"])
def bzbppw(ohixrc, pef, dyt):
     return pef == ohixrc
def liaab(ohixrc, pef, dyt):
     return pef != ohixrc and ohixrc == dyt
def phj(ohixrc, pef, dyt):
     return (not ohixrc == pef) and (ohixrc != dyt)
qilxs = Factor("zfoyvj", [DerivedLevel("lqk", WithinTrial(bzbppw, [ohixrc, dyt, pef])), DerivedLevel("skpe", WithinTrial(liaab, [ohixrc, dyt, pef])),DerivedLevel("yudp", WithinTrial(phj, [ohixrc, dyt, pef]))])
### EXPERIMENT
design=[ohixrc,dyt,pef,qilxs]
crossing=[qilxs]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)