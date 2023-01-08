from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mch = Factor("mch", ["qcorlu","iufm","uqj","vba","cid","wdpce"])
yno = Factor("yno", ["mfzqrp","sqaa","lgpdao","pkosa","oyid","wtitea","kzgaih"])
def is_rlxwtt_yrk(mch, yno):
    return mch[-1] == "cid" and yno[-2] != "wtitea"
def is_rlxwtt_uvv(mch, yno):
    return mch[-1] == "cid" and yno[-2] == "wtitea"
def is_rlxwtt_hgdxmx(mch, yno):
    return not (is_rlxwtt_yrk(mch, yno) or is_rlxwtt_uvv(mch, yno))
rlxwtt = Factor("rlxwtt", [DerivedLevel("yrk", Window(is_rlxwtt_yrk, [mch, yno], 3, 1)), DerivedLevel("uvv", Window(is_rlxwtt_uvv, [mch, yno], 3, 1)), DerivedLevel("hgdxmx", Window(is_rlxwtt_hgdxmx, [mch, yno], 3, 1))])

design=[mch,yno,rlxwtt]
crossing=[rlxwtt]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END