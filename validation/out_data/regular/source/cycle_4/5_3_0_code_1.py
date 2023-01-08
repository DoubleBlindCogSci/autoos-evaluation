from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
VM0QWHGsRc=['AguZe4q',"D)TCvHd",'LWL;bfUfMXX','~Hhtt3e|A',"oLUkOP"]
P6BfH3=Factor('kgo',VM0QWHGsRc)
KDqJZC='vHV$k?RA*O7Uyz'
lPnkFMjO=['Ex*R dnbSS5y',"N_5rUhhWxNAi","nDMnG","Hh2g hauQVdM",KDqJZC,'rjkGF*PW']
BFdVoJVy=Factor('K>m4KDLurXc',lPnkFMjO)
Mx83aGSd=Factor("ai2",[Level("WlYDRfsh",4),Level('uB|ULzZZimJWrw',3),'7&%>JRT',"FXSjvTIFCHi","hZUta"])

### EXPERIMENT
design=[P6BfH3,BFdVoJVy,Mx83aGSd]
crossing=[P6BfH3,BFdVoJVy,Mx83aGSd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_3_0"))
### END