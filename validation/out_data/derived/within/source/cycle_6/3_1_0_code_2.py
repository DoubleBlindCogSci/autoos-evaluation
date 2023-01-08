from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ppf = Factor("ppf", ["sqyxw","qzpevj","hmsmwv","rdxy","rjzf","ijlar"])
def is_jqgpn_ljo(ppf):
    return ppf == "hmsmwv"
def is_jqgpn_lxz(ppf):
    return ppf == "qzpevj"
def is_jqgpn_ibye(ppf):
    return not (is_jqgpn_ljo(ppf) or is_jqgpn_lxz(ppf))
jqgpn = Factor("jqgpn", [DerivedLevel("ljo", WithinTrial(is_jqgpn_ljo, [ppf])), DerivedLevel("lxz", WithinTrial(is_jqgpn_lxz, [ppf])), DerivedLevel("ibye", WithinTrial(is_jqgpn_ibye, [ppf]))])

design=[ppf,jqgpn]
crossing=[jqgpn]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END