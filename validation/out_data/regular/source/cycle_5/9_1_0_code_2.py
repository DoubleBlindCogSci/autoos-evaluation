from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eIRa_mp_xhDb = Factor("eIRa<mp<xhDb", [Level("rLCR5h~NLcTLUu", 1), Level("AFt", 1), Level("CWMql3]HUMVKrN", 1), Level("ljt", 2), Level("piqS#NWhxj", 1), Level("g>BRsRvs", 3), Level("9fusx2lFe GKOL", 1), Level("xQp", 1), Level("hm9fxe(ofqgV", 3), Level("91EmrhgBpu", 1)])

design=[eIRa_mp_xhDb]
crossing=[eIRa_mp_xhDb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_1_0"))

### END
