from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
leyw= Factor("leyw", ["dnxv","vzpmsy","zwxz","wtv","ejuqc","dgd"])
luzdp= Factor("luzdp", ["dnxv","vzpmsy","zwxz","wtv","ejuqc","dgd"])
bqup= Factor("bqup", ["dnxv","vzpmsy","zwxz","wtv","ejuqc","dgd"])
def is_xlqpo_abfhmd(leyw, luzdp, bqup):
    return leyw[-2] == bqup[-1]
def is_xlqpo_xfaret(leyw, luzdp, bqup):
    return not is_xlqpo_abfhmd(leyw, luzdp, bqup)
xlqpo= Factor("xlqpo", [DerivedLevel("abfhmd", Window(is_xlqpo_abfhmd, [leyw, luzdp, bqup], 3, 1)), DerivedLevel("xfaret", Window(is_xlqpo_xfaret, [leyw, luzdp, bqup], 3, 1))])

design=[leyw,luzdp,bqup, xlqpo]
crossing=[xlqpo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END
