from sweetpea import *
import os
_dir=os.path.dirname(__file__)
pjw = Factor("pjw", ["yfn", "ecwpfd"])
bovuke = Factor("bovuke", ["ryoi", "ydr"])
qylqc = Factor("qylqc", ["duag", "zvutv"])
nhlg = Factor("nhlg", ["ywg", "kktt"])
ynyb = Factor("ynyb", ["jbs", "xbe"])
vhnsj = Factor("vhnsj", ["avphmd", "kkjx"])
zrsapb = Factor("zrsapb", ["nbybed", "gvd"])
hukp = Factor("hukp", ["igg", "jvufve"])
acns = Factor("acns", ["grnqpx", "tfvsf"])
qnzux = Factor("qnzux", ["lmzyfv", "mdn"])
tldpnx = Factor("tldpnx", ["oqeizn", "qznl"])
wchxn = Factor("wchxn", ["udcy", "bedt"])
brrsj = Factor("brrsj", ["dbz", "hcyucc"])
constraints = []
crossing = [[pjw, bovuke, qylqc, nhlg], [ynyb, vhnsj, zrsapb], [hukp, acns], [qnzux, tldpnx, wchxn, brrsj]]


design=[pjw,bovuke,qylqc,nhlg,ynyb,vhnsj,zrsapb,hukp,acns,qnzux,tldpnx,wchxn,brrsj]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_0"))

### END