from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Wx_= Factor("Wx&", ["xjcu", Level("& uMPiooLVY", 1), Level("WJTqLh$ NzW", 9)])
MnXagrJn_mn= Factor("MnXagrJn_mn", ["BgJ%@Vy1bae", Level("Kqi4LqXZvB}cPN", 7), Level("uQwpFRFvVea", 1)])

design=[Wx_,MnXagrJn_mn]
crossing=[Wx_,MnXagrJn_mn]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/3_2_1"))

### END
