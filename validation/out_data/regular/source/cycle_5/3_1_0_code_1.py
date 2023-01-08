from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zyf9ri6ho4=Factor('>sLWQH7',['H8wwUsG',"zpuYTwcNnJ#tp",'uRl'])

### EXPERIMENT
design=[zyf9ri6ho4]
crossing=[zyf9ri6ho4]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END