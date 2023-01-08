from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cyovro = Factor("cyovro", ["wbde","qnjs","lzto","yxvnmb","gsxfcz","zldecv","mdke"])
qoyk = Factor("qoyk", ["wbde","qnjs","lzto","yxvnmb","gsxfcz","zldecv","mdke"])
zjgjio = Factor("zjgjio", ["wbde","qnjs","lzto","yxvnmb","gsxfcz","zldecv","mdke"])
def sjxel(cyovro, qoyk, zjgjio):
     return qoyk[-1] == cyovro[0] and cyovro[-1] != zjgjio[0]
def axnc(cyovro, qoyk, zjgjio):
     return qoyk[-1] != cyovro[0] and cyovro[-1] == zjgjio[0]
def eykatp(cyovro, qoyk, zjgjio):
     return (not sjxel(cyovro, qoyk, zjgjio)) and (not cyovro[-1] == zjgjio[0])
afliw = DerivedLevel("pgc", Transition(sjxel, [cyovro, qoyk, zjgjio]))
qhw = DerivedLevel("efgfn", Transition(axnc, [cyovro, qoyk, zjgjio]))
nsi = DerivedLevel("avaxq", Transition(eykatp, [cyovro, qoyk, zjgjio]))
fho = Factor("qfzc", [afliw, qhw, nsi])

### EXPERIMENT
design=[cyovro,qoyk,zjgjio,fho]
crossing=[fho]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END