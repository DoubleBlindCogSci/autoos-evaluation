from sweetpea import *
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
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_3_0"))
### END