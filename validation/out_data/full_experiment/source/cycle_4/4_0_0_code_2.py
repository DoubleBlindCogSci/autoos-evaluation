from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
nzcbj = Factor("nzcbj", ["qxclap", "ggnefj"])
brdzmk = Factor("brdzmk", ["xhra", "uhllj"])
pvza = Factor("pvza", ["qxclap", "ggnefj"])
bglcc = Factor("bglcc", ["xhra", "uhllj"])
constraints = []
crossing = [nzcbj, brdzmk]

design=[nzcbj,brdzmk,pvza,bglcc]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_0_0"))
