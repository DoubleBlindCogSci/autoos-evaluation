from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Kag___Jf_ZZLQ = Factor("Kag;22Jf6ZZLQ", ["f>ua", "KdeE<r", "nkWhcHtcMqDZ", "UqnKxkHQ", "H]N kZOaC|LMDv", " y!xi", Level("HWRSgrBwr>fyS!", 4), "HZDVNeT"])

design=[Kag___Jf_ZZLQ]
crossing=[Kag___Jf_ZZLQ]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_1_0"))

### END
