from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
uqwxh = Factor("uqwxh", ["bixpkk","kkf","yjxjug","yurjl","asss","snqm","yjy","rssmp"])
vwoe = Factor("vwoe", ["bixpkk","kkf","yjxjug","yurjl","asss","snqm","yjy","rssmp"])
ckstue = Factor("ckstue", ["bixpkk","kkf","yjxjug","yurjl","asss","snqm","yjy","rssmp"])
def kzmmbm(uqwxh, ckstue, vwoe):
     return uqwxh[-3] == ckstue[0] and uqwxh[0] != vwoe[-3]
def uobo(uqwxh, ckstue, vwoe):
     return ckstue[0] != uqwxh[-3] and uqwxh[0] == vwoe[-3]
def cko(uqwxh, ckstue, vwoe):
     return (not kzmmbm(uqwxh, ckstue, vwoe)) and (not uobo(uqwxh, ckstue, vwoe))
uwai = DerivedLevel("mfqks", Window(kzmmbm, [uqwxh, vwoe, ckstue],4,1))
ndbbht = DerivedLevel("ifgsok", Window(uobo, [uqwxh, vwoe, ckstue],4,1))
rzpw = DerivedLevel("xywkiw", Window(cko, [uqwxh, vwoe, ckstue],4,1))
ehagiv = Factor("kjq", [uwai, ndbbht, rzpw])

### EXPERIMENT
design=[uqwxh,vwoe,ckstue,ehagiv]
crossing=[ehagiv]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END