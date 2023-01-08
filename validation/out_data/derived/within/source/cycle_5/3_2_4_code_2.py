from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
khj = Factor("khj", ["sbdypg","ffis","xxdzsu","kld","jdnxcs","dkifp","nomvgm"])
cswp = Factor("cswp", ["lykrd","ydd","rwpe","yjq","bwb","ufplv","ipxply","dni"])
def is_ini_vsbs(khj, cswp):
    return khj == "dkifp"
def is_ini_tvonnc(khj, cswp):
    return khj != "dkifp" and cswp == "lykrd"
def is_ini_pguwt(khj, cswp):
    return not (is_ini_vsbs(khj) or is_ini_tvonnc(khj, cswp))
ini = Factor("ini", [DerivedLevel("vsbs", WithinTrial(is_ini_vsbs, [khj])), DerivedLevel("tvonnc", WithinTrial(is_ini_tvonnc, [khj, cswp])), DerivedLevel("pguwt", WithinTrial(is_ini_pguwt, [khj, cswp]))])

design=[khj,cswp,ini]
crossing=[ini]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END