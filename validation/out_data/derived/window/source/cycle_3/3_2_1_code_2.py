from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dnra = Factor("dnra", ["ljvmuk","ygt","rvrj","grjvgd","wbxeh","xnah"])
hxqdn = Factor("hxqdn", ["rpszlw","qcbwi","zfrk","hevlrn","bkjxw","jmtsrb","mln"])
def is_xyye_cigu(dnra, hxqdn):
    return dnra[-1] == "xnah" and hxqdn[-3] != "hevlrn"
def is_xyye_lyc(dnra, hxqdn):
    return dnra[-1] != "xnah" and hxqdn[-3] == "hevlrn"
def is_xyye_ewzu(dnra, hxqdn):
    return not (is_xyye_cigu(dnra, hxqdn) or is_xyye_lyc(dnra, hxqdn))
xyye= Factor("xyye", [DerivedLevel("cigu", Window(is_xyye_cigu, [dnra, hxqdn], 4, 1)), DerivedLevel("lyc", Window(is_xyye_lyc, [dnra, hxqdn], 4, 1)), DerivedLevel("ewzu", Window(is_xyye_ewzu, [dnra, hxqdn], 4, 1))])

design=[dnra,hxqdn,xyye]
crossing=[xyye]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END
