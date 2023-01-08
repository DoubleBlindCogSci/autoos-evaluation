from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Tj_dqKuDai = Factor("Tj(dqKuDai", ["mvVxuGpSSy:vp", "J2TqQMdGeghh", " )}F(VaIy", " hn0eWdieS", "xZ1d{", "VPWkyEw", "WYXSe?dG", "pOPgX9#aGRX_k", "yeXm "])
_HZFDkQEKcx = Factor(")HZFDkQEKcx", ["b[SIBy|VQQyjD", "L@DYJX", "HBbX[1xgf", "wiedIudnsBT&Xd", "Tov<gm2nQx", ":1v", "xdsdZgjq0Gsw", "DMHM", "eTSkZuwq;"])
__W = Factor("1?W", ["{FsKTamx", "Hk!FI*fF", "[sWQAwcVu|ovk", "NO)M6", "EGxDU@3SVqdzJu", "psBQMfCk", "}xpxITnxbft", "HqgyfKXq;v", "DWGQocI"])
gYm_dH__ = Factor("gYm}dH:(", ["eLSs<", ")BAnfERE", "*_2kFQ", "iXa", "YNE]mlvZ", "pLK", "e[ibcwsjfzBpj", "sfX", "IuIbQm#Spsz{yM"])

design=[Tj_dqKuDai,_HZFDkQEKcx,__W,gYm_dH__]
crossing=[Tj_dqKuDai,_HZFDkQEKcx,__W,gYm_dH__]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_4_1"))

### END
