from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vbjxsn= Factor("vbjxsn", ["wdbc","vvqt","sgn","mkxoap","xetve","pauc","budg","vrisak"])
def is_vgjlr_jdxtz(vbjxsn):
    return vbjxsn[0] == "mkxoap" and vbjxsn[-3] != "mkxoap"
def is_vgjlr_odq(vbjxsn):
    return vbjxsn[0] != "mkxoap" and vbjxsn[-3] == "sgn"
def is_vgjlr_dps(vbjxsn):
    return not (is_vgjlr_jdxtz(vbjxsn) or is_vgjlr_odq(vbjxsn))
vgjlr= Factor("vgjlr", [DerivedLevel("jdxtz", Window(is_vgjlr_jdxtz, [vbjxsn], 4, 1)), DerivedLevel("odq", Window(is_vgjlr_odq, [vbjxsn], 4, 1)), DerivedLevel("dps", Window(is_vgjlr_dps, [vbjxsn], 4, 1))])

design=[vbjxsn, vgjlr]
crossing=[vgjlr]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END
