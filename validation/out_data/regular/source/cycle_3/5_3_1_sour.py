from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
X4gcOb=Factor('rywp9s)B;pNz',["ol1SNL>urpCs",'ToZiajcDY;L','U?HanBxlgxiyg','SnZvzhVuD','[ZSxI0yW '])
dcOwd6AU7a0='XcrrEEQ&dzWJ~'
ecf5=Level(" nd1 wXhC]^H",7)
CfA2j=Factor('D1ZpVNQD',[ecf5,"~sKt_K[|",Level("LQSA1zljHPc",2),dcOwd6AU7a0,Level('WcGk',9),Level('Yp(RKdbeg',6),'psxeRCdwbOqyo'])
u2hHDxYBX0=Factor('W<bOaSC',["[V&jJVtYY","qtW",'w{U^N2Y(G',"wFHo",'mSNIXej*eKdjKD'])

### EXPERIMENT
design=[X4gcOb,CfA2j,u2hHDxYBX0]
crossing=[X4gcOb,CfA2j,u2hHDxYBX0]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_3_1_0.csv"))
nr_factors=3
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)