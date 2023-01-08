from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qab1k=Factor("ZcVTYelGRDwiLI",['xXZuP2Q!j',"lndsygsw",Level("EsIV&NsehpG",3),'eHaDuiVxT_sN',"gm{mCNR","dFE3NILI",'uFs;GbsDPg~1'])
yu3jYky=Factor("IadPijzVwc8d",['Effa',"zDGDrLhpaCJ&9",Level("6xwBm|ciNVy",6),'UiG8vrx}dSX','KdfZeOlTmj',"W2CUuVxL",Level("fGz$pJYD",4)])

### EXPERIMENT
design=[qab1k,yu3jYky]
crossing=[qab1k,yu3jYky]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/7_2_1_0.csv"))
nr_factors=2
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/7_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)