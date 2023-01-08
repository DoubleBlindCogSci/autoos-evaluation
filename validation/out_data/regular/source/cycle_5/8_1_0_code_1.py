from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ze8fmhE=['f>ua',"KdeE<r","nkWhcHtcMqDZ","UqnKxkHQ","H]N kZOaC|LMDv"," y!xi",Level("HWRSgrBwr>fyS!",4),"HZDVNeT"]
UqNC7bL=Factor("Kag;22Jf6ZZLQ",ze8fmhE)

### EXPERIMENT
design=[UqNC7bL]
crossing=[UqNC7bL]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_1_0"))
### END