from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nmCqS_Q= Factor("nmCqS Q", [Level("bjLAX_e", 10), Level("<AxMNV", 1), Level("cLx!hbAF", 2), Level("Eify", 1), Level("hdJNxVjQu%YMx", 1), Level("NjGk", 1), Level("JjeVDq*T8sUxgb", 1), Level("IDHq", 5), Level("igjzQGT!!bqxO", 7)])
_MVb= Factor("!MVb", [Level("N[sLUNL", 6), Level("uliPi>L{vYZu<", 1), Level("D@KQ mM", 1), Level("KcXYF9nJW", 1), Level("4EfGTqk[] M", 1), Level("QjUXhkmxGl", 1), Level("JvHTCWUAS&{", 1), Level("Q aCECGmsOF0V", 10)])
LMIBd_RN= Factor("LMIBd{RN", [Level("Jbfn", 1), Level("uj3N]t<dcgr", 1), Level("Bd~Uhe(eHn", 1), Level("WZw:NZj", 1), Level("NyZQVF4JR|QWvw", 3), Level("Lhe^Xnx", 4), Level("JMeoz_WQO", 1), Level("7pbBGocj", 1)])

design=[nmCqS_Q,_MVb,LMIBd_RN]
crossing=[nmCqS_Q,_MVb,LMIBd_RN]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/8_3_0"))

### END
