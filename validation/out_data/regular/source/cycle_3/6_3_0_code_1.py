from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tG7ep="mkG"
fLpN=["o&hqnoGLqDytjX","OdH",'VOfxC3Omb%A','jJAN18N',tG7ep,"CwpAf4rQGNA",Level('ZRjSb*9E:n>',7)]
IbcH2=Factor('zmlMNmIsOxRD',fLpN)
QGteir42GsR=Factor('MSpw(dWsfrsZw',["SSaaahFktKaKIS",Level('MDrEK<QAy',4),'zZH','gWGsXcb',"OqxH","db sNZuZI)MwCx"])
r9hIUz8LBR=Factor("3J:b[",['qc^7(t^Ulc',"TPPZfRaEXs4u",Level("~JZESduWvLrpV3",8),"@gU(mw$tim","4ORsMW",Level('oPDRL',4)])

### EXPERIMENT
design=[IbcH2,QGteir42GsR,r9hIUz8LBR]
crossing=[IbcH2,QGteir42GsR,r9hIUz8LBR]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_3_0"))
### END