from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
khj = Factor("khj", ["sbdypg","ffis","xxdzsu","kld","jdnxcs","dkifp","nomvgm"])
cswp = Factor("cswp", ["lykrd","ydd","rwpe","yjq","bwb","ufplv","ipxply","dni"])
def hysud(khj, cswp):
     return "dkifp" == khj
def sfu(khj, cswp):
     return khj != "dkifp" and  cswp == "lykrd"
def pcro(khj, cswp):
     return (khj != "dkifp") and (not cswp == "lykrd")
mkzleo = Factor("ini", [DerivedLevel("vsbs", WithinTrial(hysud, [khj, cswp])), DerivedLevel("tvonnc", WithinTrial(sfu, [khj, cswp])),DerivedLevel("pguwt", WithinTrial(pcro, [khj, cswp]))])
### EXPERIMENT
design=[khj,cswp,mkzleo]
crossing=[mkzleo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END