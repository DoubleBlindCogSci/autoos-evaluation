from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tlahu = Factor("tlahu", ["pgb","xzptv","juvf","kmsmbb","pvas","lbmeii"])
cmjg = Factor("cmjg", ["zxv","nppzc","spwnx","dxqe","uvaiu","cpdcp"])
def is_zgmb_punz(tlahu, cmjg):
    return tlahu == "juvf"
def is_zgmb_ufp(tlahu, cmjg):
    return tlahu != "juvf" and cmjg == "nppzc"
def is_zgmb_hzs(tlahu, cmjg):
    return not (is_zgmb_punz(tlahu, cmjg) or is_zgmb_ufp(tlahu, cmjg))
zgmb= Factor("zgmb", [DerivedLevel("punz", WithinTrial(is_zgmb_punz, [tlahu,cmjg])), DerivedLevel("ufp", WithinTrial(is_zgmb_ufp, [tlahu, cmjg])), DerivedLevel("hzs", WithinTrial(is_zgmb_hzs, [tlahu, cmjg]))])

design=[tlahu,cmjg,zgmb]
crossing=[zgmb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END
