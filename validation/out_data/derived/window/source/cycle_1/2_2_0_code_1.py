from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
avahh = Factor("avahh", ["yax","rxkwhl","hhuxrh","ikxtd","uxzog","rwemy","enfch"])
gzc = Factor("gzc", ["yax","rxkwhl","hhuxrh","ikxtd","uxzog","rwemy","enfch"])
wzfxxn = Factor("wzfxxn", ["yax","rxkwhl","hhuxrh","ikxtd","uxzog","rwemy","enfch"])
def ddyxvs(avahh, gzc, wzfxxn):
    return avahh[-2] == gzc[0] or avahh[0] != wzfxxn[-2]
def zwuig(avahh, gzc, wzfxxn):
    return not ddyxvs(avahh, gzc, wzfxxn)
pwqdl = DerivedLevel("ddgmep", Window(ddyxvs, [avahh, gzc, wzfxxn],3,1))
kpdrzq = DerivedLevel("usy", Window(zwuig, [avahh, gzc, wzfxxn],3,1))
hrm = Factor("eanb", [pwqdl, kpdrzq])

### EXPERIMENT
design=[avahh,gzc,wzfxxn,hrm]
crossing=[hrm]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END