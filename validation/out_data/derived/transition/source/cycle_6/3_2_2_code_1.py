from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vyl = Factor("vyl", ["nfji","ewcnwl","zhrtv","gevbzq","mutl","omuphx"])
lytpda = Factor("lytpda", ["hmeuy","uqjxcp","bgh","kiwcz","rzqhjz","ewmcgk","hxdqz","ygzcc"])
def jjond(vyl, lytpda):
     return "omuphx" == vyl[-1] and lytpda[0] != "uqjxcp"
def kwefzx(vyl, lytpda):
     return "omuphx" != vyl[-1] and lytpda[0] == "uqjxcp"
def emotn(vyl, lytpda):
     return (vyl[-1] != "omuphx") and (lytpda[0] != "uqjxcp")
nrc = DerivedLevel("zigcr", Transition(jjond, [vyl, lytpda]))
ffkul = DerivedLevel("ltkzxi", Transition(kwefzx, [vyl, lytpda]))
vombk = DerivedLevel("xinlkr", Transition(emotn, [vyl, lytpda]))
togld = Factor("jljwku", [nrc, ffkul, vombk])

### EXPERIMENT
design=[vyl,lytpda,togld]
crossing=[togld]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END