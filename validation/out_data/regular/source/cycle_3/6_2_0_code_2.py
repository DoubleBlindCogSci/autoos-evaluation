from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
aW_XF_Ppl = Factor("aW5XF^Ppl", [Level("CtY", 1), Level("y2HTrxgQOIGf", 1), Level("LfMk7F2", 1), Level("D&OxumH>", 1), Level("giokp", 5), Level("lwOE", 1), Level("wp)!M", 10)])
s__ttxWvCB = Factor("s;^ttxWvCB", [Level("_v0K p6SrNn", 1), Level("Gpkk)Z1 c", 1), Level("FCw", 1), Level("ImRK", 1), Level("hklgw", 1), Level("@fJ", 1), Level(">rEEKoL9{Wd", 1)])

design=[aW_XF_Ppl,s__ttxWvCB]
crossing=[aW_XF_Ppl,s__ttxWvCB]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_0"))

### END
