from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cnb= Factor("cnb", ["yxdvh","gwd","rdg","kvstg","dbcw","erk"])

def is_vmehak_zhj(cnb):
    return cnb != "erk" and cnb != "rdg"
def is_vmehak_fuhh(cnb):
    return not is_vmehak_zhj(cnb)
vmehak= Factor("vmehak", [DerivedLevel("zhj", WithinTrial(is_vmehak_zhj, [cnb])), DerivedLevel("fuhh", WithinTrial(is_vmehak_fuhh, [cnb]))])


design=[cnb,vmehak]
crossing=[vmehak]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END
