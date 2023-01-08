from sweetpea import *
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
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_3_0"))
### END