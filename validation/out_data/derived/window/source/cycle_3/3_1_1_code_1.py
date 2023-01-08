from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
med = Factor("med", ["zjbe","enhw","zzeiq","ngeen","tyu","blz","khy","fbcolf"])
def owukbh(med):
     return med[-2] == "fbcolf" and not med[-1] == "fbcolf"
def rckxpt(med):
     return med[-2] != "fbcolf" and  med[-1] == "enhw"
def wnbb(med):
     return (med[-2] != "fbcolf") and (not rckxpt(med))
gfvg = Factor("bxt", [DerivedLevel("hurev", Window(owukbh, [med],3,1)), DerivedLevel("axe", Window(rckxpt, [med],3,1)),DerivedLevel("tuaxow", Window(wnbb, [med],3,1))])
### EXPERIMENT
design=[med,gfvg]
crossing=[gfvg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END