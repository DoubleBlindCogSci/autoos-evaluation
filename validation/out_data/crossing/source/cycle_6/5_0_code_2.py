from sweetpea import *
import os
_dir=os.path.dirname(__file__)
hisfv = Factor("hisfv", ["bji", "gwm"])
anw = Factor("anw", ["cxph", "burq"])
akm = Factor("akm", ["dqc", "fjaak"])
xvku = Factor("xvku", ["qrmqm", "hemcr"])
hqte = Factor("hqte", ["voqekg", "eqmhpg"])
qqeqce = Factor("qqeqce", ["thux", "rlqczm"])
yqwa = Factor("yqwa", ["irfol", "ixxd"])
rxt = Factor("rxt", ["xsimsv", "jbo"])
usigz = Factor("usigz", ["xtvj", "vmiwdy"])
efudzv = Factor("efudzv", ["knf", "kztk"])
jhqq = Factor("jhqq", ["qxt", "cohbby"])
llpseo = Factor("llpseo", ["yzm", "vtxsd"])
dxr = Factor("dxr", ["ltrc", "gbvyf"])
hln = Factor("hln", ["ixohgn", "awirbk"])
jauytr = Factor("jauytr", ["plab", "kije"])
constraints = []
crossing = [[hisfv, anw, akm], [xvku, hqte, qqeqce, yqwa], [rxt, usigz, efudzv, jhqq], [llpseo, dxr, hln], [jauytr]]


design=[hisfv,anw,akm,xvku,hqte,qqeqce,yqwa,rxt,usigz,efudzv,jhqq,llpseo,dxr,hln,jauytr]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_0"))

### END