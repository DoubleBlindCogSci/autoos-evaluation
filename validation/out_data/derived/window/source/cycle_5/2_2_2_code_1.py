from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dhrnfc = Factor("dhrnfc", ["dav","onhc","rpl","lmj","kxolk"])
exxlpg = Factor("exxlpg", ["dav","onhc","rpl","lmj","kxolk"])
hbrqgi = Factor("hbrqgi", ["dav","onhc","rpl","lmj","kxolk"])
def vwnse(dhrnfc, exxlpg, hbrqgi):
    return dhrnfc[-1] == exxlpg[-2] or dhrnfc[-2] == hbrqgi[-1]
def dvefb(dhrnfc, exxlpg, hbrqgi):
    return dhrnfc[-1] != exxlpg[-2] and not (dhrnfc[-2] == hbrqgi[-1])
zjha = Factor("vmgfeo", [DerivedLevel("dbuz", Window(vwnse, [dhrnfc, exxlpg, hbrqgi],3,1)), DerivedLevel("iztnz", Window(dvefb, [dhrnfc, exxlpg, hbrqgi],3,1))])
### EXPERIMENT
design=[dhrnfc,exxlpg,hbrqgi,zjha]
crossing=[zjha]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END