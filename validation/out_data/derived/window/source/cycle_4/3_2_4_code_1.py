from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
onfbo = Factor("onfbo", ["nbqy","hluxjt","bgvex","kmcxj","oij","foyoxc","dyc"])
nbq = Factor("nbq", ["nbqy","hluxjt","bgvex","kmcxj","oij","foyoxc","dyc"])
rim = Factor("rim", ["nbqy","hluxjt","bgvex","kmcxj","oij","foyoxc","dyc"])
def suofw(onfbo, nbq, rim):
     return onfbo[-3] == nbq[-2] and onfbo[-2] != rim[-3]
def xfcew(onfbo, nbq, rim):
     return nbq[-2] != onfbo[-3] and onfbo[-2] == rim[-3]
def fgvx(onfbo, nbq, rim):
     return (not suofw(onfbo, nbq, rim)) and (not xfcew(onfbo, nbq, rim))
zdw = Factor("zfdgl", [DerivedLevel("chq", Window(suofw, [onfbo, nbq, rim],4,1)), DerivedLevel("zfnpyb", Window(xfcew, [onfbo, nbq, rim],4,1)),DerivedLevel("foaw", Window(fgvx, [onfbo, nbq, rim],4,1))])
### EXPERIMENT
design=[onfbo,nbq,rim,zdw]
crossing=[zdw]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END