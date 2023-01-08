from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jqghz= Factor("jqghz", ["cladjy","haqvq","wersx","aqyi","bdds","jtzc","apqtow","axu"])

def is_kctzbv_yvvzxe(jqghz):
    return jqghz == "cladjy" or jqghz == "aqyi"
def is_kctzbv_ymvhv(jqghz):
    return jqghz == "haqvq" or jqghz == "apqtow"
def is_kctzbv_kci(jqghz):
    return jqghz == "wersx" or jqghz == "axu"
kctzbv= Factor("kctzbv", [DerivedLevel("yvvzxe", WithinTrial(is_kctzbv_yvvzxe, [jqghz])), DerivedLevel("ymvhv", WithinTrial(is_kctzbv_ymvhv, [jqghz])), DerivedLevel("kci", WithinTrial(is_kctzbv_kci, [jqghz]))])


design=[jqghz,kctzbv]
crossing=[kctzbv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END
