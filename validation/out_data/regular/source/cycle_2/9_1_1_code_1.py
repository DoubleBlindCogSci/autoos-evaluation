from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Agr7HL=['jhCRI)YIX',Level('GLuI',1),Level("mLFWURTN4pNq",5),'KgcuDbbXobSPwu',Level('vYNuY}CJPxNTli',6),'dFJ[tHB',"HukXRhVF","xthWfHGq","EkUmun(kp"]
hSuA82m7=Factor('ZbaD',Agr7HL)

### EXPERIMENT
design=[hSuA82m7]
crossing=[hSuA82m7]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_1_1"))
### END