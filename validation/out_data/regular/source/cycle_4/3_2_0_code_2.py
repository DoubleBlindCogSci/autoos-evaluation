from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

hWAMudbckl_bx = Factor("hWAMudbckl bx", ["kKakRVC]", "KoDBjSbma~Rck", "sS];RJV("])
Rac = Factor("Rac", ["jjh:ieMymY", "VI6nEFbwPu", "w1GvhuMJL"])


design=[hWAMudbckl_bx,Rac]
crossing=[hWAMudbckl_bx,Rac]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END
