from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xmPXCagiE=Factor("kPX",["RIXHSCRm]&w9",'BAv@xW'])
AvV0v1G_x=Factor("Sg_",["zA7UZgVJKR","wrMNGFRkex"])
jBZuftztcvq=Factor('Wd68D',['AxgIH','aiFdCWzYlwNNK'])

### EXPERIMENT
design=[xmPXCagiE,AvV0v1G_x,jBZuftztcvq]
crossing=[xmPXCagiE,AvV0v1G_x,jBZuftztcvq]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_3_1_0.csv"))
nr_factors=3
nr_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)