from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
TpSyH = Factor("TpSyH", [Level("qvv", 1), Level("~uZzSl", 1), Level("~UX>Akw NFk", 7), Level("ZXObQhL", 4), Level("PXCmymqM<", 1), Level("UpGGxXu% ", 10), Level("pDBXfz", 1), Level("VyYSVwPgFac x_", 1)])
hoVgtgpKmVWe = Factor("hoVgtgpKmVWe", [Level("Sv?Q", 1), Level("Y0lQ j#aT", 4), Level("z^jVnIZC6k", 7), Level("1i[c3IC", 1), Level("cJnhg@jVoPlAO9", 9), Level("6eyaLcBL:vy@d|", 1), Level("Hzd@WSISDdt2x", 1), Level("@wjzxGHMxkh5", 1), Level("iByNS", 1)])
t_hSsEQ_nDHGxg = Factor("t$hSsEQ]nDHGxg", [Level("Rsxk", 3), Level("cdaQVimM", 7), Level("GvMk", 9), Level(";sF0", 1), Level("gvTmz_C0ByQAK", 1), Level("Zi;2rF@R", 1), Level("g]nkKj", 1), Level("o;rGrZT8d", 1)])

design=[TpSyH,hoVgtgpKmVWe,t_hSsEQ_nDHGxg]
crossing=[TpSyH,hoVgtgpKmVWe,t_hSsEQ_nDHGxg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_3_0"))

### END
