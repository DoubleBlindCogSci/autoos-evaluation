from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
NjgQFJ = Factor("NjgQFJ", [Level("srKtJYiwZr", 3), Level("JO>ZDvyCgvMJB", 1), Level("cXsT$KKwLdBq", 1), Level("KqrbIo8eEo", 1)])
OFbEmU = Factor("OFbEmU", ["wjZfj", "lsH", "gqeazvclevrST", "FnH"])
___Q__IGtfRfZ = Factor("?82Q^&IGtfRfZ", [Level("uIaKxy;ptAK", 1), Level("DycIbXUYN", 1), Level("SVi", 3), Level("Cjc|{Dua z", 1), Level("PIQ9JkUoOyII", 1)])

design=[NjgQFJ,OFbEmU,___Q__IGtfRfZ]
crossing=[NjgQFJ,OFbEmU,___Q__IGtfRfZ]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3_0"))

### END
