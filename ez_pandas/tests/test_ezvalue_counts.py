""" test value_counts """
import numpy as np
import pytest

import pandas as pd
import pandas._testing as tm

from ez_pandas import ez_value_counts

df = pd.DataFrame({"fake_col":sum([[i]*i for i in range(5)], [])+[np.nan]})

class TestEZValue_counts:
    def test_simple(self):
        print(df.fake_col.value_counts())
        


