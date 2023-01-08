from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yrcneo= Factor("yrcneo", ["cvpjht","akn","fpuslh","mtkpab","pygjc"])
ixp= Factor("ixp", ["cuf","xuebm","zcio","ufdatp","zdwdp"])
def is_ykb_dlg(yrcneo, ixp):
    return yrcneo[0] != yrcneo[-4] and ixp[0] != ixp[-1]
def is_ykb_ooynm(yrcneo, ixp):
    return not is_ykb_dlg(yrcneo, ixp)
ykb= Factor("ykb", [DerivedLevel("dlg", Window(is_ykb_dlg, [yrcneo, ixp], 4, 1)), DerivedLevel("ooynm", Window(is_ykb_ooynm, [yrcneo, ixp], 4, 1))])

design=[yrcneo,ixp,ykb]
crossing=[ykb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END
