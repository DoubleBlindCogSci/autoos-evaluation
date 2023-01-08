from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yemhmd = Factor("yemhmd", ["gygk","ikz","nwm","sycb","tbdjl","fexrc","njna"])
fhpxgk = Factor("fhpxgk", ["gygk","ikz","nwm","sycb","tbdjl","fexrc","njna"])
hbf = Factor("hbf", ["gygk","ikz","nwm","sycb","tbdjl","fexrc","njna"])
def gnidds(yemhmd, hbf, fhpxgk):
    return yemhmd[-3] != hbf[-2]
def ram(yemhmd, hbf, fhpxgk):
    return not (yemhmd[-3] != hbf[-2])
fjnik = DerivedLevel("ejfrf", Window(gnidds, [yemhmd, fhpxgk, hbf],4))
cfxgf = DerivedLevel("ytxwau", Window(ram, [yemhmd, fhpxgk, hbf],4))
jlhqr = Factor("xai", [fjnik, cfxgf])

### EXPERIMENT
design=[yemhmd,fhpxgk,hbf,jlhqr]
crossing=[jlhqr]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)