from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wcom_J=['UUHMmNSxl',Level("VGHkg",4),"pbPOGOw"]
sCqH2Dl=Level('kTSZa?Gz',9)
E1pm0x=[Level("IQJL",10),'3&h)AV',wcom_J[0],Level("qrFthpS|tVeHWJ",6),'GGI5Fea',sCqH2Dl,Level('dXEpv#xE[inoJd',10)]
SNj4gEinO=Factor('IRFBTnR',E1pm0x)
xt6ly9=["zP%yvoiE?Bv)y",Level("cS&ThNN",6),"vPZpS",Level('qcZYKB',6),"RYc"]
lzBL=Factor("TPlnvC*",xt6ly9)

### EXPERIMENT
design=[SNj4gEinO,lzBL]
crossing=[SNj4gEinO,lzBL]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_0"))
### END