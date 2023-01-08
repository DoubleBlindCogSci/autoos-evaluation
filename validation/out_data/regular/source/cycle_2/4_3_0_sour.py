from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tY_yFIsHZOb=[Level('CNgNhGHCCZHip',10),'kFEKuvBWnTg?3c',Level("YtThQKPVniM~",8),"Aq#{UhDtH"]
hQkbk=Factor('ZPWrVc',tY_yFIsHZOb)
VnLqZ='VQPBA'
OyOeSLNvG=Factor('eqGmUptsi',["oC7Sfpibdy",VnLqZ,Level('tJRJlVUb~yL',7),'VNZNo0p',"RBL5P?dedH"])
Y4ZebIu23=Factor("v}Vy",["2hy>",'MHU',Level('UwsYZMnPe',4),Level('ZMLL#T',2)])

### EXPERIMENT
design=[hQkbk,OyOeSLNvG,Y4ZebIu23]
crossing=[hQkbk,OyOeSLNvG,Y4ZebIu23]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_3_0_0.csv"))
nr_factors=3
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)