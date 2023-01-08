from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qha = Factor("qha", ["wdq", "iqa"])
jbu = Factor("jbu", ["mqs", "rser"])
psj = Factor("psj", ["gno", "omln"])
fod = Factor("fod", ["jpzc", "kias"])
ledros = Factor("ledros", ["uknau", "byf"])
fcs = Factor("fcs", ["nnczm", "diq"])
cftisd = Factor("cftisd", ["sbidgy", "wpkghw"])
dmeeb = Factor("dmeeb", ["vyg", "wulrex"])
tmb = Factor("tmb", ["vetd", "mvnk"])
alsj = Factor("alsj", ["tbb", "soktwa"])
aew = Factor("aew", ["mvz", "ful"])
xlo = Factor("xlo", ["mwib", "dnvhyb"])
vytrfn = Factor("vytrfn", ["mqmor", "otyoje"])
bne = Factor("bne", ["zyqcat", "nuhrml"])

### EXPERIMENT
design=[qha,jbu,psj,fod,ledros,fcs,cftisd,dmeeb,tmb,alsj,aew,xlo,vytrfn,bne]
crossing=[[qha,jbu,psj],[fod,ledros,fcs],[cftisd,dmeeb,tmb,alsj],[aew,xlo,vytrfn,bne],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1"))
### END