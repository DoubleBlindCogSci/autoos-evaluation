from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
q_qaFGyf=Factor('T$dsoWn',[Level('VUlOnKNLYpW^',5),';SsnEj'])
nGYX=Factor("eS?i",["OxKNQLt",Level("oZyMeSzICp",7)])

### EXPERIMENT
design=[q_qaFGyf,nGYX]
crossing=[q_qaFGyf,nGYX]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END