from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
yrcneo = Factor("yrcneo", ["cvpjht","akn","fpuslh","mtkpab","pygjc"])
ixp = Factor("ixp", ["cuf","xuebm","zcio","ufdatp","zdwdp"])
def byjjot(yrcneo, ixp):
    return yrcneo[-3] != "mtkpab" and ixp[0] != "zcio"
def ezupnv(yrcneo,ixp):
    return yrcneo[-3] == "mtkpab" or ixp[0] == "zcio"
myyhpf = DerivedLevel("dlg", Window(byjjot, [yrcneo, ixp],4,1))
ckwqu = DerivedLevel("ooynm", Window(ezupnv, [yrcneo, ixp],4,1))
zrdgap = Factor("ykb", [myyhpf, ckwqu])

### EXPERIMENT
design=[yrcneo,ixp,zrdgap]
crossing=[zrdgap]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END