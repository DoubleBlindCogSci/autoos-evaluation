from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hcwy = Factor("hcwy", ["rts","furb","mutfqd","zqowsh","ytm","ivhzdn","hvqke","stoh"])
mhcn = Factor("mhcn", ["rts","furb","mutfqd","zqowsh","ytm","ivhzdn","hvqke","stoh"])
wnsekp = Factor("wnsekp", ["rts","furb","mutfqd","zqowsh","ytm","ivhzdn","hvqke","stoh"])
def is_tqfiyn_poqmg(hcwy, mhcn, wnsekp):
    return mhcn[-1] == hcwy[0] and hcwy[-1] != wnsekp[0]
def is_tqfiyn_vgrgin(hcwy, mhcn, wnsekp):
    return mhcn[-1] != hcwy[0] and hcwy[-1] == wnsekp[0]
def is_tqfiyn_wxp(hcwy, mhcn, wnsekp):
    return not (is_tqfiyn_poqmg(hcwy, mhcn, wnsekp) or is_tqfiyn_vgrgin(hcwy, mhcn, wnsekp))
tqfiyn = Factor("tqfiyn", [DerivedLevel("poqmg", Transition(is_tqfiyn_poqmg, [hcwy, mhcn, wnsekp])), DerivedLevel("vgrgin", Transition(is_tqfiyn_vgrgin, [hcwy, mhcn, wnsekp])), DerivedLevel("wxp", Transition(is_tqfiyn_wxp, [hcwy, mhcn, wnsekp]))])

design=[hcwy,mhcn,wnsekp,tqfiyn]
crossing=[tqfiyn]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END