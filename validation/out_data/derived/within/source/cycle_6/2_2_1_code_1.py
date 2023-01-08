from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qvno = Factor("qvno", ["jgmlk","lmd","wmi","pnlq","lhwdzz"])
yqskm = Factor("yqskm", ["jgmlk","lmd","wmi","pnlq","lhwdzz"])
hrl = Factor("hrl", ["jgmlk","lmd","wmi","pnlq","lhwdzz"])
def jwy(qvno, hrl, yqskm):
    return qvno != hrl
def uqyi(qvno, hrl, yqskm):
    return qvno == hrl
zic = Factor("rcq", [DerivedLevel("tclmcm", WithinTrial(jwy, [qvno, yqskm, hrl])), DerivedLevel("pihm", WithinTrial(uqyi, [qvno, yqskm, hrl]))])
### EXPERIMENT
design=[qvno,yqskm,hrl,zic]
crossing=[zic]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END