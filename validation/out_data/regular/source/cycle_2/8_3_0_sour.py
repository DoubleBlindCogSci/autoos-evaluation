from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
EJatN='JOenoqcb2Mo'
kICX8R=Factor("[DRl@cVPj%",[Level('gJvZ',3),EJatN,Level('gDcj0rCJ!',4),"MnoNqtDHfdxn",Level("UrzOLBabJDku",1),'SqtIfU',Level('UuHfqfKtmK',8),'ahZdO]','kEbZmKzeC'])
Fkoh6v=Factor('CmL~cLxZ',['qDu4qRtw',Level('QOHdZu*wwL;gG',4),Level("DDOu",6),'XxQCLYRWKEyal',"dAst","t>VxQncProzoN",'Gbani',Level('SRnwIoCbpBHHeh',1)])
X5g9ftRb=Factor('YzQW',[Level('(NocRPqp3j',2),Level("Y]q3Vbr",6),"tAlGiEtlmUrakW","P}Ra@juLhouF","iEwzJYTYC","J!rcIIN(RzG!K","N_$VI","yyy"])

### EXPERIMENT
design=[kICX8R,Fkoh6v,X5g9ftRb]
crossing=[kICX8R,Fkoh6v,X5g9ftRb]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)