from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lnc= Factor("lnc", ["wdzc","grzhyq","cfsi","kxy","wabm","mhh"])
ziyuus= Factor("ziyuus", ["wdzc","grzhyq","cfsi","kxy","wabm","mhh"])
fpj= Factor("fpj", ["wdzc","grzhyq","cfsi","kxy","wabm","mhh"])
def is_dsny_hxibgp(lnc, ziyuus):
    return lnc[0] != ziyuus[-1]
def is_dsny_cbvbbo(lnc, ziyuus):
    return not is_dsny_hxibgp(lnc, ziyuus)
dsny= Factor("dsny", [DerivedLevel("hxibgp", Window(is_dsny_hxibgp, [lnc, ziyuus], 2, 1)), DerivedLevel("cbvbbo", Window(is_dsny_cbvbbo, [lnc, ziyuus], 2, 1))])

design=[lnc,ziyuus,fpj,dsny]
crossing=[dsny]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END
