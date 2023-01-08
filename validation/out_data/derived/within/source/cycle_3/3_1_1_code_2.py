from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
guh = Factor("guh", ["icgxd","rio","nfnij","spbm","jtmifq","bzfnd"])
def is_jobcfs_rdl(guh):
    return guh == "rio"
def is_jobcfs_grs(guh):
    return guh == "nfnij"
def is_jobcfs_vujbce(guh):
    return not (is_jobcfs_rdl(guh) or is_jobcfs_grs(guh))
jobcfs= Factor("jobcfs", [DerivedLevel("rdl", WithinTrial(is_jobcfs_rdl, [guh])), DerivedLevel("grs", WithinTrial(is_jobcfs_grs, [guh])), DerivedLevel("vujbce", WithinTrial(is_jobcfs_vujbce, [guh]))])

design=[guh,jobcfs]
crossing=[jobcfs]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END
