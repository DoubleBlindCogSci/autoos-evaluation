from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_DRl_cVPj_ = Factor("[DRl@cVPj%", [Level("gJvZ", 3), Level("JOenoqcb2Mo", 1), Level("gDcj0rCJ!", 4), Level("MnoNqtDHfdxn", 1), Level("UrzOLBabJDku", 1), Level("SqtIfU", 1), Level("UuHfqfKtmK", 8), Level("kEbZmKzeC", 1)])
CmL_cLxZ = Factor("CmL~cLxZ", [Level("qDu4qRtw", 1), Level("QOHdZu*wwL;gG", 4), Level("DDOu", 6), Level("XxQCLYRWKEyal", 1), Level("dAst", 1), Level("t>VxQncProzoN", 1), Level("Gbani", 1), Level("SRnwIoCbpBHHeh", 1)])
YzQW = Factor("YzQW", [Level("(NocRPqp3j", 2), Level("Y]q3Vbr", 1), Level("tAlGiEtlmUrakW", 1), Level("P}Ra@juLhouF", 1), Level("iEwzJYTYC", 1), Level("J!rcIIN(RzG!K", 1), Level("N_$VI", 1), Level("yyy", 6)])

design=[_DRl_cVPj_,CmL_cLxZ,YzQW]
crossing=[_DRl_cVPj_,CmL_cLxZ,YzQW]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_3_0"))

### END
