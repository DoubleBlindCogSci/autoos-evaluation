from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
epjvsp = Factor("epjvsp", ["lub","ofc","cfuj","wkah","vlrfg","uzqq","kcbik"])
vfowp = Factor("vfowp", ["runks","rpaaj","gsat","ekm","gie","vty","jgzgd"])
def is_zdao_rcvuob(epjvsp, vfowp):
    return epjvsp == "vlrfg"
def is_zdao_ympx(epjvsp, vfowp):
    return epjvsp != "vlrfg" and vfowp == "gsat"
def is_zdao_vqro(epjvsp, vfowp):
    return not (is_zdao_rcvuob(epjvsp) or is_zdao_ympx(epjvsp, vfowp))
zdao= Factor("zdao", [DerivedLevel("rcvuob", WithinTrial(is_zdao_rcvuob, [epjvsp])), DerivedLevel("ympx", WithinTrial(is_zdao_ympx, [epjvsp, vfowp])), DerivedLevel("vqro", WithinTrial(is_zdao_vqro, [epjvsp, vfowp]))])

design=[epjvsp,vfowp,zdao]
crossing=[zdao]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_0"))

### END