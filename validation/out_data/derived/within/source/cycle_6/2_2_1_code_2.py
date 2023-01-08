from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qvno = Factor("qvno", ["jgmlk","lmd","wmi","pnlq","lhwdzz"])
yqskm = Factor("yqskm", ["jgmlk","lmd","wmi","pnlq","lhwdzz"])
hrl = Factor("hrl", ["jgmlk","lmd","wmi","pnlq","lhwdzz"])
def is_rcq_tclmcm(qvno, yqskm, hrl):
    return qvno != hrl
def is_rcq_pihm(qvno, yqskm, hrl):
    return not is_rcq_tclmcm(qvno, yqskm, hrl)
rcq = Factor("rcq", [DerivedLevel("tclmcm", WithinTrial(is_rcq_tclmcm, [qvno, yqskm, hrl])), DerivedLevel("pihm", WithinTrial(is_rcq_pihm, [qvno, yqskm, hrl]))])

design=[qvno,yqskm,hrl,rcq]
crossing=[rcq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END