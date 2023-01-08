from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
YJJ7RTs=Factor('EZJJ(VpVz7wUQ',['yJYk3K','MKjjJD3r'])
SxDK=['{NrQk)Sy',Level("#EZV",10)]
oJMM8yfh=Factor('PZ}n1',SxDK)
nJdlJyOBm2=Factor('jmhDcwuB|Xs',["Y eGKV*W",'KwO>F'])

### EXPERIMENT
design=[YJJ7RTs,oJMM8yfh,nJdlJyOBm2]
crossing=[YJJ7RTs,oJMM8yfh,nJdlJyOBm2]
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