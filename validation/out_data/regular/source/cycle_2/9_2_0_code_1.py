from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
NuKCQfoe=Level("KRsuNgOkEA",8)
bkTn_ivYsWl=Factor('VXgn',[Level("pFuROZI",10),'AL:Rm',Level('H%ezN>9cIA8Z',10),Level("C4dy",5),"KAEiGsZv!gDEqx",NuKCQfoe,'h<XqmUzks ko',Level("qD7",9),"gZSo",Level('AIJTUuUnYi#7q',10)])
Yeap7=Factor("gzlpiy",[Level('sNRD^CUTY',2),'PyDkyB5H(x@',Level('AlW',2),"p tewt",'AS@MZGGvJDCgs','pw!',Level('F#igtIMhgbzrwi',1),Level("gjn:S",9),"vb_EeQVca]j"])

### EXPERIMENT
design=[bkTn_ivYsWl,Yeap7]
crossing=[bkTn_ivYsWl,Yeap7]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_2_0"))
### END