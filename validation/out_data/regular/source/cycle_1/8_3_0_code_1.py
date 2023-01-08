from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
MiP0=Level("cLx!hbAF",2)
oY5RsBK=Factor("nmCqS Q",[Level('bjLAX_e',10),Level("<AxMNV",3),MiP0,Level('Eify',3),'hdJNxVjQu%YMx',"NjGk","JjeVDq*T8sUxgb",Level("IDHq",5),Level('igjzQGT!!bqxO',7)])
GNhd=Factor('!MVb',["N[sLUNL",Level('uliPi>L{vYZu<',6),"D@KQ mM",'KcXYF9nJW','4EfGTqk[] M',"QjUXhkmxGl",'JvHTCWUAS&{',Level("Q aCECGmsOF0V",10)])
jpq6=['Jbfn','uj3N]t<dcgr',"Bd~Uhe(eHn",'WZw:NZj',Level('NyZQVF4JR|QWvw',3),Level('Lhe^Xnx',4),'JMeoz_WQO','7pbBGocj']
fkYd0rgS5=Factor("LMIBd{RN",jpq6)

### EXPERIMENT
design=[oY5RsBK,GNhd,fkYd0rgS5]
crossing=[oY5RsBK,GNhd,fkYd0rgS5]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/8_3_0"))
### END