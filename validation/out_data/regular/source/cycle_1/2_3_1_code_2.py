from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
BNpEwv_T= Factor("BNpEwv@T", ["LLeVDr", "XN9DUj^IEz"])
PSCUREaDySmUP= Factor("PSCUREaDySmUP", [Level("q6GqtQ8ONseYUv", 1), Level("eeFDH4#jlgJy", 3)])
jcx= Factor("jcx", [Level("I)GeF", 2), Level("kmx", 1)])

design=[BNpEwv_T,PSCUREaDySmUP,jcx]
crossing=[BNpEwv_T,PSCUREaDySmUP,jcx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/2_3_1"))

### END
