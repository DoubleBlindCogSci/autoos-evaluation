from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jGhkG = Factor("jGhkG", [" GyKQz6AtL", "kHE^tK#PsSu", "b6Cxtj{", "dWZRHs SNQy5qt", "eMYNaS 9", ":UhRc", "yEhe]FrBMMhjn~", "NF?WtqD"])

design=[jGhkG]
crossing=[jGhkG]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_1_1"))

### END
