from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
biQo8=Factor("JPEeK bkk",['xekdk!qo1KXd',"uoRn",']s;LlOhKDh4nO',Level('dg[KbbqeYb',6),'JOPDSRc'])
SUTxR=Factor("FYdEXnj_hvR0",[Level("lvOntGk",3),'rPHWnDpjUUj','yOX ',"w4Hraly8rOCOt","Jplf&syKU"])
DbAo=[')oBbh(daJ6KS3','KeLIpuG GlY','UO>aKUuZXspP)F']
nWbupQoiJMW=Factor('AmUdvwcYmOEu',[Level('^ucgbDZUF8',1),Level('Wax*Rn',6),"jPrdx3>eh","LCxxI[gA",Level('g]DoKdSY',7),DbAo[2]])

### EXPERIMENT
design=[biQo8,SUTxR,nWbupQoiJMW]
crossing=[biQo8,SUTxR,nWbupQoiJMW]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/5_3_0_0.csv"))
nr_factors=3
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/5_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)