from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dbco= Factor("dbco", ["hzkwtm","feme","vfv","meulmi","tjtd","xfiqt","qryxq","ivbakq"])
ftoy= Factor("ftoy", ["hzkwtm","feme","vfv","meulmi","tjtd","xfiqt","qryxq","ivbakq"])
sfquoi= Factor("sfquoi", ["hzkwtm","feme","vfv","meulmi","tjtd","xfiqt","qryxq","ivbakq"])
def is_itd_kgusrl(dbco, ftoy, sfquoi):
    return sfquoi == dbco
def is_itd_jtdph(dbco, ftoy, sfquoi):
    return sfquoi != dbco and dbco == ftoy
def is_itd_akj(dbco, ftoy, sfquoi):
    return sfquoi != dbco and dbco != ftoy
itd= Factor("itd", [DerivedLevel("kgusrl", WithinTrial(is_itd_kgusrl, [dbco, ftoy, sfquoi])), DerivedLevel("jtdph", WithinTrial(is_itd_jtdph, [dbco, ftoy, sfquoi])), DerivedLevel("akj", WithinTrial(is_itd_akj, [dbco, ftoy, sfquoi]))])

design=[dbco,ftoy,sfquoi, itd]
crossing=[itd]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END
