from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ngavjj= Factor("ngavjj", ["ips","ych","kwmfoj","fedhn","oflobf","nym","owwhzk","mscp"])
umnwpc= Factor("umnwpc", ["ips","ych","kwmfoj","fedhn","oflobf","nym","owwhzk","mscp"])
kibvon= Factor("kibvon", ["ips","ych","kwmfoj","fedhn","oflobf","nym","owwhzk","mscp"])

def is_egudg_hysx(ngavjj, umnwpc, kibvon):
    return kibvon == ngavjj
def is_egudg_gmaul(ngavjj, umnwpc, kibvon):
    return kibvon != ngavjj and ngavjj == umnwpc
def is_egudg_vipame(ngavjj, umnwpc, kibvon):
    return not (is_egudg_hysx(ngavjj, umnwpc, kibvon) or is_egudg_gmaul(ngavjj, umnwpc, kibvon))
egudg= Factor("egudg", [DerivedLevel("hysx", WithinTrial(is_egudg_hysx, [ngavjj, umnwpc, kibvon])), DerivedLevel("gmaul", WithinTrial(is_egudg_gmaul, [ngavjj, umnwpc, kibvon])), DerivedLevel("vipame", WithinTrial(is_egudg_vipame, [ngavjj, umnwpc, kibvon]))])


design=[ngavjj,umnwpc,kibvon,egudg]
crossing=[egudg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END
