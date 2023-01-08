from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
dbco = Factor("dbco", ["hzkwtm","feme","vfv","meulmi","tjtd","xfiqt","qryxq","ivbakq"])
ftoy = Factor("ftoy", ["hzkwtm","feme","vfv","meulmi","tjtd","xfiqt","qryxq","ivbakq"])
sfquoi = Factor("sfquoi", ["hzkwtm","feme","vfv","meulmi","tjtd","xfiqt","qryxq","ivbakq"])
def ugbok(dbco, sfquoi, ftoy):
     return sfquoi == dbco
def msaed(dbco, sfquoi, ftoy):
     return sfquoi != dbco and dbco == ftoy
def gwg(dbco, sfquoi, ftoy):
     return (dbco != sfquoi) and (dbco != ftoy)
ardz = DerivedLevel("kgusrl", WithinTrial(ugbok, [dbco, ftoy, sfquoi]))
cdovtg = DerivedLevel("jtdph", WithinTrial(msaed, [dbco, ftoy, sfquoi]))
ffolrn = DerivedLevel("akj", WithinTrial(gwg, [dbco, ftoy, sfquoi]))
wvtra = Factor("itd", [ardz, cdovtg, ffolrn])

### EXPERIMENT
design=[dbco,ftoy,sfquoi,wvtra]
crossing=[wvtra]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)