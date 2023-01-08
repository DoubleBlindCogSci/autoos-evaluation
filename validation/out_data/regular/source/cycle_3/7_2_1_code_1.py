from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
A28tvrBRF4=Factor("ufcU",["n *CPd",Level('A1x %OydT',10),Level("uIZZirH!kEYwIg",7),Level('PIJGKRCnawR',5),Level('(MatxpxIQo',9),'UzD',"nf9cvX"])
N9vI1yEBhS3=[Level("*BFnz",2),'wHtvDBrYsxy',";kFWwrleT",Level('ABvq:YM^kO',7),'1UROfWtA|HTbk',Level('RthmVAcUJ%u]RT',1),'ctS']
sjkyy=Factor('QG ',N9vI1yEBhS3)

### EXPERIMENT
design=[A28tvrBRF4,sjkyy]
crossing=[A28tvrBRF4,sjkyy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_2_1"))
### END