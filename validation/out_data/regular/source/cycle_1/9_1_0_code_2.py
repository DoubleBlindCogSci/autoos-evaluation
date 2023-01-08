from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
klWxvR= Factor("klWxvR", ["isc2IlmXIX", "JLcUIfY", "cDlenobc", Level(";Az", 9), "s^ryhRRE@v", "B~L@$", "f^Ty", Level("JcbwJCsZt", 1), "@bMmDp!x", "SScdTo5n#Edad"])

design=[klWxvR]
crossing=[klWxvR]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/9_1_0"))

### END
