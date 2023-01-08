from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_JZf_Gnpbnc_J = Factor("[JZf{Gnpbnc0J", ["Q4eRN", "mjrgSLkfaIAIQ", "KoyRHs", "eVosBH", "bUvdc", "RN)0sWERgwkrv", "FDjlP)h"])
otksVwounPMzF = Factor("otksVwounPMzF", ["bGwec SXzC&d)c", "U0hJt8DHGQ", "LJSqpYhIRmp", "KpkxejmULVRVK", "xpRpjzcegqrRs ", "(sVO<TNudPsmi", "mKh"])


design=[_JZf_Gnpbnc_J,otksVwounPMzF]
crossing=[_JZf_Gnpbnc_J,otksVwounPMzF]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_2_1"))

### END
