from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Tj_z = Factor("Tj2z", [Level("f_W]B<ZRuG", 9), Level("MjfPLdhu", 6), "rF]ZyO", "ctG:tUTxkTUNH*", "e|Kmp7hKAg0Bg", "X:MifqeRNZxDL{", "ug(4)", "fTd"])
_DoQDv = Factor(";DoQDv", [Level("xadYQNJsPQIE", 9), Level("kvKzrxfWmLvzS", 9), "nPsPIw", "bIqzL", "ErKccNMuoym T{"])

design=[Tj_z,_DoQDv]
crossing=[Tj_z,_DoQDv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_0"))

### END
