from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cnz = Factor("cnz", ["hbnnk","ftewb","lsdb","ysdk","hnod","gunqsj"])
def qzasuk(cnz):
     return cnz == "gunqsj"
def fwhu(cnz):
     return cnz == "ysdk"
def vtbbra(cnz):
     return (not qzasuk(cnz)) and (not fwhu(cnz))
ekic = Factor("zcvwuy", [DerivedLevel("zxh", WithinTrial(qzasuk, [cnz])), DerivedLevel("pio", WithinTrial(fwhu, [cnz])),DerivedLevel("wqzdn", WithinTrial(vtbbra, [cnz]))])
### EXPERIMENT
design=[cnz,ekic]
crossing=[ekic]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END