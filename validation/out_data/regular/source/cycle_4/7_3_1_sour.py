from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
NK3Rb3lw0='5mJmPVI'
JJA8TFHo=[Level("upXMuXEIj>t^",2),"QTggMR",'WEEY%CoE','$tkA',"NQi",Level('BIBZv',4),'ZAUExL(',"bS1FNxDg"]
a4mF8=Factor("ydAaf6#dCAAz",["dLwZ(YH",JJA8TFHo[3],"j#7wTVQ","OHh",NK3Rb3lw0,'YSsn;oH',')lU)tFtt',"2Fgxhis%","t2Wd"])
AryDl2eChY7=Factor("et#V",['GSxn}','7Kg~%$WRzC',')GMEvtmlLGd','dCZUVRH','kYuq',"EJSMu?v9a","dB4"])
pa_HLB9Dc8L="X b}U"
yCrRhLF=Factor("bmWCjFbSVw[ i]",['GXUYg!<','GRG a0','H?tHHF',"ubwsNtUe1yTh",'zoHJ5ovOzW','hvIEVubmJ7',Level('PslhR;&',2),pa_HLB9Dc8L])

### EXPERIMENT
design=[a4mF8,AryDl2eChY7,yCrRhLF]
crossing=[a4mF8,AryDl2eChY7,yCrRhLF]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_3_1_0.csv"))
nr_factors=3
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)