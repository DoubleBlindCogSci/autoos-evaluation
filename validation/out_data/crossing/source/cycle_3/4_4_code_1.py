from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dgnaub = Factor("dgnaub", ["kklua", "xpmns"])
tfaro = Factor("tfaro", ["jxcj", "jfwo"])
manzxm = Factor("manzxm", ["fzc", "xsfb"])
ped = Factor("ped", ["ksrxsh", "xirv"])
jlj = Factor("jlj", ["lnvgdl", "xnuoq"])
fonstm = Factor("fonstm", ["rmhl", "tehvak"])
liebp = Factor("liebp", ["nufeno", "bktzf"])
xhzlgr = Factor("xhzlgr", ["tifz", "fnejf"])
zvlsr = Factor("zvlsr", ["cik", "umo"])
bfgx = Factor("bfgx", ["xchb", "ijxg"])
petb = Factor("petb", ["aejq", "wtljsw"])
doucj = Factor("doucj", ["xuco", "yyxa"])
xaz = Factor("xaz", ["lnanh", "hcltqz"])
fesx = Factor("fesx", ["rcfo", "mprq"])

### EXPERIMENT
design=[dgnaub,tfaro,manzxm,ped,jlj,fonstm,liebp,xhzlgr,zvlsr,bfgx,petb,doucj,xaz,fesx]
crossing=[[dgnaub,tfaro,manzxm],[ped,jlj,fonstm],[liebp,xhzlgr,zvlsr,bfgx],[petb,doucj,xaz,fesx],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_4"))
### END