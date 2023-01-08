from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_FzSMyl = Factor("}FzSMyl", ["m LrDFvap", "wtF<LZFluJ", "*qnh(M"])
BIwkduEvUm = Factor("BIwkduEvUm", ["~Gq", "LrLs", "MstFu~dL4fyrCY"])
pc_AbZlUc = Factor("pc|AbZlUc", ["hhwdX&Y<@", "E~ZwGxz", "L<YDO"])
Qrw_CIO = Factor("Qrw?CIO", ["qdBmj%qSq4_xfa", "jKYT)7ci", "0x&gWPPs", "c|!hF:ooQ>ie"])


design=[_FzSMyl,BIwkduEvUm,pc_AbZlUc,Qrw_CIO]
crossing=[_FzSMyl,BIwkduEvUm,pc_AbZlUc,Qrw_CIO]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_4_1"))

### END
