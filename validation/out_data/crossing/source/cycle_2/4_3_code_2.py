from sweetpea import *
import os
_dir=os.path.dirname(__file__)
qsg = Factor("qsg", ["lkiivd", "vdhnt"])
olhl = Factor("olhl", ["cons", "srrji"])
onnhvg = Factor("onnhvg", ["fqx", "kfr"])
jrlk = Factor("jrlk", ["wvm", "uxht"])
bhsums = Factor("bhsums", ["wrnx", "tmrd"])
oednti = Factor("oednti", ["tetu", "jmr"])
aapttm = Factor("aapttm", ["mvpxw", "nrwdl"])
awrp = Factor("awrp", ["viczx", "syi"])
yxlzu = Factor("yxlzu", ["nyxnue", "ykl"])
ynlt = Factor("ynlt", ["ckwnk", "lnyj"])
lew = Factor("lew", ["rvdl", "khxxrj"])
amd = Factor("amd", ["fltecy", "dwwqbf"])
mpsyg = Factor("mpsyg", ["xjk", "vzs"])
constraints = []
crossing = [[qsg, olhl, onnhvg, jrlk], [bhsums, oednti], [aapttm, awrp, yxlzu], [ynlt, lew, amd, mpsyg]]


design=[qsg,olhl,onnhvg,jrlk,bhsums,oednti,aapttm,awrp,yxlzu,ynlt,lew,amd,mpsyg]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3"))

### END