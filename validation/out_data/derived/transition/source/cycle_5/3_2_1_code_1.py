from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mkepe = Factor("mkepe", ["ccp","jgigw","mhfhy","qask","rzj","efzx"])
ytw = Factor("ytw", ["ccp","jgigw","mhfhy","qask","rzj","efzx"])
nbv = Factor("nbv", ["ccp","jgigw","mhfhy","qask","rzj","efzx"])
def kwoas(mkepe, ytw, nbv):
     return ytw[-1] == mkepe[0] and mkepe[-1] != nbv[0]
def vvx(mkepe, ytw, nbv):
     return ytw[-1] != mkepe[0] and mkepe[-1] == nbv[0]
def qedi(mkepe, ytw, nbv):
     return (mkepe[0] != ytw[-1]) and (mkepe[-1] != nbv[0])
hlwxkh = Factor("vkv", [DerivedLevel("vqhjwa", Transition(kwoas, [mkepe, ytw, nbv])), DerivedLevel("xphfj", Transition(vvx, [mkepe, ytw, nbv])),DerivedLevel("vjxgzr", Transition(qedi, [mkepe, ytw, nbv]))])
### EXPERIMENT
design=[mkepe,ytw,nbv,hlwxkh]
crossing=[hlwxkh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END