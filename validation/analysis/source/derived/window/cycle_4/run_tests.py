import os
from rouge_score import rouge_scorer
import pandas as pd

### random code was not compileable (exclude without mention):
EXCLUDES_CODE_1 = [(3,2,0),(2,1,0),(2,2,1),(3,2,1),(2,2,2),(3,2,2),(2,2,3),(3,2,3),(2,2,4),(3,2,4)]

NO_COMPILE = []
