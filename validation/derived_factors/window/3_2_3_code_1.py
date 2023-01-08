from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ooox = Factor("ooox", ["yzcvnr","cfyizy","hes","qnez","sliev","bosm","rkx"])
plmzac = Factor("plmzac", ["yzcvnr","cfyizy","hes","qnez","sliev","bosm","rkx"])
xwlxbv = Factor("xwlxbv", ["yzcvnr","cfyizy","hes","qnez","sliev","bosm","rkx"])
def dooc(ooox, xwlxbv, plmzac):
     return ooox[-1] == xwlxbv[-2] and ooox[-2] != plmzac[-1]
def pma(ooox, xwlxbv, plmzac):
     return xwlxbv[-2] != ooox[-1] and plmzac[-1] == ooox[-2]
def bqo(ooox, xwlxbv, plmzac):
     return (ooox[-1] != xwlxbv[-2]) and (not pma(ooox, xwlxbv, plmzac))
ilgksd = DerivedLevel("aldchc", Window(dooc, [ooox, plmzac, xwlxbv],3,1))
whbkkh = DerivedLevel("xlzynf", Window(pma, [ooox, plmzac, xwlxbv],3,1))
ren = DerivedLevel("omb", Window(bqo, [ooox, plmzac, xwlxbv],3,1))
nhuo = Factor("seqkw", [ilgksd, whbkkh, ren])

### EXPERIMENT
design=[ooox,plmzac,xwlxbv,nhuo]
crossing=[nhuo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END