from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tyi= Factor("tyi", ["oiz","gqm","tdh","jjlisq","etae"])
def is_qjd_ydytym(tyi):
    return tyi[0] == "gqm" or tyi[-3] != "tdh"
def is_qjd_sehsfj(tyi):
    return not is_qjd_ydytym(tyi)
qjd= Factor("qjd", [DerivedLevel("ydytym", Window(is_qjd_ydytym, [tyi], 4, 1)), DerivedLevel("sehsfj", Window(is_qjd_sehsfj, [tyi], 4, 1))])

design=[tyi,qjd]
crossing=[qjd]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END
