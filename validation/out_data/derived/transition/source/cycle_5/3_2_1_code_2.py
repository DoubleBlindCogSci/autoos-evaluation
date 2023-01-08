from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mkepe = Factor("mkepe", ["ccp","jgigw","mhfhy","qask","rzj","efzx"])
ytw = Factor("ytw", ["ccp","jgigw","mhfhy","qask","rzj","efzx"])
nbv = Factor("nbv", ["ccp","jgigw","mhfhy","qask","rzj","efzx"])
def is_vkv_vqhjwa(mkepe, ytw, nbv):
    return ytw[-1] == mkepe[0] and mkepe[-1] != nbv[0]
def is_vkv_xphfj(mkepe, ytw, nbv):
    return ytw[-1] != mkepe[0] and mkepe[-1] == nbv[0]
def is_vkv_vjxgzr(mkepe, ytw, nbv):
    return ytw[-1] != mkepe[0] and mkepe[-1] != nbv[0]
vkv = Factor("vkv", [DerivedLevel("vqhjwa", Transition(is_vkv_vqhjwa, [mkepe, ytw, nbv])), DerivedLevel("xphfj", Transition(is_vkv_xphfj, [mkepe, ytw, nbv])), DerivedLevel("vjxgzr", Transition(is_vkv_vjxgzr, [mkepe, ytw, nbv]))])

design=[mkepe,ytw,nbv,vkv]
crossing=[vkv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END