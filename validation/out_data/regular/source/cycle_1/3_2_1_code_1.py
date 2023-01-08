from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
BanANW9HJ=Factor("Wx&",['xjcu',"& uMPiooLVY",Level('WJTqLh$ NzW',9)])
nvh6K=Factor('MnXagrJn_mn',["BgJ%@Vy1bae",Level("Kqi4LqXZvB}cPN",7),'uQwpFRFvVea'])

### EXPERIMENT
design=[BanANW9HJ,nvh6K]
crossing=[BanANW9HJ,nvh6K]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/3_2_1"))
### END