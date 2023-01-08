from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
RDSEpr = Factor("RDSEpr", ["ZggI nf5aThntc", "WziuObriIO", "ERd", "yl]DPGD", "OfC4J", "HWY8sY", "QWgAs", "oVtwy Nc[ ", "AsKvEGHInx&B"])
_gbiy = Factor("[gbiy", [Level("jYyh&", 2), Level("IuHlLOFjeZD", 1), Level("Edl", 1), Level("E]lWG", 1), Level("Y5qkZW", 1), Level("!COqemf", 1), Level("$9DApcQO", 1), Level("&yixbxzcOsE", 1), Level("TSwfa", 1), Level("(SQ?a 8LfVWO", 4)])
X_pX = Factor("X@pX", ["pUWSzeHp", "TFWMACuTiC4", "ntfVIgRC", "sSFM", "LFk7B_e", "PExu", Level("uO1gGGkvBhMNqo", 4), "GPUN?4u", "EcUgZTJV"])
__E = Factor("65E", ["uPjIFDWiqNdeX", "rUrpr01Sv:", "UelMQN", "1QBt9HRsifg", Level("mjxEhahdbIQg", 1), "PT$pn2JDit", "RFnByR^YB", "3d!", "uVTSouO7N"])

design=[RDSEpr,_gbiy,X_pX,__E]
crossing=[RDSEpr,_gbiy,X_pX,__E]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_4_0"))

### END
