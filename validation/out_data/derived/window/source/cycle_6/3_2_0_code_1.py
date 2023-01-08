from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
egwrq = Factor("egwrq", ["llu","xyis","sjmq","klfis","jjd","ttsjj"])
sgrux = Factor("sgrux", ["llu","xyis","sjmq","klfis","jjd","ttsjj"])
vgzhs = Factor("vgzhs", ["llu","xyis","sjmq","klfis","jjd","ttsjj"])
def tupqc(egwrq, sgrux, vgzhs):
     return sgrux[0] == egwrq[-1] and egwrq[0] != vgzhs[-1]
def ngdnu(egwrq, sgrux, vgzhs):
     return sgrux[0] != egwrq[-1] and egwrq[0] == vgzhs[-1]
def toku(egwrq, sgrux, vgzhs):
     return (not egwrq[-1] == sgrux[0]) and (egwrq[0] != vgzhs[-1])
qrpuio = DerivedLevel("svi", Window(tupqc, [egwrq, sgrux, vgzhs],2,1))
tbxp = DerivedLevel("wkej", Window(ngdnu, [egwrq, sgrux, vgzhs],2,1))
ldf = DerivedLevel("sugtp", Window(toku, [egwrq, sgrux, vgzhs],2,1))
qhr = Factor("uheab", [qrpuio, tbxp, ldf])

### EXPERIMENT
design=[egwrq,sgrux,vgzhs,qhr]
crossing=[qhr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END