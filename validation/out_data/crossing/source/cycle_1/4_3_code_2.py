from sweetpea import *
import os
_dir=os.path.dirname(__file__)
iemv = Factor("iemv", ["isij", "qoooek"])
fum = Factor("fum", ["zgxqg", "erbdje"])
wclgu = Factor("wclgu", ["tgft", "vwkac"])
kdidwf = Factor("kdidwf", ["mfkw", "invtsc"])
pdodv = Factor("pdodv", ["bkgwzs", "avb"])
tgz = Factor("tgz", ["bqs", "bsa"])
cdwpvu = Factor("cdwpvu", ["twuje", "jgckv"])
ordv = Factor("ordv", ["hzca", "efwiof"])
lwe = Factor("lwe", ["vui", "klsqys"])
ufkn = Factor("ufkn", ["ovm", "xnqmvq"])
lqfm = Factor("lqfm", ["taotot", "jkjtj"])
acx = Factor("acx", ["ynupos", "kyl"])
sswl = Factor("sswl", ["fqvfl", "chmr"])
blt = Factor("blt", ["ndzbe", "eviqaw"])
constraints = []
crossing = [[iemv, fum, wclgu], [kdidwf, pdodv, tgz], [cdwpvu, ordv, lwe, ufkn], [lqfm, acx, sswl, blt]]


design=[iemv,fum,wclgu,kdidwf,pdodv,tgz,cdwpvu,ordv,lwe,ufkn,lqfm,acx,sswl,blt]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3"))

### END