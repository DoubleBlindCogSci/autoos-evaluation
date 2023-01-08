from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Bzdb=["CCY",'qeULZr[fAivq? ',"hlN~",'UxmC]zanlu','$H^*MUN',"khpbXCprfqy$","&oL8xta3C"]
LmUpAQ8iBoD=Factor('SUdOBzK8vpH',Bzdb)
PVGXQ=Factor("R[GlhTqy",['jdk3',"AtncqBx","6oZcf",'hzWA','@hATCbcYA','lcph',")Z~nlPHljR"])
VgdZ2Q='dwAj'
uaEeuY=['kKGKSRFxfAnoAJ',Level('cFHsBxmdIVp',2),VgdZ2Q,"Q9n|(mK",'wOTpOtXBke','t!NZ',"JjhygVygnX85m",'A_ou4VdVbXdHaq']
SZJKXP6=Factor('Tmytp$pFKCrA',uaEeuY)

### EXPERIMENT
design=[LmUpAQ8iBoD,PVGXQ,SZJKXP6]
crossing=[LmUpAQ8iBoD,PVGXQ,SZJKXP6]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_3_1"))
### END