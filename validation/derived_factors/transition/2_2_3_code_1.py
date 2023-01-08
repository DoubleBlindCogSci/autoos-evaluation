from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hbrcki = Factor("hbrcki", ["mwkocn","oivj","xmbdsc","wdoqku","jmvfq"])
hbasyw = Factor("hbasyw", ["mwkocn","oivj","xmbdsc","wdoqku","jmvfq"])
dfp = Factor("dfp", ["mwkocn","oivj","xmbdsc","wdoqku","jmvfq"])
def wtzm(hbrcki, dfp, hbasyw):
    return hbrcki[0] != dfp[-1] and hbrcki[-1] != hbasyw[0]
def yye(hbrcki, dfp, hbasyw):
    return not wtzm(hbrcki, dfp, hbasyw)
opb = Factor("lccd", [DerivedLevel("ssyqzm", Transition(wtzm, [hbrcki, hbasyw, dfp])), DerivedLevel("hxmnd", Transition(yye, [hbrcki, hbasyw, dfp]))])
### EXPERIMENT
design=[hbrcki,hbasyw,dfp,opb]
crossing=[opb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END