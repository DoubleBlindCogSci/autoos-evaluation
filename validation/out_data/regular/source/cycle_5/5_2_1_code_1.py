from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZC0qJ4Gjnt0=Factor('CL2s0kKLvg',['TFyBEilVx','afh D_<XaMM3]',"cFOHPxTuk",'Muil{O@^)SBZho',"iWWjWwCl"])
Jphsa8FV='hqFU1'
jakt7Oz2Eb=['cil4Xt','C! Yysz2wAXcq_',"zo7V4Qh",Level('IWDkJ',2),Jphsa8FV,Level("Gmor:2KO&Isd",1)]
OO_M7TdW=Factor("hACykAtr",jakt7Oz2Eb)

### EXPERIMENT
design=[ZC0qJ4Gjnt0,OO_M7TdW]
crossing=[ZC0qJ4Gjnt0,OO_M7TdW]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_1"))
### END