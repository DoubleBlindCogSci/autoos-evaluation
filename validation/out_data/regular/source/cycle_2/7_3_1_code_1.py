from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fGWM2=["6uVQ",'HTYhhc',"XekN|beDN","ZzeQLqLFBozjjF",Level("ONf}Lot4",1)]
bZTlT4UO=Factor("VZL!$ Vj",['TyczWs8',"]or]k#p",")zHA)",fGWM2[0],'cCHSycd# CQfS',"gCQCfXMhjB(NLd",'ZUENJhUtLPJ',"#[mhe"])
ReYpIt0NAFU=['L^yDtUn',"jSpcW",'a5_UWzvD','Ecu',"gilfzxyVLQ&I"]
PyJu=[ReYpIt0NAFU[3],'rcAzdoxEGV',Level("YX!",6),' &rhUDiOF','GNHHGXCczh%N','E#Syqf)JmkU',"Lrl",'VWfRuI']
saqGRH5=Factor("RpRpPYMpS",PyJu)
DlPCT_VM=Level('Jx<aDX',6)
UgZDhUR3ZJ4='KHp)icMSJN'
wiGDC40=Factor("wOGTqUJVF",[UgZDhUR3ZJ4,Level('mdHbMEST[avr',4),'bOzBry',"le7jNn:}DS~Kf",Level("fQX",10),'B Vd',DlPCT_VM,"iWU@yXvE",Level("mZ:sME",6)])

### EXPERIMENT
design=[bZTlT4UO,saqGRH5,wiGDC40]
crossing=[bZTlT4UO,saqGRH5,wiGDC40]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_3_1"))
### END