from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vbjxsn = Factor("vbjxsn", ["wdbc","vvqt","sgn","mkxoap","xetve","pauc","budg","vrisak"])
def qgrnb(vbjxsn):
     return vbjxsn[0] == "mkxoap" and not vbjxsn[-3] == "mkxoap"
def ilgjn(vbjxsn):
     return vbjxsn[0] != "mkxoap" and  vbjxsn[-3] == "sgn"
def lwhro(vbjxsn):
     return (vbjxsn[0] != "mkxoap") and (vbjxsn[-3] != "sgn")
lwgmn = DerivedLevel("jdxtz", Window(qgrnb, [vbjxsn],4,1))
nqen = DerivedLevel("odq", Window(ilgjn, [vbjxsn],4,1))
tzzes = DerivedLevel("dps", Window(lwhro, [vbjxsn],4,1))
qvuwl = Factor("vgjlr", [lwgmn, nqen, tzzes])

### EXPERIMENT
design=[vbjxsn,qvuwl]
crossing=[qvuwl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END