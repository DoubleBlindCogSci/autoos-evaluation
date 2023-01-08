from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bat = Factor("bat", ["ujg","fhens","jaoxc","mqwe","tcpb","baynzb","digbte"])
def bshw(bat):
    return bat[0] != "ujg" and bat[-1] != "tcpb"
def bfteeq(bat):
    return bat[0] == "ujg" or bat[-1] == "tcpb"
jmpps = Factor("edbqn", [DerivedLevel("dzubff", Transition(bshw, [bat])), DerivedLevel("lixmae", Transition(bfteeq, [bat]))])
### EXPERIMENT
design=[bat,jmpps]
crossing=[jmpps]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END