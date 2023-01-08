from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qbxrsc= Factor("qbxrsc", ["zxari","onc","zsbmrx","lgga","mrs","tqt","qxfhwx","uqpib"])
def is_jtk_eabp(qbxrsc):
    return qbxrsc[0] == qbxrsc[-3]
def is_jtk_csw(qbxrsc):
    return qbxrsc[0] == qbxrsc[-1]
def is_jtk_zjiomh(qbxrsc):
    return not (is_jtk_eabp(qbxrsc) or is_jtk_csw(qbxrsc))
jtk= Factor("jtk", [DerivedLevel("eabp", Window(is_jtk_eabp, [qbxrsc], 4, 1)), DerivedLevel("csw", Window(is_jtk_csw, [qbxrsc], 4, 1)), DerivedLevel("zjiomh", Window(is_jtk_zjiomh, [qbxrsc], 4, 1))])

design=[qbxrsc,jtk]
crossing=[jtk]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END
