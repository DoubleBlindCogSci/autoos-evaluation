from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xwQGDVF = Factor("xwQGDVF", [Level("Uko", 1), Level("gO4iSNuT", 1), Level("lRxrEeOEoIY", 1), Level("&dVwiX", 1), Level("mpM", 4), Level("7lsu7Dsxp7ZsB", 9), Level("NVwN", 9), Level("8lqI;VSlnF!yK", 4)])
iRabLm_ssv = Factor("iRabLm7ssv", [Level("yLC6wmxzi", 4), Level("pCw", 1), Level("oVH3Mg|JwHrf", 1), Level("klZF:YoOMK", 3), Level("JDMNj", 1), Level("yQbe!q}OuE;", 8), Level("O:stSVaCELg", 2), Level("drzYtM", 1), Level("uzY&NM Ts", 1), Level("WZcPjpRX7ZB", 7)])
ER_vn__FM = Factor("ER vn99FM", [Level("SOOR", 1), Level("hfDb8oO", 1), Level("zxiBZ", 10), Level("cJqEzja", 1), Level("EQPbrTar%", 1), Level("fBizdUpK", 1), Level("BuqtjEHrfD", 9), Level("pKH", 1)])

design=[xwQGDVF,iRabLm_ssv,ER_vn__FM]
crossing=[xwQGDVF,iRabLm_ssv,ER_vn__FM]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_3_1"))

### END
