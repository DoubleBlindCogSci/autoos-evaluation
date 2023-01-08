from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
RAqI=Factor("ScY",[Level('kvzBaS9p',2),"2xNBOUjVPlN","pkZPC<hdr",'?BpoR','LBiAoA$fZbCv',"nDKyhot","s_ofo",'haD0euQ',"uNwxfRC"])
vQp6Wb=Level('oJf#N',1)
wdx9OoQVc=[vQp6Wb,"GY2AXx[*",'^uQ}gRj','YmTZuAu',"0voYsEWkjXCB",'bXB%GKCW',"QiyzS6",'p4izJliG',"B65",'iehc']
zsEB=Factor("EOOJTns5VdPxM",wdx9OoQVc)
TbdVKaXml=Level("rifENTgudZ",1)
Je67HtX5=['srHT','GHyUECmTKDKN','rN pex',"4BEbAVO",'Bn@wDLlZA','GDO','qc2KMQkxL7',Level("0qnEZKMkJ",4),TbdVKaXml,'r2KTgU']
YoQBeyJ=Factor("d9u",Je67HtX5)

### EXPERIMENT
design=[RAqI,zsEB,YoQBeyJ]
crossing=[RAqI,zsEB,YoQBeyJ]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_3_1"))
### END