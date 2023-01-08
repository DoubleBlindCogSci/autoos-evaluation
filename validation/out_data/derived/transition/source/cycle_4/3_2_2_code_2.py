from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
guy = Factor("guy", ["rtnabe","xpkjko","ctc","sdv","egjb","lhdxe","ztpvlx","kgm"])
ooagz = Factor("ooagz", ["cxkdhe","gbxv","jiyrm","kolng","tzyoei","iazcku","jll"])
def is_sjkko_cmidw(guy, ooagz):
    return guy[-1] == "egjb" and ooagz[0] != "cxkdhe"
def is_sjkko_fncgbm(guy, ooagz):
    return guy[-1] != "egjb" and ooagz[0] == "cxkdhe"
def is_sjkko_ila(guy, ooagz):
    return not (is_sjkko_cmidw(guy, ooagz) or is_sjkko_fncgbm(guy, ooagz))
sjkko = Factor("sjkko", [DerivedLevel("cmidw", Transition(is_sjkko_cmidw, [guy, ooagz])), DerivedLevel("fncgbm", Transition(is_sjkko_fncgbm, [guy, ooagz])), DerivedLevel("ila", Transition(is_sjkko_ila, [guy, ooagz]))])

design=[guy,ooagz,sjkko]
crossing=[sjkko]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END