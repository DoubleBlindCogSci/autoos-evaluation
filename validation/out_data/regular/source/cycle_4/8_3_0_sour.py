from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qilQGuEz="Mt<kW"
WcXkO_vcB_=['DtolflCM5fYCAH',"QPS2N",'4|w','vYf:','seJSMA%]f',qilQGuEz,Level(')CSgqmV:',4),'nmba','a6brMZG']
tePmiXs447W=Factor("TZ3xjZ",WcXkO_vcB_)
E7FzKS=Factor('8R6cXdnjV#X',['GW|aFAYOPC',"SYiCIPX","bow",'YVjSmyWA',Level('GWmycbs|iLn',3),"iKkfMFi{",'OTZRBVtp',']Gp;a'])
CrNUoOi=Factor('MmlzVP}o',['hUNKjllG<UP2Gb'," QgeiT7CLEEh","2ygr ZjMz&_DJ","ZgA&CIRN",'!TUHih','Amsfx<LUOm',"y:Q",'QbtPzLZ|['])

### EXPERIMENT
design=[tePmiXs447W,E7FzKS,CrNUoOi]
crossing=[tePmiXs447W,E7FzKS,CrNUoOi]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_3_0_0.csv"))
nr_factors=3
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)