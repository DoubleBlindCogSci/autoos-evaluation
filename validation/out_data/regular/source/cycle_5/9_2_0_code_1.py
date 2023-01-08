from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
o_gjYTxPb='<iwy}pnKP8'
DFFAFcAIrJ=['IHCmSJdC}zeC',Level('MA0YAZ 9ODft',2),Level("FAFAYrA1u|I",3),"ocwU!Twxuzfb",'wwTPgoo','Q]*zLlDSt',Level('a{bY%MZCIQpMDh',1),Level("GIHDEImSQxS",2)]
Ac26Xaf_QB=Factor("foBeAcVgYj2",['vjVFCEItOwt',"cDYFfFf",o_gjYTxPb,"mGf6Gxpv",'XNxbH',"Di6KYmIB","RjOE",'{GMlV3Dr','YYO?fvNTPWQ',Level('SVcgp)Nax',3),DFFAFcAIrJ[3]])
GP1ysx=Factor("PyzP",["mFDTa",'opoKtKkNvzhj',"JhDjc0_g","odIFPim}ZXvC",'Sqo<KujF}',"QG}HqG[ER7",'gergxGLBPT7IV','AXcg3E~yxM','Lttv'])

### EXPERIMENT
design=[Ac26Xaf_QB,GP1ysx]
crossing=[Ac26Xaf_QB,GP1ysx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_2_0"))
### END