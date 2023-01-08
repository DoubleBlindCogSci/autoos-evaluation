from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ngQyMaDsYFu=Factor('vcDqYA',['t9NFiQW',Level("4RXZQDRZfCv",5),Level('nTAJgZf1j Oodu',5),' jxZVEIfnqjd',Level("khFQQyN<%Cye",2),"bVKY","2naux"])

### EXPERIMENT
design=[ngQyMaDsYFu]
crossing=[ngQyMaDsYFu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_1_1"))
### END