from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
luANK7R=['mlAZbtzOD','nKr*#Y','B&~T9GDSZ',"B0xjrSIfn",'1AAewslQoHsdI','sxxrZ1aFrEGi']
RfXR=Factor('jic',luANK7R)
wjt3jxV=['ENJX~vDmHu',"uz~wzT a","rwi%jIzEJ"]
jsRv6fSbe=Factor('vtg:aXID',[wjt3jxV[0],"VyoHmOmf","QmEkjZRr z^dE",'DpKtQyJNUiyDIY',"OoV7f~l<",'DIFSplJ9ptR',"AcebDObN"])
JHuq9vtmZTG=['mwlk','fExcH','rxtl',"LItp&Zb7R",Level("tSLOOQGs5 ",4),"^sHgd"]
o2hL8qRVB=Factor('a&fUekLOWtD',[JHuq9vtmZTG[4],'KoZ',"#dM1Eo7EPc","elgmRMLGeY!kw@",' owJn',Level("osHHgtGdGLbG",1),Level('JLMygcjPqDTz',2)])

### EXPERIMENT
design=[RfXR,jsRv6fSbe,o2hL8qRVB]
crossing=[RfXR,jsRv6fSbe,o2hL8qRVB]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_3_1"))
### END