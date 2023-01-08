from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ipr = Factor("ipr", ["ims", "pflynz"])
mzq = Factor("mzq", ["jjbay", "wcdq"])
xtvepx = Factor("xtvepx", ["fipbp", "bildsx"])
qkb = Factor("qkb", ["xsyes", "nbnh"])
eszmjd = Factor("eszmjd", ["dee", "xpit"])
ydy = Factor("ydy", ["jbdsj", "ecqixf"])
hvbry = Factor("hvbry", ["jzjc", "ffknc"])
bbpkkg = Factor("bbpkkg", ["vfqv", "uvrbps"])
xtpx = Factor("xtpx", ["vcqmr", "xeeb"])

### EXPERIMENT
design=[ipr,mzq,xtvepx,qkb,eszmjd,ydy,hvbry,bbpkkg,xtpx]
crossing=[[ipr],[mzq,xtvepx,qkb,eszmjd],[ydy,hvbry,bbpkkg,xtpx],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_5"))
### END