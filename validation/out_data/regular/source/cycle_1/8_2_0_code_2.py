from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
a_YxQGIoReR= Factor("a1YxQGIoReR", [Level("kvW", 7), Level("zYyMn5xpaCfo", 1), Level("OZTmyGNq", 1), Level("OTWjDg?Vqfm", 1), Level("*DzOIF:Hcp", 1), Level("ZMhHl:CEAooQ", 1), Level("g:Vj#", 8), Level("t^G@Ab[oMmpg4N", 1)])
ooFs_z_qRGGH= Factor("ooFs2z[qRGGH", [Level("LjtFANUgqC2", 1), Level("QSVsHULW", 5), Level("UrVX", 1), Level(" g:6q", 1), Level("ml|U[Vj9O", 1), Level("gOcJjayZD) ", 1), Level("OpmTm", 1), Level("cfmcydLcF*jK", 1)])

design=[a_YxQGIoReR,ooFs_z_qRGGH]
crossing=[a_YxQGIoReR,ooFs_z_qRGGH]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/8_2_0"))

### END
