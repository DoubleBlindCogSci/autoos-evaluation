from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bzz = Factor("bzz", ["wvupc","qyioa","qtkhy","afqm","ttvo","rfpltw","xyb","iri"])
wuan = Factor("wuan", ["wvupc","qyioa","qtkhy","afqm","ttvo","rfpltw","xyb","iri"])
tbbie = Factor("tbbie", ["wvupc","qyioa","qtkhy","afqm","ttvo","rfpltw","xyb","iri"])
def is_mbgo_kavhih(bzz, wuan, tbbie):
    return bzz[0] == wuan[-1] and bzz[-1] != tbbie[0]
def is_mbgo_ytt(bzz, wuan, tbbie):
    return wuan[-1] != bzz[0] and bzz[-1] == tbbie[0]
def is_mbgo_wcaqvo(bzz, wuan, tbbie):
    return not (is_mbgo_kavhih(bzz, wuan, tbbie) or is_mbgo_ytt(bzz, wuan, tbbie))
mbgo = Factor("mbgo", [DerivedLevel("kavhih", Transition(is_mbgo_kavhih, [bzz, wuan, tbbie])), DerivedLevel("ytt", Transition(is_mbgo_ytt, [bzz, wuan, tbbie])), DerivedLevel("wcaqvo", Transition(is_mbgo_wcaqvo, [bzz, wuan, tbbie]))])

design=[bzz,wuan,tbbie,mbgo]
crossing=[mbgo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END