from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bzz = Factor("bzz", ["wvupc","qyioa","qtkhy","afqm","ttvo","rfpltw","xyb","iri"])
wuan = Factor("wuan", ["wvupc","qyioa","qtkhy","afqm","ttvo","rfpltw","xyb","iri"])
tbbie = Factor("tbbie", ["wvupc","qyioa","qtkhy","afqm","ttvo","rfpltw","xyb","iri"])
def qseewp(bzz, wuan, tbbie):
     return bzz[0] == wuan[-1] and bzz[-1] != tbbie[0]
def iauil(bzz, wuan, tbbie):
     return wuan[-1] != bzz[0] and bzz[-1] == tbbie[0]
def qzls(bzz, wuan, tbbie):
     return (not qseewp(bzz, wuan, tbbie)) and (bzz[-1] != tbbie[0])
xsg = DerivedLevel("kavhih", Transition(qseewp, [bzz, wuan, tbbie]))
lfz = DerivedLevel("ytt", Transition(iauil, [bzz, wuan, tbbie]))
rnpouz = DerivedLevel("wcaqvo", Transition(qzls, [bzz, wuan, tbbie]))
llrmt = Factor("mbgo", [xsg, lfz, rnpouz])

### EXPERIMENT
design=[bzz,wuan,tbbie,llrmt]
crossing=[llrmt]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_0"))
### END