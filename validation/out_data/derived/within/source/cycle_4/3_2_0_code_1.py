from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
epjvsp = Factor("epjvsp", ["lub","ofc","cfuj","wkah","vlrfg","uzqq","kcbik"])
vfowp = Factor("vfowp", ["runks","rpaaj","gsat","ekm","gie","vty","jgzgd"])
def swhd(epjvsp, vfowp):
     return epjvsp == "vlrfg"
def grvnc(epjvsp, vfowp):
     return "vlrfg" != epjvsp and  vfowp == "gsat"
def yklzn(epjvsp, vfowp):
     return (not epjvsp == "vlrfg") and (not grvnc(epjvsp, vfowp))
syme = DerivedLevel("rcvuob", WithinTrial(swhd, [epjvsp, vfowp]))
ijtcan = DerivedLevel("ympx", WithinTrial(grvnc, [epjvsp, vfowp]))
egtj = DerivedLevel("vqro", WithinTrial(yklzn, [epjvsp, vfowp]))
qaodrv = Factor("zdao", [syme, ijtcan, egtj])

### EXPERIMENT
design=[epjvsp,vfowp,qaodrv]
crossing=[qaodrv]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END