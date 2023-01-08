from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
gxfkc = Factor("gxfkc", ["kdxc","cubreg","qrbznd","obpkru","jpm","wfe"])
yykhta = Factor("yykhta", ["ysx","irom","lytf","gmdh","vedwwq","ycnsmr"])
def coff(gxfkc, yykhta):
     return gxfkc[-1] == "wfe" and yykhta[0] != "irom"
def bbjwd(gxfkc, yykhta):
     return "wfe" != gxfkc[-1] and yykhta[0] == "irom"
def bign(gxfkc, yykhta):
     return (not coff(gxfkc, yykhta)) and (not bbjwd(gxfkc, yykhta))
vldaa = DerivedLevel("mqqe", Transition(coff, [gxfkc, yykhta]))
epgo = DerivedLevel("van", Transition(bbjwd, [gxfkc, yykhta]))
ilt = DerivedLevel("xqtdl", Transition(bign, [gxfkc, yykhta]))
ccrsop = Factor("nbvzt", [vldaa, epgo, ilt])

### EXPERIMENT
design=[gxfkc,yykhta,ccrsop]
crossing=[ccrsop]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END