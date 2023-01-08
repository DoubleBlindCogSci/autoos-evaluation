from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
iQjl3t=["IhYsmgLiYfpC",'57H7fsSJAd',"qlQfUqJ{G","iXbtgrA","dTyqjFcmcBE>L","C8VeWdMnu1dwni"]
J0IdyRQha=[iQjl3t[2],'LTv',"ScqNV_","PGEgKoJep","f:ngJai5?j^s",Level('R<f',3),"g#OlCG",'Zw6h']
B3zq7YHA9=Factor('>#J5D7CHMhfZqE',J0IdyRQha)

### EXPERIMENT
design=[B3zq7YHA9]
crossing=[B3zq7YHA9]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_1_1"))
### END