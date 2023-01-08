from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lakcca = Factor("lakcca", ["lmwclj","pyqh", "yguvoa"])
lzpcr = Factor("lzpcr", ["ggiew", "aof"])
zkc = Factor("zkc", ["axkt","vdhy","bfcwbk", "xwkway"])
xqjmj = Factor("xqjmj", ["ahjxx","luswle", "jyeem"])
uwwbe = Factor("uwwbe", ["sfzkj", "avs"])


constraints = [MinimumTrials(17), Exclude((lzpcr, "aof"))]
crossing = [zkc, xqjmj, uwwbe]

design=[lakcca,lzpcr,zkc,xqjmj,uwwbe]

### APPENDIX
block=CrossBlock(design,crossing,constraints,require_complete_crossing=False)
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2"))

### END