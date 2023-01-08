from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dnra = Factor("dnra", ["ljvmuk","ygt","rvrj","grjvgd","wbxeh","xnah"])
hxqdn = Factor("hxqdn", ["rpszlw","qcbwi","zfrk","hevlrn","bkjxw","jmtsrb","mln"])
def kbhic(dnra, hxqdn):
     return "xnah" == dnra[-1] and hxqdn[-3] != "hevlrn"
def txrqqf(dnra, hxqdn):
     return "xnah" != dnra[-1] and  hxqdn[-3] == "hevlrn"
def ybk(dnra, hxqdn):
     return (not dnra[-1] == "xnah") and (hxqdn[-3] != "hevlrn")
jnk = Factor("xyye", [DerivedLevel("cigu", Window(kbhic, [dnra, hxqdn],4,1)), DerivedLevel("lyc", Window(txrqqf, [dnra, hxqdn],4,1)),DerivedLevel("ewzu", Window(ybk, [dnra, hxqdn],4,1))])
### EXPERIMENT
design=[dnra,hxqdn,jnk]
crossing=[jnk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END