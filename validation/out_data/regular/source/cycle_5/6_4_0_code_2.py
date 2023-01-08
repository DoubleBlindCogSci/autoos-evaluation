from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZSZcLRq = Factor("ZSZcLRq", ["fMOJxSSSw", "DnEDue", "lpjjMcCa}UMY", "QLkFpeZIA9L@l", "CWR1VeFKirTP", "cJL0HWA iYB"])
zwyiYIH = Factor("zwyiYIH", [Level("fwMcoY", 1), Level("P4SfSEsLSrhH", 3), Level("oyM7KDBmamZZ>C", 1), Level("WgPgcTONvkMcma", 1), Level("*alM(yoV9", 1), Level("txc|ozhjKAsI", 1)])
DpLReK_H_k = Factor("DpLReK7H k", ["S&qUzgKe", "lJlO", "RSNR", "}YsEJH<PX[", "dHExo}NFcyN", Level("OMjr", 2)])
klB_Y = Factor("klB&Y", ["IgFxrb", "mGrVmr", "fJYSv", "gVqAobUW", "AjjHXwIXt", "vtplV:{"])

design=[ZSZcLRq,zwyiYIH,DpLReK_H_k,klB_Y]
crossing=[ZSZcLRq,zwyiYIH,DpLReK_H_k,klB_Y]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_4_0"))

### END
