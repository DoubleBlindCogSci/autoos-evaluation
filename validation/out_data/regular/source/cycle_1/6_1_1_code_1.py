from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eTZe=Factor("nY6kjAPaEC",['L8z','3$ms',Level("GErthOVs",4),"ZcOO{RhA;oIpcx","sZcZqO<Pv ","hBWKh"])

### EXPERIMENT
design=[eTZe]
crossing=[eTZe]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/6_1_1"))
### END