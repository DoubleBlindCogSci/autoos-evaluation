from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
VXgn = Factor("VXgn", [Level("pFuROZI", 10), Level("AL:Rm", 1), Level("H%ezN>9cIA8Z", 1), Level("C4dy", 5), Level("KAEiGsZv!gDEqx", 1), Level("KRsuNgOkEA", 8), Level("h<XqmUzks ko", 1), Level("qD7", 9), Level("gZSo", 1), Level("AIJTUuUnYi#7q", 10)])
gzlpiy = Factor("gzlpiy", [Level("sNRD^CUTY", 2), Level("PyDkyB5H(x@", 1), Level("AlW", 1), Level("p tewt", 1), Level("AS@MZGGvJDCgs", 1), Level("pw!", 1), Level("F#igtIMhgbzrwi", 1), Level("gjn:S", 9), Level("vb_EeQVca]j", 1)])

design=[VXgn,gzlpiy]
crossing=[VXgn,gzlpiy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_2_0"))

### END
