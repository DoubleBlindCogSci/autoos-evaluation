from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZC0qJ4Gjnt0=Factor('CL2s0kKLvg',['TFyBEilVx','afh D_<XaMM3]',"cFOHPxTuk",'Muil{O@^)SBZho',"iWWjWwCl"])
Jphsa8FV='hqFU1'
jakt7Oz2Eb=['cil4Xt','C! Yysz2wAXcq_',"zo7V4Qh",Level('IWDkJ',2),Jphsa8FV,Level("Gmor:2KO&Isd",1)]
OO_M7TdW=Factor("hACykAtr",jakt7Oz2Eb)

### EXPERIMENT
design=[ZC0qJ4Gjnt0,OO_M7TdW]
crossing=[ZC0qJ4Gjnt0,OO_M7TdW]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_1_0.csv"))
nr_factors=2
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)