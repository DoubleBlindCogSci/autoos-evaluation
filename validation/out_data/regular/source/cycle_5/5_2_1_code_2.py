from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
CL_s_kKLvg = Factor("CL2s0kKLvg", ["TFyBEilVx", "afh D_<XaMM3]", "cFOHPxTuk", "Muil{O@^)SBZho", "iWWjWwCl"])
hACykAtr = Factor("hACykAtr", [Level("cil4Xt", 1), Level("C! Yysz2wAXcq_", 1), Level("zo7V4Qh", 1), Level("IWDkJ", 2), Level("hqFU1", 1), Level("Gmor:2KO&Isd", 1)])

design=[CL_s_kKLvg,hACykAtr]
crossing=[CL_s_kKLvg,hACykAtr]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_1"))

### END
