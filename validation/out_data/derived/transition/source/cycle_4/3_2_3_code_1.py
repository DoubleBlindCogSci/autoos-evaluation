from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hcwy = Factor("hcwy", ["rts","furb","mutfqd","zqowsh","ytm","ivhzdn","hvqke","stoh"])
mhcn = Factor("mhcn", ["rts","furb","mutfqd","zqowsh","ytm","ivhzdn","hvqke","stoh"])
wnsekp = Factor("wnsekp", ["rts","furb","mutfqd","zqowsh","ytm","ivhzdn","hvqke","stoh"])
def qazj(hcwy, mhcn, wnsekp):
     return mhcn[-1] == hcwy[0] and hcwy[-1] != wnsekp[0]
def tdzlj(hcwy, mhcn, wnsekp):
     return mhcn[-1] != hcwy[0] and hcwy[-1] == wnsekp[0]
def ucwav(hcwy, mhcn, wnsekp):
     return (hcwy[0] != mhcn[-1]) and (hcwy[-1] != wnsekp[0])
qkzfmn = Factor("tqfiyn", [DerivedLevel("poqmg", Transition(qazj, [hcwy, mhcn, wnsekp])), DerivedLevel("vgrgin", Transition(tdzlj, [hcwy, mhcn, wnsekp])),DerivedLevel("wxp", Transition(ucwav, [hcwy, mhcn, wnsekp]))])
### EXPERIMENT
design=[hcwy,mhcn,wnsekp,qkzfmn]
crossing=[qkzfmn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END