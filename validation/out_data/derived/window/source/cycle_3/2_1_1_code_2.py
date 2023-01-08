from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ttak = Factor("ttak", ["klvnuk","deca","xeqi","oegdzv","ntqt"])
def is_hrl_pavhzi(ttak):
    return ttak[0] != "klvnuk" and ttak[-1] == "xeqi"
def is_hrl_typxqe(ttak):
    return not is_hrl_pavhzi(ttak)
hrl= Factor("hrl", [DerivedLevel("pavhzi", Window(is_hrl_pavhzi, [ttak], 2, 1)), DerivedLevel("typxqe", Window(is_hrl_typxqe, [ttak], 2, 1))])

design=[ttak,hrl]
crossing=[hrl]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END
