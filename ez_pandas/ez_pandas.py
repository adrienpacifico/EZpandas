import pandas as pd
import pandas_flavor as pf

@pf.register_series_method
def ez_value_counts(s,dropna=False, ascending=False, bins=None):
    """A fancier value_counts"""
    df_ = pd.concat([
        s.value_counts(dropna=dropna, normalize=False, ascending=ascending, bins=bins),
        s.value_counts(dropna=dropna, normalize=True, ascending=ascending, bins=bins),
        s.value_counts(dropna=dropna, normalize=True, ascending=ascending, bins=bins).cumsum()],
        axis=1,
        keys=["N_obs","share","cum_share"])
    
    if bins:
        return df_.assign(bins=lambda x: x.index).assign(quantile= lambda x : np.array(range(len(x)))+1).set_index("quantile")
    return df_
