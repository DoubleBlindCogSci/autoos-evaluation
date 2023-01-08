from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mes = Factor("mes", ["vvmbzw","hbj","uhi","cuetl","cvk","fgar","hilp"])
def zrqhv(mes):
     return mes[0] == "hbj" and not mes[-1] == "fgar"
def tzhvd(mes):
     return (not "hbj" != mes[0]) and  mes[-1] == "fgar"
def tgztx(mes):
     return (not mes[0] == "hbj") and (not tzhvd(mes))
vjahbn = Factor("hrsqjf", [DerivedLevel("hvrwc", Transition(zrqhv, [mes])), DerivedLevel("fhi", Transition(tzhvd, [mes])),DerivedLevel("oxtbkp", Transition(tgztx, [mes]))])
### EXPERIMENT
design=[mes,vjahbn]
crossing=[vjahbn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_2"))
### END