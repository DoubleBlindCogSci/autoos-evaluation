from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
VlTtXKL4g=Factor('XhhZiGB',[Level('hPGl uOtisLND',6),'syCRDMI'])
D_haHS4wf=Factor("uXUzDyTLRmY",["&WZJORykj__bx<",'yvbPMPvTBO'])

### EXPERIMENT
design=[VlTtXKL4g,D_haHS4wf]
crossing=[VlTtXKL4g,D_haHS4wf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/2_2_0"))
### END