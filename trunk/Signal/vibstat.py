# -*- coding:utf-8 -*-
'''
Created on 2011-12-13

@author: WLQ
'''
import numpy as np
def moving(m,data,step,points,*args,**kwargs):
    'apply a function to a sequence, with a specialfied interval.'
    data=data.flatten()
    if len(data)<=points:
        return {0:m(data,*args,**kwargs)}
    else:
        index=range(0,len(data)-points+1,step)
        res={}
        for ind in index:
            res[ind]=m(data[ind:ind+points],*args,**kwargs)
        return res
    
def postdict(d):
    'proceed the moving output dict, the key is sorted.'
    keys=d.keys()
    keys.sort()
    for key in keys:
        yield d[key]
    
def fastmoving(m,data,step,points,*args,**kwargs):
    '''apply a function to a sequence, with a specialfied interval.
the output is the same size, the result is store in a ndarray.'''
    data=data.flatten()
    if len(data)<=points:
        tmp=m(data,*args,**kwargs)
        res=np.zeros(tmp.shape+(1,))
        res[...,0]=tmp       
        return res
    else:
        index=range(0,len(data)-points+1,step)
        tmp=m(data[index[0]:index[0]+points],*args,**kwargs)
        res=np.zeros(tmp.shape+(len(index),))
        lastaxis=0
        res[...,lastaxis]=tmp
        for ind in index[1:]:
            lastaxis+=1
            res[...,lastaxis]=m(data[ind:ind+points],*args,**kwargs)
        return res
 
def rms(v):
    'caculate the RMS of a vector'
    return np.sqrt(np.dot(v,v)/len(v))

def peak(v):
    'caculate the peak of a vector'
    return np.max(np.abs(v))

'''
Several of these functions have a similar version in scipy.stats.mstats which work for masked arrays.

gmean(a[, axis, dtype]) Compute the geometric mean along the specified axis. 
hmean(a[, axis, dtype]) Calculates the harmonic mean along the specified axis. 
cmedian(a[, numbins]) Returns the computed median value of an array. 
mode(a[, axis]) Returns an array of the modal (most common) value in the passed array. 
tmean(a[, limits, inclusive]) Compute the trimmed mean 
tvar(a[, limits, inclusive]) Compute the trimmed variance 
tmin(a[, lowerlimit, axis, inclusive]) Compute the trimmed minimum 
tmax(a, upperlimit[, axis, inclusive]) Compute the trimmed maximum 
tstd(a[, limits, inclusive]) Compute the trimmed sample standard deviation 
tsem(a[, limits, inclusive]) Compute the trimmed standard error of the mean 
moment(a[, moment, axis]) Calculates the nth moment about the mean for a sample. 
variation(a[, axis]) Computes the coefficient of variation, the ratio of the biased standard deviation to the mean. 
skew(a[, axis, bias]) Computes the skewness of a data set. 
kurtosis(a[, axis, fisher, bias]) Computes the kurtosis (Fisher or Pearson) of a dataset. 
describe(a[, axis]) Computes several descriptive statistics of the passed array. 
skewtest(a[, axis]) Tests whether the skew is different from the normal distribution. 
kurtosistest(a[, axis]) Tests whether a dataset has normal kurtosis 
normaltest(a[, axis]) Tests whether a sample differs from a normal distribution 
itemfreq(a) Returns a 2D array of item frequencies. 
scoreatpercentile(a, per[, limit]) Calculate the score at the given per percentile of the sequence a. 
percentileofscore(a, score[, kind]) The percentile rank of a score relative to a list of scores. 
histogram2(a, bins) Compute histogram using divisions in bins. 
histogram(a[, numbins, defaultlimits, ...]) Separates the range into several bins and returns the number of instances of a in each bin. 
cumfreq(a[, numbins, defaultreallimits, weights]) Returns a cumulative frequency histogram, using the histogram function. 
relfreq(a[, numbins, defaultreallimits, weights]) Returns a relative frequency histogram, using the histogram function. 
obrientransform(*args) Computes a transform on input data (any number of columns). 
signaltonoise(a[, axis, ddof]) Calculates the signal-to-noise ratio, defined as the ratio between the mean and the standard deviation. 
bayes_mvs(data[, alpha]) Return Bayesian confidence intervals for the mean, var, and std. 
sem(a[, axis, ddof]) Calculates the standard error of the mean (or standard error of measurement) of the values in the input array. 
zmap(scores, compare[, axis, ddof]) Calculates the relative z-scores. 
zscore(a[, axis, ddof]) Calculates the z score of each value in the sample, relative to the sample mean and standard deviation. 
threshold(a[, threshmin, threshmax, newval]) Clip array to a given value. 
trimboth(a, proportiontocut) Slices off a proportion of items from both ends of an array. 
trim1(a, proportiontocut[, tail]) Slices off a proportion of items from ONE end of the passed array 
f_oneway(*args) Performs a 1-way ANOVA. 
pearsonr(x, y) Calculates a Pearson correlation coefficient and the p-value for testing 
spearmanr(a[, b, axis]) Calculates a Spearman rank-order correlation coefficient and the p-value 
pointbiserialr(x, y) Calculates a point biserial correlation coefficient and the associated p-value. 
kendalltau(x, y[, initial_lexsort]) Calculates Kendall’s tau, a correlation measure for ordinal data. 
linregress(x[, y]) Calculate a regression line 
ttest_1samp(a, popmean[, axis]) Calculates the T-test for the mean of ONE group of scores a. 
ttest_ind(a, b[, axis]) Calculates the T-test for the means of TWO INDEPENDENT samples of scores. 
ttest_rel(a, b[, axis]) Calculates the T-test on TWO RELATED samples of scores, a and b. 
kstest(rvs, cdf, **kwds[, args, N, ...]) Perform the Kolmogorov-Smirnov test for goodness of fit 
chisquare(f_obs[, f_exp, ddof]) Calculates a one-way chi square test. 
ks_2samp(data1, data2) Computes the Kolmogorov-Smirnof statistic on 2 samples. 
mannwhitneyu(x, y[, use_continuity]) Computes the Mann-Whitney rank test on samples x and y. 
tiecorrect(rankvals) Tie-corrector for ties in Mann Whitney U and Kruskal Wallis H tests. 
ranksums(x, y) Compute the Wilcoxon rank-sum statistic for two samples. 
wilcoxon(x[, y]) Calculate the Wilcoxon signed-rank test 
kruskal(*args) Compute the Kruskal-Wallis H-test for independent samples 
friedmanchisquare(*args) Computes the Friedman test for repeated measurements 
ansari(x, y) Perform the Ansari-Bradley test for equal scale parameters 
bartlett(*args) Perform Bartlett’s test for equal variances 
levene(*args, **kwds) Perform Levene test for equal variances 
shapiro(x[, a, reta]) Perform the Shapiro-Wilk test for normality. 
anderson(x[, dist]) Anderson-Darling test for data coming from a particular distribution 
binom_test(x[, n, p]) Perform a test that the probability of success is p. 
fligner(*args, **kwds) Perform Fligner’s test for equal variances 
mood(x, y) Perform Mood’s test for equal scale parameters 
oneway(*args, **kwds) Test for equal means in two or more samples from the normal distribution. 
glm(data, para) Calculates a linear model fit ... 
'''    