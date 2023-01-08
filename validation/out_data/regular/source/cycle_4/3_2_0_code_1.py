from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
g8Ba=Factor("hWAMudbckl bx",["kKakRVC]",'KoDBjSbma~Rck','sS];RJV('])
MqK46=['jjh:ieMymY','VI6nEFbwPu',"w1GvhuMJL"]
WxGym2C=Factor("Rac",MqK46)

### EXPERIMENT
design=[g8Ba,WxGym2C]
crossing=[g8Ba,WxGym2C]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END