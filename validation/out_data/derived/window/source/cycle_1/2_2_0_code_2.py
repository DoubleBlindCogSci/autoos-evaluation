from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
avahh= Factor("avahh", ["yax","rxkwhl","hhuxrh","ikxtd","uxzog","rwemy","enfch"])
gzc= Factor("gzc", ["yax","rxkwhl","hhuxrh","ikxtd","uxzog","rwemy","enfch"])
wzfxxn= Factor("wzfxxn", ["yax","rxkwhl","hhuxrh","ikxtd","uxzog","rwemy","enfch"])
def is_eanb_ddgmep(avahh, gzc, wzfxxn):
    return avahh[0] == gzc[-2] or avahh[0] != wzfxxn[-1]
def is_eanb_usy(avahh, gzc, wzfxxn):
    return not is_eanb_ddgmep(avahh, gzc, wzfxxn)
eanb= Factor("eanb", [DerivedLevel("ddgmep", Window(is_eanb_ddgmep, [avahh, gzc, wzfxxn], 3, 1)), DerivedLevel("usy", Window(is_eanb_usy, [avahh, gzc, wzfxxn], 3, 1))])

design=[avahh,gzc,wzfxxn,eanb]
crossing=[eanb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END
