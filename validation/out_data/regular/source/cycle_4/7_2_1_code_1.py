from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fiGN7=Factor('[JZf{Gnpbnc0J',["Q4eRN",'mjrgSLkfaIAIQ','KoyRHs','eVosBH',"bUvdc",'RN)0sWERgwkrv',"FDjlP)h"])
iPWF=Factor('otksVwounPMzF',['bGwec SXzC&d)c','U0hJt8DHGQ',Level("LJSqpYhIRmp",4),Level('KpkxejmULVRVK',1),'xpRpjzcegqrRs ',"(sVO<TNudPsmi",'mKh'])

### EXPERIMENT
design=[fiGN7,iPWF]
crossing=[fiGN7,iPWF]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_2_1"))
### END