from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
acN = Factor("acN", ["NCxmd", "PteBpv", "nNg", "tpD^5R", "!A&"])
qnqYg = Factor("qnqYg", ["pA;b)<luxgDWs", "zVuz9K>H)rdwcB", "{7xhelWGHSNd!Y", "WXRcPM%MU5YSzC", "hKaRwnnoDeWXX", "hr?", "ioNKmC", "a{WDu4U8Pz(Xd", "1V*"])
__YO_NIn = Factor(";9YO?NIn", [Level("2KPeoV0NsF*AGf", 4), Level("jpGSx", 1), Level("XP1b", 1), Level("8a*WJXla)", 1), Level("mctOo", 1)])

design=[acN,qnqYg,__YO_NIn]
crossing=[acN,qnqYg,__YO_NIn]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_3_0"))

### END
