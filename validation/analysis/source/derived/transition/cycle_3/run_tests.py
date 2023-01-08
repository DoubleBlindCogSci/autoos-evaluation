import os
from rouge_score import rouge_scorer
import pandas as pd

EXCLUDES = [(2, 1, 2), (3, 2, 2)]

NO_COMPILE = []
