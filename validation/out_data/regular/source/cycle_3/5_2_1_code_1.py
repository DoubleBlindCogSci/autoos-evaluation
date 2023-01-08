from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
u0lNpmVpH=Factor("mFqDNN!M;bv",[Level('zNetXJow',5),Level('DfMFe',1),"y_St",Level("WxWi",7),Level('kGiXa5<bdFP ',5)])
OHBDukXxa="KVkCfe"
yNsH=Factor('wR?XQip4',[OHBDukXxa,'X3xzKAD',"2xTlvaElNl",Level('HwqO',5),"Yjr",Level('Lo>UHI',1)])

### EXPERIMENT
design=[u0lNpmVpH,yNsH]
crossing=[u0lNpmVpH,yNsH]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_1"))
### END