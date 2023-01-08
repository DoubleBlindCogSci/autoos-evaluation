from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kgo = Factor("kgo", ["AguZe4q", "D)TCvHd", "LWL;bfUfMXX", "~Hhtt3e|A", "oLUkOP"])
K_m_KDLurXc = Factor("K>m4KDLurXc", ["Ex*R dnbSS5y", "N_5rUhhWxNAi", "nDMnG", "Hh2g hauQVdM", "vHV$k?RA*O7Uyz", "rjkGF*PW"])
ai_ = Factor("ai2", [Level("WlYDRfsh", 4), Level("uB|ULzZZimJWrw", 1), "7&%>JRT", "FXSjvTIFCHi", "hZUta"])

design=[kgo,K_m_KDLurXc,ai_]
crossing=[kgo,K_m_KDLurXc,ai_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_3_0"))

### END
