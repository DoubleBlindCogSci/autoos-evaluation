from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tgyp = Factor("tgyp", ["jvy","kamjzt","pxaz","fuboj","wsa","buisa","rekfxs"])
izn = Factor("izn", ["trh","blzzdh","vmc","jxwuke","wxn","iof","depihe"])
def wbmgo(tgyp, izn):
     return "wsa" == tgyp[-3] and not izn[0] == "vmc"
def hemil(tgyp, izn):
     return tgyp[-3] != "wsa" and  izn[0] == "vmc"
def tlsqyj(tgyp, izn):
     return (tgyp[-3] != "wsa") and (not hemil(tgyp, izn))
zdpoz = DerivedLevel("zvo", Window(wbmgo, [tgyp, izn],4,1))
kixks = DerivedLevel("fhvwfc", Window(hemil, [tgyp, izn],4,1))
ceb = DerivedLevel("bxig", Window(tlsqyj, [tgyp, izn],4,1))
ztiwqt = Factor("hxtank", [zdpoz, kixks, ceb])

### EXPERIMENT
design=[tgyp,izn,ztiwqt]
crossing=[ztiwqt]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END