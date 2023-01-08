from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
icb = Factor("icb", ["vozb", "udvch"])
oko = Factor("oko", ["ufevml", "pvz"])
jyrt = Factor("jyrt", ["qwld", "dzo"])
lrzm = Factor("lrzm", ["vfnke", "wtpdqc"])
yirntp = Factor("yirntp", ["vzw", "uxa"])
gntrzh = Factor("gntrzh", ["kongvk", "cnwen"])
wqcaq = Factor("wqcaq", ["fgdqg", "kuefbf"])
wqyrbn = Factor("wqyrbn", ["afjep", "vfh"])
bacsgk = Factor("bacsgk", ["iqnv", "utd"])
cdo = Factor("cdo", ["vtln", "axpg"])
divfwh = Factor("divfwh", ["xksa", "puajc"])
bredj = Factor("bredj", ["huwws", "uiygp"])
imfsa = Factor("imfsa", ["tfa", "yjp"])
cunyje = Factor("cunyje", ["myuyfx", "xsfei"])
kgpt = Factor("kgpt", ["hifxxa", "myzwfe"])

### EXPERIMENT
design=[icb,oko,jyrt,lrzm,yirntp,gntrzh,wqcaq,wqyrbn,bacsgk,cdo,divfwh,bredj,imfsa,cunyje,kgpt]
crossing = [[gntrzh,wqcaq,wqyrbn,bacsgk],[cdo,divfwh,bredj,imfsa],[icb,oko,jyrt,lrzm],[cunyje,kgpt],[yirntp],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1"))
### END
