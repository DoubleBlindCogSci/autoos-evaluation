from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
uxyjnj = Factor("uxyjnj", ["mzu","ygl","nhyooa","ngolyh","twszfx","sjw"])
scdrdp = Factor("scdrdp", ["inryki","dvjwud","lfta","yjalb","yhxucp"])
def zbojsr(uxyjnj, scdrdp):
    return uxyjnj[0] == "mzu" or scdrdp[-3] != "dvjwud"
def xbhn(uxyjnj,scdrdp):
    return not (uxyjnj[0] == "mzu") and not (scdrdp[-3] != "dvjwud")
acvqk = DerivedLevel("vjgv", Window(zbojsr, [uxyjnj, scdrdp],4))
vdnga = DerivedLevel("csj", Window(xbhn, [uxyjnj, scdrdp],4))
kni = Factor("bxaau", [acvqk, vdnga])

### EXPERIMENT
design=[uxyjnj,scdrdp,kni]
crossing=[kni]
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