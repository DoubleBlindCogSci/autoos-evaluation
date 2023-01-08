from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
varpxe= Factor("varpxe", ["slql","kkzoxv","hdloe","wffdn","eudjn","vdw"])
def is_ntabf_kon(varpxe):
    return varpxe == "eudjn"
def is_ntabf_kzist(varpxe):
    return varpxe == "vdw"
def is_ntabf_qab(varpxe):
    return not (is_ntabf_kon(varpxe) or is_ntabf_kzist(varpxe))
ntabf= Factor("ntabf", [DerivedLevel("kon", WithinTrial(is_ntabf_kon, [varpxe])), DerivedLevel("kzist", WithinTrial(is_ntabf_kzist, [varpxe])), DerivedLevel("qab", WithinTrial(is_ntabf_qab, [varpxe]))])

design=[varpxe, ntabf]
crossing=[ntabf]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END
