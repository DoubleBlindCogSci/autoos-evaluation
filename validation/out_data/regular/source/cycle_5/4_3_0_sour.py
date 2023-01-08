from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZstPRIse=Factor('atISnwmWtks',['QvV','_rlRsmAg{Q','IqQAAQL','l^Lh[Bnhx'])
q3PXwtecpj=Level("FNDNa",2)
Uh1mUJCIu=['0Jme',"t@HHhyQevS","*ZCwL?{KQogs",q3PXwtecpj,"Sx]uz~q4Nb"]
iOHm2wUxBT=Factor('oO XCRR',Uh1mUJCIu)
Swxuu=Factor('IyVpmnqGLUUB',[Level("BxKKPj;_gcUL",3)," ioqk","S]cvEsXQuTp",Level('qwDo BfKJXI',3)])

### EXPERIMENT
design=[ZstPRIse,iOHm2wUxBT,Swxuu]
crossing=[ZstPRIse,iOHm2wUxBT,Swxuu]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)