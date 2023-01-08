from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
onfbo = Factor("onfbo", ["nbqy","hluxjt","bgvex","kmcxj","oij","foyoxc","dyc"])
nbq = Factor("nbq", ["nbqy","hluxjt","bgvex","kmcxj","oij","foyoxc","dyc"])
rim = Factor("rim", ["nbqy","hluxjt","bgvex","kmcxj","oij","foyoxc","dyc"])
def is_zfdgl_chq(onfbo, nbq, rim):
    return onfbo[-3] == nbq[-2] and onfbo[-2] != rim[-3]
def is_zfdgl_zfnpyb(onfbo, nbq, rim):
    return onfbo[-3] != nbq[-2] and onfbo[-2] == rim[-3]
def is_zfdgl_foaw(onfbo, nbq, rim):
    return not (is_zfdgl_chq(onfbo, nbq, rim) or is_zfdgl_zfnpyb(onfbo, nbq, rim))
zfdgl = Factor("zfdgl", [DerivedLevel("chq", Window(is_zfdgl_chq, [onfbo, nbq, rim], 4, 1)), DerivedLevel("zfnpyb", Window(is_zfdgl_zfnpyb, [onfbo, nbq, rim], 4, 1)), DerivedLevel("foaw", Window(is_zfdgl_foaw, [onfbo, nbq, rim], 4, 1))])

design=[onfbo,nbq,rim,zfdgl]
crossing=[zfdgl]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_4"))

### END