from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wCitXyGU=Factor('gEA',[Level('GFaS0QA%gdsbWv',4),">UlJw","KL;yCKXPWgC?",Level("hecoSTDmd] VO",2),"RDmXG%O",'xIKE>heId','TWY(','exmdZoQ','uwGfZW;9r?Ko'])
yoap1Pl=Factor("(XOHTPtuI<du",[Level("PvDxbWU%URnODy",3),'hTVnnhiugkZ_EX','iyybcjPOq',"Szic!_A[bjvjs","rgaqZS","QZZVtoeXgyainT","RgZ_jAzDX",'WHYEWymX',"_ALziiuF"])

### EXPERIMENT
design=[wCitXyGU,yoap1Pl]
crossing=[wCitXyGU,yoap1Pl]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_2_1_0.csv"))
nr_factors=2
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)