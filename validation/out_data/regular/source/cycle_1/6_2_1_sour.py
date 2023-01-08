from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
WDwD=Factor('bloeNR(c',["#Rii",'GQpeC$o','ocJEKsOBe',"GiAW>sQdc?t",Level('U E$vGK',8),Level('A@F2HAnyN',10)])
OztEEw=Factor("wg4Ig6",['aMbum:LO','_zD)BRcfYNI',"CQk^hOhaj)kot",Level('YgwAt',9),'#b;',Level('BYSfLRDmUOrCP',7)])

### EXPERIMENT
design=[WDwD,OztEEw]
crossing=[WDwD,OztEEw]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/6_2_1_0.csv"))
nr_factors=2
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/6_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)