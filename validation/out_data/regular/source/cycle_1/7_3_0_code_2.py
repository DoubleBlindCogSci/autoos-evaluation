from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
l_HDHBWxR= Factor("l>HDHBWxR", [Level("Ls(t", 3), Level("sTUiO3eXcy^I", 1), Level("at*(bs9jDinb", 1), Level("XuHVRnZAkHn", 1), Level("WTayEPxExi^", 1), Level("Nnrp!n&dQJ", 8), Level("qUwDOPNIMCJ", 1), Level(" XmHk1", 9)])
uBKrQeGEhYKrb= Factor("uBKrQeGEhYKrb", [Level("14KKMYqM", 8), Level("afw", 8), Level("jcQiT", 10), Level("vRe", 1), Level("OvVrLC", 1), Level("Ka Le", 1), Level("vgwJ", 1), Level("%zQxUl}YWtoB", 1)])
NcIdaI= Factor("NcIdaI", [Level("TtS9fTWcz>I", 1), Level("bJbuVL", 1), Level("CxIbZLCmEiy", 8), Level("V uDd^vq", 1), Level("G_yvV)5", 1), Level("}LI^jmZ:!}s", 4), Level("u&gvyt", 1)])

design=[l_HDHBWxR,uBKrQeGEhYKrb,NcIdaI]
crossing=[l_HDHBWxR,uBKrQeGEhYKrb,NcIdaI]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/7_3_0"))

### END
