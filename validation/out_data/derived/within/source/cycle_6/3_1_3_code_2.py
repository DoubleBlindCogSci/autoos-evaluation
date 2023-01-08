from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
flf = Factor("flf", ["mzt","idcvup","ejpvyk","lliic","igbcrl","hwlruj","tbtts","rieymr"])
def is_cpgwf_hne(flf):
    return flf == "igbcrl"
def is_cpgwf_naof(flf):
    return flf == "hwlruj"
def is_cpgwf_hanqhq(flf):
    return not (is_cpgwf_hne(flf) or is_cpgwf_naof(flf))
cpgwf = Factor("cpgwf", [DerivedLevel("hne", WithinTrial(is_cpgwf_hne, [flf])), DerivedLevel("naof", WithinTrial(is_cpgwf_naof, [flf])), DerivedLevel("hanqhq", WithinTrial(is_cpgwf_hanqhq, [flf]))])

design=[flf,cpgwf]
crossing=[cpgwf]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END