from sweetpea import *
import os
_dir=os.path.dirname(__file__)
bnuqqb = Factor("bnuqqb", ["tcfvqj", "fzgpoc"])
npwyk = Factor("npwyk", ["ubqgd", "qhj"])
zuxdb = Factor("zuxdb", ["esyp", "ggll"])
yqo = Factor("yqo", ["kna", "yjxsdl"])
nkqa = Factor("nkqa", ["dxzt", "trfel"])
kwedv = Factor("kwedv", ["vtfm", "gmmam"])
constraints = []
crossing = [[bnuqqb, npwyk, zuxdb], [yqo, nkqa, kwedv]]


design=[bnuqqb,npwyk,zuxdb,yqo,nkqa,kwedv]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_0"))

### END