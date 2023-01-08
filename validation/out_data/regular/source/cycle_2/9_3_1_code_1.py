from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
WVUt9jHM=Factor('ozndzP~R',["#buNacuy",Level('YNiQCbujIRl',6),'>Ab',"lH]tGfO*wAk8kQ",Level("ZVS:",2),'Splvlo',"|a*hCPDN","cER",Level('bhxspM&TUbgo',1)])
uaSOQA=["^oBET",Level("FdPdt(",9),"!izZ3EwlEi","Ld Cf",']%%EEHYA','#4n@rSWwmV',Level("IyMEQBIp",6)]
X41tdNjt9=[Level("DUigxkR]3ACJW",1),'SOVSBYqSjXUi',':hZc2gJoUG',"Elq","j;E","]RuF>JdytuDGZ",uaSOQA[2],"pgG",'pAp',"uOuNm#KYEOg7KR"]
f1kwp_8dx=Factor('aIRsfp;r0FH',X41tdNjt9)
PgYBtN=Factor('rrCuzg',["VtoEgmqSUjXZo",Level('ibii8kH',3),"l3f",Level('s2uX',10),'swRxu|NZbmy&c','YMQ#','GlrG',"oJneQnjMU4#f",'I%KCddz BO'])

### EXPERIMENT
design=[WVUt9jHM,f1kwp_8dx,PgYBtN]
crossing=[WVUt9jHM,f1kwp_8dx,PgYBtN]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_3_1"))
### END