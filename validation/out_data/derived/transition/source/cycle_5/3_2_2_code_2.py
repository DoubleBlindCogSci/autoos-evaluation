from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cyovro = Factor("cyovro", ["wbde","qnjs","lzto","yxvnmb","gsxfcz","zldecv","mdke"])
qoyk = Factor("qoyk", ["wbde","qnjs","lzto","yxvnmb","gsxfcz","zldecv","mdke"])
zjgjio = Factor("zjgjio", ["wbde","qnjs","lzto","yxvnmb","gsxfcz","zldecv","mdke"])
def is_qfzc_pgc(qoyk, cyovro, zjgjio):
    return qoyk[-1] == cyovro[0] and cyovro[-1] != zjgjio[0]
def is_qfzc_efgfn(qoyk, cyovro, zjgjio):
    return qoyk[-1] != cyovro[0] and cyovro[-1] == zjgjio[0]
def is_qfzc_avaxq(qoyk, cyovro, zjgjio):
    return qoyk[-1] != cyovro[0] and cyovro[-1] != zjgjio[0]
qfzc = Factor("qfzc", [DerivedLevel("pgc", Transition(is_qfzc_pgc, [qoyk, cyovro, zjgjio])), DerivedLevel("efgfn", Transition(is_qfzc_efgfn, [qoyk, cyovro, zjgjio])), DerivedLevel("avaxq", Transition(is_qfzc_avaxq, [qoyk, cyovro, zjgjio]))])

design=[cyovro,qoyk,zjgjio,qfzc]
crossing=[qfzc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END