from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vcDqYA = Factor("vcDqYA", [Level("t9NFiQW", 1), Level("4RXZQDRZfCv", 5), Level("nTAJgZf1j Oodu", 1), Level(" jxZVEIfnqjd", 1), Level("khFQQyN<%Cye", 2), Level("2naux", 1)])

design=[vcDqYA]
crossing=[vcDqYA]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/7_1_1"))

### END
