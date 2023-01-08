from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
IFianaRLFw= Factor("IFianaRLFw", ["3lIxCbWtjU@aeK", "}G8%!p", "eYHU", "EXHIiw(myce", "ig8rwTRloZn", Level("dBGyaZKn 1I]vG", 4), "t(E8iu"])
PGxfqfvHjV_= Factor("PGxfqfvHjV{", ["DUz ucY1na", "fnJFR", "]RMPX9sY{vQDm", "sS@Y", "qDVMv", "Kv9Z9kW", "CIYBliC", Level("Mw@|qRC~z", 8)])

design=[IFianaRLFw,PGxfqfvHjV_]
crossing=[IFianaRLFw,PGxfqfvHjV_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/7_2_0"))

### END
