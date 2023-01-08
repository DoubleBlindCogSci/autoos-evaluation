from sweetpea import *
import os
_dir=os.path.dirname(__file__)
pskm = Factor("pskm", ["qyfi", "lbgpxh"])
gvrb = Factor("gvrb", ["fgga", "mzyjc"])
layijh = Factor("layijh", ["qqag", "jpcc"])
txyx = Factor("txyx", ["dkz", "aqwho"])
cmroqn = Factor("cmroqn", ["vazbo", "jjv"])
hqebl = Factor("hqebl", ["hgmkpq", "lrqd"])
shpzn = Factor("shpzn", ["xxjjwh", "klfswg"])
gew = Factor("gew", ["wrlow", "mlawg"])
jznr = Factor("jznr", ["sdc", "sboxd"])
yulqsk = Factor("yulqsk", ["tstpr", "qovok"])
dtpt = Factor("dtpt", ["bbva", "fpw"])
syp = Factor("syp", ["fvd", "vznm"])
yeykw = Factor("yeykw", ["jlvmd", "njtm"])
mckky = Factor("mckky", ["ftsvmu", "yjv"])
constraints = []
crossing = [[pskm, gvrb], [layijh, txyx, cmroqn, hqebl], [shpzn, gew], [jznr], [yulqsk, dtpt], [syp, yeykw, mckky]]


design=[pskm,gvrb,layijh,txyx,cmroqn,hqebl,shpzn,gew,jznr,yulqsk,dtpt,syp,yeykw,mckky]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_3"))

### END