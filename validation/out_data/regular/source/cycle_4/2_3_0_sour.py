from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bsNGvyMr169=Factor("ELv",["HNLF",Level("chZk0hKWLDK",3)])
p9yUm3qi=Factor("Cg}|LDfzS3[M?",[Level('mlNItWvVzGZtfR',4),'vJj(;v'])
TEYRKKtHZ="jdq"
qkFOjXE=[TEYRKKtHZ,'bqbaUVrN]rM',"IyGgMQV{"]
yj_773ki=Factor('Y{ZN{rwKgeZkW',qkFOjXE)

### EXPERIMENT
design=[bsNGvyMr169,p9yUm3qi,yj_773ki]
crossing=[bsNGvyMr169,p9yUm3qi,yj_773ki]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_3_0_0.csv"))
nr_factors=3
nr_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)