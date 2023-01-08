from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dbco = Factor("dbco", ["hzkwtm","feme","vfv","meulmi","tjtd","xfiqt","qryxq","ivbakq"])
ftoy = Factor("ftoy", ["hzkwtm","feme","vfv","meulmi","tjtd","xfiqt","qryxq","ivbakq"])
sfquoi = Factor("sfquoi", ["hzkwtm","feme","vfv","meulmi","tjtd","xfiqt","qryxq","ivbakq"])
def ugbok(dbco, sfquoi, ftoy):
     return sfquoi == dbco
def msaed(dbco, sfquoi, ftoy):
     return sfquoi != dbco and dbco == ftoy
def gwg(dbco, sfquoi, ftoy):
     return (dbco != sfquoi) and (dbco != ftoy)
ardz = DerivedLevel("kgusrl", WithinTrial(ugbok, [dbco, ftoy, sfquoi]))
cdovtg = DerivedLevel("jtdph", WithinTrial(msaed, [dbco, ftoy, sfquoi]))
ffolrn = DerivedLevel("akj", WithinTrial(gwg, [dbco, ftoy, sfquoi]))
wvtra = Factor("itd", [ardz, cdovtg, ffolrn])

### EXPERIMENT
design=[dbco,ftoy,sfquoi,wvtra]
crossing=[wvtra]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END