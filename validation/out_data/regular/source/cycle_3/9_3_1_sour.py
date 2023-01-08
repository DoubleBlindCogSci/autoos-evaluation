from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
o9CIQ=Factor('GSScI~jmaWctYX',[Level('tTwoWeFW',6),Level('J rI',3),"b;jWYhx(d(6f0a",Level('E$hF',10),"qiW^xUhfBQSp",' YSRGOP','X9J','teg[IfqrC',"wn~f*fAcLsXHoB"])
LQ6I85=['WwSc','vFG 3gsAz',Level('mDQPJMeH',8),Level('Ntw',3),'#|ijl9urNLDTt',"TvJFdCQLTK",'uoVl','LI2wpgDLviRhp',Level('EYWswGzPq',8)]
WmKIypq45=Factor("QG GSw|WnW@Z",LQ6I85)
TvtdLMRA=Factor('a2v|l!LvXU_)uj',['kYReKIDGfJ9TPP',"NJAdmPAJXQhVX","C$dEmqmYfta;so",'fo[RQpd','kbQGPTj',"ln|3|MZWbx","PljT)F",') Te(E~GeB','WFsTwhS'])

### EXPERIMENT
design=[o9CIQ,WmKIypq45,TvtdLMRA]
crossing=[o9CIQ,WmKIypq45,TvtdLMRA]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_3_1_0.csv"))
nr_factors=3
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)