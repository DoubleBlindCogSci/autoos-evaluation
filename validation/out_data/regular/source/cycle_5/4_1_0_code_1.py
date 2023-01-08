from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lQH3Wtzxv5V=Factor('[sXyFTqTfX',["A&DJHpbpIV6C",' Dy','L<0fbyXbsHS',Level('%XXtRH!Y',4)])

### EXPERIMENT
design=[lQH3Wtzxv5V]
crossing=[lQH3Wtzxv5V]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_0"))
### END