from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vmuLJj3L5Gc=Factor('ZSZcLRq',['fMOJxSSSw','DnEDue','lpjjMcCa}UMY','QLkFpeZIA9L@l','CWR1VeFKirTP',"cJL0HWA iYB"])
U50NpUhTqiF=Factor("zwyiYIH",['fwMcoY',Level('P4SfSEsLSrhH',3),'oyM7KDBmamZZ>C',"WgPgcTONvkMcma","*alM(yoV9","txc|ozhjKAsI"])
gLVo=Factor("DpLReK7H k",['S&qUzgKe',"lJlO",'RSNR',"}YsEJH<PX[","dHExo}NFcyN",Level('OMjr',2)])
BAwualGWCP=Factor('klB&Y',["IgFxrb",'mGrVmr',"fJYSv","gVqAobUW","AjjHXwIXt",'vtplV:{'])

### EXPERIMENT
design=[vmuLJj3L5Gc,U50NpUhTqiF,gLVo,BAwualGWCP]
crossing=[vmuLJj3L5Gc,U50NpUhTqiF,gLVo,BAwualGWCP]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_4_0"))
### END