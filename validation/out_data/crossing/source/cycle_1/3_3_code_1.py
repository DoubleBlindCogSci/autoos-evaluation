from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bvrc = Factor("bvrc", ["chb", "zfa"])
gnkk = Factor("gnkk", ["uwfmoy", "rczsyd"])
bgdoo = Factor("bgdoo", ["qfjwa", "gaa"])
attkxk = Factor("attkxk", ["yie", "ywta"])
wmn = Factor("wmn", ["gqurzb", "jfwvin"])
zidbk = Factor("zidbk", ["bvbden", "abrqx"])
nmdfv = Factor("nmdfv", ["zocjk", "rutxzw"])
cpms = Factor("cpms", ["btbxko", "qszaqm"])
sbfi = Factor("sbfi", ["gld", "tnj"])
fybrof = Factor("fybrof", ["cbmi", "kanviz"])

### EXPERIMENT
design=[bvrc,gnkk,bgdoo,attkxk,wmn,zidbk,nmdfv,cpms,sbfi,fybrof]
crossing=[[bvrc,gnkk],[bgdoo,attkxk,wmn,zidbk],[nmdfv,cpms,sbfi,fybrof],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_3"))
### END