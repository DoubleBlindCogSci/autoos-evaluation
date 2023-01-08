from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
KRGb_oxJ_S_E = Factor("KRGb]oxJ S%E", ["<LNtSV", '%ZHAtUoQD", "PrH", 'te9nWzStC", "t!m{YqJd", "zkWIHDEMn"])
Ncvzjt_zwtl = Factor("Ncvzjt~zwtl", ["vX[OaFdCWV", "VEBlp", "CSaQe#6CYihBGy", "j#n#t", "QjgG_zuF", "Or5F1pdvJaT|Sk", "QtUWmc$Np|"])
_OCBIdJXiSXz = Factor("%OCBIdJXiSXz", [Level("eSfvQg", 1), Level(" N} bG8IiO", 2), Level("9n>", 3), Level("2Y1JFWinNt5", 1), Level("SJjHwS$", 1), Level("YKhkxIXGNeuzYM", 1)])

design=[KRGb_oxJ_S_E,Ncvzjt_zwtl,_OCBIdJXiSXz]
crossing=[KRGb_oxJ_S_E,Ncvzjt_zwtl,_OCBIdJXiSXz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_3_1"))

### END
