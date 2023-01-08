from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
RiIw_ZGdxgzqi = Factor("RiIw7ZGdxgzqi", [Level("dkpm[", 3), Level("YbErnP", 2), Level("oUIZXF4S", 1), Level("uFvTVnb", 1), Level("tDgoKwQvv", 1), Level("KzozGI7x0#oc!u", 1), Level("R;Dt", 1)])
Im__JagACs__Z = Factor("Im$~JagACs4$Z", [Level("nDGt%", 4), Level("XCC", 1), Level("iBtWtz8F", 1), Level("HpVeN?QcZdg;RS", 1), Level("qC]PhLDmg2l", 1), Level("VFlRZUFhYdA", 1), Level("Qdu", 1)])
_Gl_FcSwL = Factor("8Gl%FcSwL", [Level("pfnl;SC6", 3), Level("DpN&ZQGRp", 1), Level("IcP", 1), Level("rrs", 1), Level("ymaaeSXZltSlT", 1), Level("Guct&f_wiqcYr", 1), Level(" yPkbXMIZh", 1), Level("IChBrBMr^a", 1)])

design=[RiIw_ZGdxgzqi,Im__JagACs__Z,_Gl_FcSwL]
crossing=[RiIw_ZGdxgzqi,Im__JagACs__Z,_Gl_FcSwL]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_3_0"))

### END
