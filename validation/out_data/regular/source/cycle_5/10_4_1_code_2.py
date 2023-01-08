from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
GuZ = Factor("GuZ", ["VVw]bS uS", "aYXjW", "K?7Hma", "p$XMTXmMCuqR", "h^W1wMwgTR", "cIqL&DVvgivi", "nObBwMQPshbddM", "CcQFxAzvaHwge2", "nJDK", "NBWAeK5mJEQxk", "x[smAoI"])
MMmje = Factor("MMmje", ["hnHaZhI", "~fG gQtCtP", "ag[avld", "D;)kN8", "Umm", "VYLknJ7{", "FcBv", "XdlXgRrQ", "C]jf", "DzThKA"])
b_W_S_bFAH_ZE = Factor("b%W2S#bFAH[ZE", ["sEPbM{~eFkN", "SFm]YB", "uXbDVOyYs", "nBWKZyw", "KRoX(hUdt", "qdcjMxdsXMaMi", "EiTSrlo", "VOQf_", "lVmOr%", "R%QIDbOo}zijyF"])

design=[GuZ,MMmje,b_W_S_bFAH_ZE]
crossing=[GuZ,MMmje,b_W_S_bFAH_ZE]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/10_4_1"))

### END
