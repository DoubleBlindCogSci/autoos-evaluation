from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ya_ = Factor("ya$", [Level("h#jzak", 1), Level("Fu(mYYzc!eD4E<", 3), Level("LNcGLxIdFrSv", 1), Level("OzX%OfsRWx9kly", 1), Level("YCN", 1), Level("snCkYKFVta", 10)])
aKuYu_ercSL = Factor("aKuYu*ercSL", [Level("KTeTuHou*aO", 1), Level("@JNE", 1), Level("WeknS~Y", 1), Level("DjFrBW}pjHvW", 1), Level("DdOx1XLCCU", 1), Level("zPQQn", 4)])

design=[ya_,aKuYu_ercSL]
crossing=[ya_,aKuYu_ercSL]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_0"))

### END
