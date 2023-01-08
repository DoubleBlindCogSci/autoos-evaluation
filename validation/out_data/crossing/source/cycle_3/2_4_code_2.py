from sweetpea import *
import os
_dir=os.path.dirname(__file__)
yde = Factor("yde", ["nhmxnl", "uij"])
nxlg = Factor("nxlg", ["pfbl", "uvfh"])
une = Factor("une", ["xolt", "tqvcg"])
qzxuf = Factor("qzxuf", ["nhbv", "zje"])
wcn = Factor("wcn", ["crme", "comly"])
cqxp = Factor("cqxp", ["puspni", "iud"])
anb = Factor("anb", ["blqmgv", "ali"])
lkgs = Factor("lkgs", ["zhai", "kfqfnv"])
constraints = []
crossing = [[yde, nxlg, une, qzxuf], [wcn, cqxp, anb, lkgs]]


design=[yde,nxlg,une,qzxuf,wcn,cqxp,anb,lkgs]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_4"))

### END