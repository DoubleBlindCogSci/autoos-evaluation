from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
P9of0VaCuHq=Factor("ng#T",[Level("QPW_FX^Y*M",8),Level('dTD9MPpG<D',7),'Z~wRCPKTX',"bKYQxbaaNY","EAQSxiHxO1B!A","n$Rl#DY",Level("Nh[kOF(?Gvw",2),'sgbfvSj'])

### EXPERIMENT
design=[P9of0VaCuHq]
crossing=[P9of0VaCuHq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_1_0"))
### END