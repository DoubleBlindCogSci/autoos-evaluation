from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
geucEiq7=Factor('ya$',["h#jzak",Level('Fu(mYYzc!eD4E<',3),"LNcGLxIdFrSv",'OzX%OfsRWx9kly','YCN',Level('snCkYKFVta',10)])
q7ysU=["KTeTuHou*aO","@JNE",'WeknS~Y',"DjFrBW}pjHvW",'DdOx1XLCCU',Level("zPQQn",4)]
Ghe6WQ=Factor("aKuYu*ercSL",q7ysU)

### EXPERIMENT
design=[geucEiq7,Ghe6WQ]
crossing=[geucEiq7,Ghe6WQ]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_0"))
### END