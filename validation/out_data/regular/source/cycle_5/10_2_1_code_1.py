from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
KEZbuPu=Factor('OGhyxfKA',['CyJRwFTVSTXbZ',"5>OvauYdNTy",'GIAsZeoe)UW_',"uUkEpboE",Level('GpIF oIPiLs',3),'xEhxor_hDDM1xm',"3Ym",'@rcBr',"P{ DbDpbFxUHeX","qPGg_suDXp)Dy!"])
u2fIvWG91c='XwKBLaBs'
Ut6DzC6z='bJYzMGO'
kufr2o=["WGdrC4R","~HiSlNh",'uZoH',":POtdtAsg>J",Ut6DzC6z,"O390dJsFo",'A4co9Eba(wS:{',"jmG",'lcD','kCMfMrs',u2fIvWG91c,'Xp0)iqc']
JBEi_feiwg=Factor('EEoQq',kufr2o)

### EXPERIMENT
design=[KEZbuPu,JBEi_feiwg]
crossing=[KEZbuPu,JBEi_feiwg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/10_2_1"))
### END