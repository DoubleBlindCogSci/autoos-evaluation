from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ng_T = Factor("ng#T", [Level("QPW_FX^Y*M", 8), Level("dTD9MPpG<D", 1), Level("Z~wRCPKTX", 1), Level("bKYQxbaaNY", 1), Level("EAQSxiHxO1B!A", 1), Level("n$Rl#DY", 1), Level("Nh[kOF(?Gvw", 2), Level("sgbfvSj", 1)])

design=[ng_T]
crossing=[ng_T]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_1_0"))

### END
