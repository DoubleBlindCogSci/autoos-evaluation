from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eB_zaL6=Factor('FRep',["kQEFiiw|6lz7",Level('fLMdM S',6)])
HbnveUld1ia=Factor('dqWvEw;1ke&f',['VcYd7Fh',"RPd9xPS"])
cJ1f8hbzJT1=['rrsZ',"MaocZJZr:KI"]
LsWqf0g7QN8=Factor('5HMqbAriUXtgR',cJ1f8hbzJT1)

### EXPERIMENT
design=[eB_zaL6,HbnveUld1ia,LsWqf0g7QN8]
crossing=[eB_zaL6,HbnveUld1ia,LsWqf0g7QN8]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3_0"))
### END