from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
SUdOBzK_vpH = Factor("SUdOBzK8vpH", ["CCY", "qeULZr[fAivq? ", "hlN~", "UxmC]zanlu", "$H^*MUN", "khpbXCprfqy$", "&oL8xta3C", ""])
R_GlhTqy = Factor("R[GlhTqy", ["jdk3", "AtncqBx", "6oZcf", "hzWA", "@hATCbcYA", "lcph", ")Z~nlPHljR", ""])
Tmytp_pFKCrA = Factor("Tmytp$pFKCrA", [Level("kKGKSRFxfAnoAJ", 1), Level("cFHsBxmdIVp", 2), Level("dwAj", 1), Level("Q9n|(mK", 1), Level("wOTpOtXBke", 1), Level("t!NZ", 1), Level("JjhygVygnX85m", 1), Level("A_ou4VdVbXdHaq", 1)])

design=[SUdOBzK_vpH,R_GlhTqy,Tmytp_pFKCrA]
crossing=[SUdOBzK_vpH,R_GlhTqy,Tmytp_pFKCrA]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_3_1"))

### END
