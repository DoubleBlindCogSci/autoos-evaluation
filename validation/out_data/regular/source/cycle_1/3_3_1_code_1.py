from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cZ96y2=Factor('hHhjIT#Skj)Vr',[Level("eL9{mhG8C{Zt",5),'WPzItkve@!rEe','zaKrmGLbEGmzR'])
oioDbqbFCmV=Factor('kxY!r8',[']&UFD3tuiyS','tGYmNS','zClDUXWfp'])
yHirkFY=Factor("t6vd;",["aPFyndMROE","TLzzbnYIIY",'DJXE&dfMaYT'])

### EXPERIMENT
design=[cZ96y2,oioDbqbFCmV,yHirkFY]
crossing=[cZ96y2,oioDbqbFCmV,yHirkFY]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/3_3_1"))
### END