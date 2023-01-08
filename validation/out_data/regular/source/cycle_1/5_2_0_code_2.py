from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
aFFrDTJF_= Factor("aFFrDTJF~", [Level("NCeyfqWILr5RzI", 1), Level("YH%njwHgJe", 5), Level("pPr08Ddvqy", 1), Level("DM?fq Bzq", 1), Level("DpD|IK Boe", 1)])
KJgiTHr_lW= Factor("KJgiTHr7lW", [Level("}LY", 1), Level("chk>mOUZsDPlO", 3), Level("]~@FmCBJsA", 8), Level("RUDwvZ?", 8), Level("AQ}RRYJf2)<Uje", 1)])

design=[aFFrDTJF_,KJgiTHr_lW]
crossing=[aFFrDTJF_,KJgiTHr_lW]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/5_2_0"))

### END
