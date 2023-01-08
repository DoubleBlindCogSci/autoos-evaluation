from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vmuLJj3L5Gc=Factor('ZSZcLRq',['fMOJxSSSw','DnEDue','lpjjMcCa}UMY','QLkFpeZIA9L@l','CWR1VeFKirTP',"cJL0HWA iYB"])
U50NpUhTqiF=Factor("zwyiYIH",['fwMcoY',Level('P4SfSEsLSrhH',3),'oyM7KDBmamZZ>C',"WgPgcTONvkMcma","*alM(yoV9","txc|ozhjKAsI"])
gLVo=Factor("DpLReK7H k",['S&qUzgKe',"lJlO",'RSNR',"}YsEJH<PX[","dHExo}NFcyN",Level('OMjr',2)])
BAwualGWCP=Factor('klB&Y',["IgFxrb",'mGrVmr',"fJYSv","gVqAobUW","AjjHXwIXt",'vtplV:{'])

### EXPERIMENT
design=[vmuLJj3L5Gc,U50NpUhTqiF,gLVo,BAwualGWCP]
crossing=[vmuLJj3L5Gc,U50NpUhTqiF,gLVo,BAwualGWCP]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_4_0_0.csv"))
nr_factors=4
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_4_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)