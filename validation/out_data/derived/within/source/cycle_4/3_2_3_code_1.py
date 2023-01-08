from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vrq = Factor("vrq", ["dgxe","fngdhc","yreu","wbw","eizq","zhh"])
ouics = Factor("ouics", ["hvjfh","yoibhb","fuaex","aoc","xykbw","wunj"])
def bbrveh(vrq, ouics):
     return vrq == "eizq"
def bhsp(vrq, ouics):
     return "eizq" != vrq and  ouics == "wunj"
def rpb(vrq, ouics):
     return (not vrq == "eizq") and (ouics != "wunj")
gypmm = Factor("chd", [DerivedLevel("iim", WithinTrial(bbrveh, [vrq, ouics])), DerivedLevel("lkyk", WithinTrial(bhsp, [vrq, ouics])),DerivedLevel("eqe", WithinTrial(rpb, [vrq, ouics]))])
### EXPERIMENT
design=[vrq,ouics,gypmm]
crossing=[gypmm]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END