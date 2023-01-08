from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Ncp = Factor("Ncp", [Level("u%whc", 1), Level("NAhQ2 &waGA", 1), Level("puZz4teJMKJ", 1), Level("vmlShuSG_h", 1), Level("juX3RSd8qJ", 1), Level("wIY4vATHmeHn", 1), Level("~i)HFQmcpRH", 5), Level("lg%9szyeLPs", 1), Level("I3cUKG", 6), Level("DBv6tnuw", 10)])
gD_MZ_US = Factor("gD!MZ[US", [Level("QRvUD*fo", 1), Level("b&gSEeGoXmkW", 1), Level("bmqI~wVl{GDGra", 1), Level("KNo D8", 1), Level("gI2YFl]syX", 3), Level("LtAgghskcb&", 1), Level("yGK", 7), Level("OFkXIpQ>", 1), Level("CiGQ^LCZiZGsUt", 4)])

design=[Ncp,gD_MZ_US]
crossing=[Ncp,gD_MZ_US]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_2_1"))

### END
