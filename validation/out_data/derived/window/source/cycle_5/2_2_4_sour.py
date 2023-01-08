from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dctt = Factor("dctt", ["bguc","fojt","lte","oiq","ivyk","aezr"])
zftfq = Factor("zftfq", ["tkrv","rktx","kpf","ssf","wllw","vohs"])
def uqhxhw(dctt, zftfq):
    return dctt[-2] != "oiq" or zftfq[0] == "tkrv"
def fnt(dctt,zftfq):
    return not (dctt[-2] != "oiq") and not (zftfq[0] == "tkrv")
mlq = DerivedLevel("uuov", Window(uqhxhw, [dctt, zftfq],3))
zgfi = DerivedLevel("npy", Window(fnt, [dctt, zftfq],3))
ypl = Factor("ibcdmx", [mlq, zgfi])

### EXPERIMENT
design=[dctt,zftfq,ypl]
crossing=[ypl]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)