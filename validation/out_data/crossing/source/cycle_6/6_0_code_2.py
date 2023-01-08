from sweetpea import *
import os
_dir=os.path.dirname(__file__)
ntn = Factor("ntn", ["pzf", "brjg"])
avbl = Factor("avbl", ["kgxjut", "ptlzjd"])
czjb = Factor("czjb", ["nztwlf", "equjjz"])
rbrro = Factor("rbrro", ["kcgv", "eqx"])
teosi = Factor("teosi", ["hafgvn", "mend"])
jlp = Factor("jlp", ["kjshow", "vfzvdy"])
qglvta = Factor("qglvta", ["qhopii", "zfnsvy"])
ixq = Factor("ixq", ["grv", "vzd"])
wij = Factor("wij", ["lvptf", "gqrr"])
purl = Factor("purl", ["riavs", "pfao"])
baih = Factor("baih", ["yvz", "ymd"])
fhvv = Factor("fhvv", ["nutx", "xpv"])
vdc = Factor("vdc", ["ojvxll", "hafzm"])
hyeq = Factor("hyeq", ["bxtcrc", "nemz"])
constraints = []
crossing = [[ntn], [avbl, czjb, rbrro, teosi], [jlp], [qglvta, ixq, wij], [purl], [baih, fhvv, vdc, hyeq]]


design=[ntn,avbl,czjb,rbrro,teosi,jlp,qglvta,ixq,wij,purl,baih,fhvv,vdc,hyeq]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_0"))

### END