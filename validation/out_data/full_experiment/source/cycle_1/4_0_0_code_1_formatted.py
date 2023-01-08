### REGULAR FACTORS
hjben = Factor("hjben", ["nsfpc", "hln"])
skt = Factor("skt", ["kmx", "ddoug"])
urcbh = Factor("urcbh", ["nsfpc", "hln"])
ljh = Factor("ljh", ["kmx", "ddoug"])
### EXPERIMENT
design=[hjben,skt,urcbh,ljh]
constraints=[]
crossing=[ljh,skt]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
