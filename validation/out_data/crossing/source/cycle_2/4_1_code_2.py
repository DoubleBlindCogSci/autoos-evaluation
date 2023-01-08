from sweetpea import *
import os
_dir=os.path.dirname(__file__)
jaad = Factor("jaad", ["zdw", "egt"])
izjsng = Factor("izjsng", ["ydv", "nqzuhf"])
dadeg = Factor("dadeg", ["sjn", "nvhy"])
owik = Factor("owik", ["bic", "fys"])
njazq = Factor("njazq", ["wsxtk", "ngaws"])
rtkgin = Factor("rtkgin", ["dvt", "ilyuzp"])
upfqk = Factor("upfqk", ["nvm", "jendlv"])
kbsh = Factor("kbsh", ["kmar", "mqatb"])
ify = Factor("ify", ["wgwuat", "jbexl"])
wwrrg = Factor("wwrrg", ["npx", "qvdrb"])
lgcedy = Factor("lgcedy", ["ubcqfm", "izshjk"])
fcyhmw = Factor("fcyhmw", ["wcr", "rrm"])
iuc = Factor("iuc", ["nmus", "ytk"])
constraints = []
crossing = [[jaad, izjsng], [dadeg, owik, njazq, rtkgin], [upfqk, kbsh, ify], [wwrrg, lgcedy, fcyhmw, iuc]]


design=[jaad,izjsng,dadeg,owik,njazq,rtkgin,upfqk,kbsh,ify,wwrrg,lgcedy,fcyhmw,iuc]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1"))

### END