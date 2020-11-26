import pandas as pd

def CorrMatrixAnalysis(df, dep_feature):
    '''brief:
            Displays in depth analysis of the correlation between features. Currently only addresses
            correlation of dependent feature to independent features, but will be updated soon.
        params (see default values for examples):
            df          - The dataframe to analyze.
            dep_feature - The dependent feature
        example call:
            df = pd.read_csv('Iris.csv')
            CorrMatrixAnalysis(df, 'species')'''
    dep_feature = str(dep_feature)
    corr = df.corr()
    dep, corrs = corr[dep_feature], []
    dep_t = dep.drop(dep_feature).abs().sort_values(ascending=False).dropna()
    corrs.append(['High', dep_t.loc[dep_t >= 0.7]])
    corrs.append(['Moderate', dep_t.loc[(dep_t >= 0.5) & (dep_t < 0.7)]])
    corrs.append(['Low', dep_t.loc[(dep_t >= 0.3) & (dep_t < 0.5)]])
    corrs.append(['No', dep_t.loc[dep_t < 0.3]])
    for corr_ in corrs:
        if corr_[1].size > 0:
            print("Features With " + corr_[0] + " Correlation to " + dep_feature + ":")
            [print("% .2f  -" % round(dep[x],2), x) for x in corr_[1].index]
            print('\n')