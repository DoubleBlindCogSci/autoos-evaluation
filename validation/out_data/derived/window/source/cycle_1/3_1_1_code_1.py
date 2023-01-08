from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qbxrsc = Factor("qbxrsc", ["zxari","onc","zsbmrx","lgga","mrs","tqt","qxfhwx","uqpib"])
def sopu(qbxrsc):
     return qbxrsc[-3] == "zsbmrx"
def qqcgi(qbxrsc):
     return qbxrsc[0] == "qxfhwx"
def iqj(qbxrsc):
     return (qbxrsc[-3] != "zsbmrx") and (qbxrsc[0] != "qxfhwx")
cxlu = Factor("jtk", [DerivedLevel("eabp", Window(sopu, [qbxrsc],4,1)), DerivedLevel("csw", Window(qqcgi, [qbxrsc],4,1)),DerivedLevel("zjiomh", Window(iqj, [qbxrsc],4,1))])
### EXPERIMENT
design=[qbxrsc,cxlu]
crossing=[cxlu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END