from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jyMJFmejL__riP = Factor("jyMJFmejL^$riP", [Level("dJI%LKQM2b", 8), Level("6nNM9JzBH", 1), Level("4lvw9vkCXAd", 1), Level("b5v#{rQmbVl", 1), Level("dnVGG$jGosiw", 4), Level("CsLiKY", 1), Level("X3]Xg%Ybv(SS", 1), Level("sJEXiFaDEPF2tI", 1), Level("uinKOa?R4NQ^p;", 5), Level("vaoA", 1)])
b_xatqivt = Factor("b;xatqivt", [Level("pC4]5quBFbYx#", 1), Level("rRgLFs_b", 1), Level("Y&IqDNTxiZ", 1), Level("ENeYshy", 1), Level("CDwDwCV", 1), Level("FJ{H8", 1), Level("MYmNwuFq", 3), Level("kDlxS_}VgRTK", 1), Level("cmSrfDovTtUU", 10), Level("d:UQ", 1), Level("ghbnXlPeFaKhGL", 1)])

design=[jyMJFmejL__riP,b_xatqivt]
crossing=[jyMJFmejL__riP,b_xatqivt]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_2_0"))

### END
