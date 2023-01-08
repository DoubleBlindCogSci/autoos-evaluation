from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ATt = Factor("ATt", ["hON", "gSvq_", "ijm}CjTDpBompc", "nLI*YFg", "ZkQHyJN(j~ ", "$ZzoKDfJOb|", "dcfxkQnOR6r", "NwPbastQN", "eI setsNY", "IyxCxQQHV"])
W_AzyZw__MSK = Factor("W7AzyZw~?MSK", ["lseRor!cqHCa", "T}fikaFghFlNYz", "pk<b LuZ^oGY", "bLs", "rrnjycxVCiROM", "ktBGy$", "hGVKFWCd0F", "wSou_ejp", "2wQ", "#rithj(Zxe"])

design=[ATt,W_AzyZw__MSK]
crossing=[ATt,W_AzyZw__MSK]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/10_2_0"))

### END
