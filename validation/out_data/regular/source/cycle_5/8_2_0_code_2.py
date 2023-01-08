from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rZggspQ = Factor("rZggspQ", ["H*mLpzyUtgdRg", "AbfFYgTAHzYx", Level("udE", 1), Level("qQ5PYgrQB31", 2), "I$Y", "U3p", "FJL@wgMrZtT", "lPsN3JsjvALM"])
jxDBGippuVYiyj = Factor("jxDBGippuVYiyj", ["ikeJYM?mMyl3D", Level("YUK5MWm;OR9Ek", 1), "#:AGjVHGKf", "EBfb", "HJp2YwhpYk", "rFp", "HHp43#AiTfv!", "eVBD3Q%6cjs", "Jauc~dJGndi"])

design=[rZggspQ,jxDBGippuVYiyj]
crossing=[rZggspQ,jxDBGippuVYiyj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_2_0"))

### END
