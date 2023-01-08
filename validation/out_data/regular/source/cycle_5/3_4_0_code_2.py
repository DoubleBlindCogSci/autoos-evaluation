from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_rtrQ_iw_u = Factor(";rtrQ>iw>u", ["tDgc9xpc", "rvzmS[Jv|Vy", "PGknaVxdd8[5Uh"])
GCUYG&hEUH YrG = Factor("GCUYG&hEUH YrG", ["GQfW]zaOBZxt<", "%Czk5AB", "x6dYnGqey"])
cgWmLYt = Factor("cgWmLYt", [Level(">lBtL]RileJQ", 1), Level("TtfTZdjXV", 4), Level("JhdVsilJY6z_>{", 1)])
_EaNu_ZUnHvsm = Factor("7EaNu<ZUnHvsm", [Level("GJxFuqBNHktMYr", 1), Level("JK^D)wKGMvm%bV", 1), Level("8VWxl", 4), Level("TqwZp", 1)])


design=[_rtrQ_iw_u,cgWmLYt,_EaNu_ZUnHvsm]
crossing=[_rtrQ_iw_u,cgWmLYt,_EaNu_ZUnHvsm]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_4_0"))

### END
