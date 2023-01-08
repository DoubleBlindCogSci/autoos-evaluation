from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bat= Factor("bat", ["ujg","fhens","jaoxc","mqwe","tcpb","baynzb","digbte"])
def is_edbqn_dzubff(bat):
    return bat[-1] != "ujg" and bat[0] != "tcpb"
def is_edbqn_lixmae(bat):
    return not is_edbqn_dzubff(bat)
edbqn= Factor("edbqn", [DerivedLevel("dzubff", Transition(is_edbqn_dzubff, [bat])), DerivedLevel("lixmae", Transition(is_edbqn_lixmae, [bat]))])

design=[bat,edbqn]
crossing=[edbqn]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END
