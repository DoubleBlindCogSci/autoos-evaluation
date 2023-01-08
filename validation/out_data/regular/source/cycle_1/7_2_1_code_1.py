from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qab1k=Factor("ZcVTYelGRDwiLI",['xXZuP2Q!j',"lndsygsw",Level("EsIV&NsehpG",3),'eHaDuiVxT_sN',"gm{mCNR","dFE3NILI",'uFs;GbsDPg~1'])
yu3jYky=Factor("IadPijzVwc8d",['Effa',"zDGDrLhpaCJ&9",Level("6xwBm|ciNVy",6),'UiG8vrx}dSX','KdfZeOlTmj',"W2CUuVxL",Level("fGz$pJYD",4)])

### EXPERIMENT
design=[qab1k,yu3jYky]
crossing=[qab1k,yu3jYky]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/7_2_1"))
### END