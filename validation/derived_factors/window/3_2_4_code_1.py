from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jifmc = Factor("jifmc", ["njln","gzz","stnk","ylbkuh","bhr","sesr","gdupd","nxta"])
hasycl = Factor("hasycl", ["njln","gzz","stnk","ylbkuh","bhr","sesr","gdupd","nxta"])
cydh = Factor("cydh", ["njln","gzz","stnk","ylbkuh","bhr","sesr","gdupd","nxta"])
def oakuy(jifmc, hasycl, cydh):
     return hasycl[-1] == jifmc[0] and jifmc[-1] != cydh[0]
def hwthv(jifmc, hasycl, cydh):
     return hasycl[-1] != jifmc[0] and cydh[0] == jifmc[-1]
def bhus(jifmc, hasycl, cydh):
     return (jifmc[0] != hasycl[-1]) and (not hwthv(jifmc, hasycl, cydh))
tbeo = DerivedLevel("jieox", Window(oakuy, [jifmc, hasycl, cydh],2,1))
jbx = DerivedLevel("cnnrmc", Window(hwthv, [jifmc, hasycl, cydh],2,1))
ppqe = DerivedLevel("hfyt", Window(bhus, [jifmc, hasycl, cydh],2,1))
qpjya = Factor("yysx", [tbeo, jbx, ppqe])

### EXPERIMENT
design=[jifmc,hasycl,cydh,qpjya]
crossing=[qpjya]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END