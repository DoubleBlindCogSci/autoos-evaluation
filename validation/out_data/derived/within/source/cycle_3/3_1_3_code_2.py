from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cnz = Factor("cnz", ["hbnnk","ftewb","lsdb","ysdk","hnod","gunqsj"])
def is_zcvwuy_zxh(cnz):
    return cnz == "gunqsj"
def is_zcvwuy_pio(cnz):
    return cnz == "ysdk"
def is_zcvwuy_wqzdn(cnz):
    return not (is_zcvwuy_zxh(cnz) or is_zcvwuy_pio(cnz))
zcvwuy= Factor("zcvwuy", [DerivedLevel("zxh", WithinTrial(is_zcvwuy_zxh, [cnz])), DerivedLevel("pio", WithinTrial(is_zcvwuy_pio, [cnz])), DerivedLevel("wqzdn", WithinTrial(is_zcvwuy_wqzdn, [cnz]))])

design=[cnz,zcvwuy]
crossing=[zcvwuy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END
