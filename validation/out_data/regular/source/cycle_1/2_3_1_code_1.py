from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uOeRUFDjih=Factor("BNpEwv@T",["LLeVDr","XN9DUj^IEz"])
vvmEE6nWQ=Factor("PSCUREaDySmUP",['q6GqtQ8ONseYUv',Level("eeFDH4#jlgJy",3)])
SYyC0j=[Level("I)GeF",2),"kmx"]
x8dWLa3U4=Factor('jcx',SYyC0j)

### EXPERIMENT
design=[uOeRUFDjih,vvmEE6nWQ,x8dWLa3U4]
crossing=[uOeRUFDjih,vvmEE6nWQ,x8dWLa3U4]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/2_3_1"))
### END