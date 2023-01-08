from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dhrnfc = Factor("dhrnfc", ["dav","onhc","rpl","lmj","kxolk"])
exxlpg = Factor("exxlpg", ["dav","onhc","rpl","lmj","kxolk"])
hbrqgi = Factor("hbrqgi", ["dav","onhc","rpl","lmj","kxolk"])
def is_vmgfeo_dbuz(dhrnfc, exxlpg, hbrqgi):
    return dhrnfc[-1] == exxlpg[-2] or dhrnfc[-2] == hbrqgi[-1]
def is_vmgfeo_iztnz(dhrnfc, exxlpg, hbrqgi):
    return not is_vmgfeo_dbuz(dhrnfc, exxlpg, hbrqgi)
vmgfeo = Factor("vmgfeo", [DerivedLevel("dbuz", Window(is_vmgfeo_dbuz, [dhrnfc, exxlpg, hbrqgi], 3, 1)), DerivedLevel("iztnz", Window(is_vmgfeo_iztnz, [dhrnfc, exxlpg, hbrqgi], 3, 1))])

design=[dhrnfc,exxlpg,hbrqgi,vmgfeo]
crossing=[vmgfeo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END