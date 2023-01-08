from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
guy = Factor("guy", ["rtnabe","xpkjko","ctc","sdv","egjb","lhdxe","ztpvlx","kgm"])
ooagz = Factor("ooagz", ["cxkdhe","gbxv","jiyrm","kolng","tzyoei","iazcku","jll"])
def whkm(guy, ooagz):
     return "egjb" == guy[-1] and not ooagz[0] == "cxkdhe"
def mky(guy, ooagz):
     return guy[-1] != "egjb" and ooagz[0] == "cxkdhe"
def xseihr(guy, ooagz):
     return (not whkm(guy, ooagz)) and (not mky(guy, ooagz))
hsk = DerivedLevel("cmidw", Transition(whkm, [guy, ooagz]))
vvhnc = DerivedLevel("fncgbm", Transition(mky, [guy, ooagz]))
xlv = DerivedLevel("ila", Transition(xseihr, [guy, ooagz]))
qugixe = Factor("sjkko", [hsk, vvhnc, xlv])

### EXPERIMENT
design=[guy,ooagz,qugixe]
crossing=[qugixe]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END