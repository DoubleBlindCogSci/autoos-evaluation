from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
egwrq = Factor("egwrq", ["llu","xyis","sjmq","klfis","jjd","ttsjj"])
sgrux = Factor("sgrux", ["llu","xyis","sjmq","klfis","jjd","ttsjj"])
vgzhs = Factor("vgzhs", ["llu","xyis","sjmq","klfis","jjd","ttsjj"])
def is_uheab_svi(sgrux, egwrq, vgzhs):
    return sgrux[0] == egwrq[-1] and egwrq[0] != vgzhs[-1]
def is_uheab_wkej(sgrux, egwrq, vgzhs):
    return sgrux[0] != egwrq[-1] and egwrq[0] == vgzhs[-1]
def is_uheab_sugtp(sgrux, egwrq, vgzhs):
    return not (is_uheab_svi(sgrux, egwrq, vgzhs) or is_uheab_wkej(sgrux, egwrq, vgzhs))
uheab = Factor("uheab", [DerivedLevel("svi", Window(is_uheab_svi, [sgrux, egwrq, vgzhs], 2, 1)), DerivedLevel("wkej", Window(is_uheab_wkej, [sgrux, egwrq, vgzhs], 2, 1)), DerivedLevel("sugtp", Window(is_uheab_sugtp, [sgrux, egwrq, vgzhs], 2, 1))])

design=[egwrq,sgrux,vgzhs,uheab]
crossing=[uheab]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END