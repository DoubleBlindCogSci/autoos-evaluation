from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZMT_HDPrv = Factor("ZMT<HDPrv", ["IEM(0~QoZ", "AmiJ(HkuBB", "KjNIzZMgR", "yQNLkC8", "VW$xUUt", "teUZsTZAI", Level("w(FEXfsSr6KU|", 1), "BcTS"])

design=[ZMT_HDPrv]
crossing=[ZMT_HDPrv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_1_0"))

### END
