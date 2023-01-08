from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_9AnDrA=Factor('YgtsvYET',["LX6wnk","ylO","6SyYjHVgKmk","BC~UhxQyIEw"])
aCl_z8=Factor("etcI",[Level('lxGOK',4),'opEjNb zCdxUu(',"pVcP)ui{l$w",'5[Q7PR'])

### EXPERIMENT
design=[_9AnDrA,aCl_z8]
crossing=[_9AnDrA,aCl_z8]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_0_0.csv"))
nr_factors=2
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)