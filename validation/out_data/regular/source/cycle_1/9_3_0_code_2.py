from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_HAzv= Factor("_HAzv", ["gr&GSlM", "9xdOnDHGXf", "UNOTTFk)AFMq0", "U1*mng J", "BZysJvDInew", "FSHhEAThvq4", "{{BS", "FtPqFz", "AdpSV|TDjYLoN"])
RabtMGmqX= Factor("RabtMGmqX", [Level("ZgGspLf nfkGor", 9), Level("uWf;kYbym#JIk", 4), Level("kMHQP", 3), Level("{u3K EaIG", 3), "*FChWzjw", "L}d", "QhJJMKxIbjFcEk", "CGC", "Mvd"])
LFsvlDVeGo_= Factor("LFsvlDVeGo$", [Level("EZWxy>hD6h", 3), Level("G7~sZf VBE$r", 5), "DSVIcFpZBQZ", "utGw", "uzZQFDKw]WIe", "OxkwKnHt?", "rW>S&p", "Y1TaFMKq tRA", "bDJVif"])

design=[_HAzv,RabtMGmqX,LFsvlDVeGo_]
crossing=[_HAzv,RabtMGmqX,LFsvlDVeGo_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/9_3_0"))

### END
