from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
swxrom = Factor("swxrom", ["indmsy","yrf","cwqp","ziaw","vhjh","irj","mdfvvh","cirqwl"])
hfo = Factor("hfo", ["rmn","jusbu","fyc","qcqre","uukbjl","akcut"])
def is_ybt_asygc(swxrom, hfo):
    return swxrom[-1] == "cwqp" and hfo[0] != "uukbjl"
def is_ybt_cgb(swxrom, hfo):
    return swxrom[-1] != "cwqp" and hfo[0] == "uukbjl"
def is_ybt_chx(swxrom, hfo):
    return not (is_ybt_asygc(swxrom, hfo) or is_ybt_cgb(swxrom, hfo))
ybt = Factor("ybt", [DerivedLevel("asygc", Window(is_ybt_asygc, [swxrom, hfo], 2, 1)), DerivedLevel("cgb", Window(is_ybt_cgb, [swxrom, hfo], 2, 1)), DerivedLevel("chx", Window(is_ybt_chx, [swxrom, hfo], 2, 1))])

design=[swxrom,hfo,ybt]
crossing=[ybt]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END