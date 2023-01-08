from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
op60qWf8jV2=Factor('OpS',[">2tXWexZ",'dSH|hlFVObONk'])
gxCx3uOcCWr=Factor('e0WxsEDEWgDMz',[Level('wgFdahXpLHV',10),Level("q;dRnYDA",10)])

### EXPERIMENT
design=[op60qWf8jV2,gxCx3uOcCWr]
crossing=[op60qWf8jV2,gxCx3uOcCWr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END