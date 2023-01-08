from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
_qDN_ = Factor("!qDN3", [Level("Q6LqyfUp", 4), Level("SngMlW", 3), Level("4gdOh", 2), "XuFE", "QFwd:Z", "VMJiMBbJIAJG", "gHZt(KrcldOm ", "Gd[H)cXWZV", "H)DaSf", "UM_jFL"])
FL_p = Factor("FL0p", [Level("Jgfo;KxshSxI", 2), Level("TY?L", 1), Level("AlKm>BrgqA", 2), "aJAa:mCAghLnBK", "dvioV#QkuM", "ej)OFcG", ">:9", "n2p!tFmY", "AUMdbMtmV", "s|QiEfF#i"])
EhRYA__iR = Factor("EhRYA!$iR", [Level("nwYY}VI", 1), "{?$rH6SD5T", "q81aEhA", "manacASWYHb", "lNMWaaiKUtZOf", "xNT|W&W", "MZlyiN", "QLrZP", "CwSopuVm;yn}O", "pxfy^LcNmTxKE"])

design=[_qDN_,FL_p,EhRYA__iR]
crossing=[_qDN_,FL_p,EhRYA__iR]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_3_0"))

### END
