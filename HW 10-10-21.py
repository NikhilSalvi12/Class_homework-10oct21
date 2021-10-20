# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:25:47 2021

@author: NIKHIL
"""


import pandas as pd

mile_df = pd.read_excel('Millage_data.xlsx')

""" Q1. Find whether the average mileage driven by you is equal to 40KMPh for 
your data. (note Use =NORM.INV(RAND(),30,2.5) in excel to generate data. 
            Take at least 50 rows of data)"""


mile_df.columns

mile_df.describe()

""" 
X = Self (D)
Y = mileage (C)
alpha = 0.05
ho = mileage == 40
h1 = mileage != 40

"""
from scipy.stats import ttest_1samp

ttest_1samp(mile_df.Mileage, 40)

""" pvalue=4.526802893151997e-31
comparing p value with alpha 
we reject the null hypothesis and accept alternate hypothesis 
that our mileage is not equal to assumed mileage comparing mean its less than 
the expected millage"""


""" Q2. Find whether there is any significance difference in mileage between 
you and your driver while riding in the motor vehicle. """

comparemile = pd.read_excel('Comparative_Millage.xlsx')

comparemile.columns

comparemile.describe()

"""
X = PERSON (d)
y = Mileage (cont)
alpha = 0.05
ho: mu(driver)==mu(self)
h1: mu(driver)!=mu(self)
"""
from scipy.stats import ttest_ind

ttest_ind(comparemile.Self,comparemile.Driver)

""" pvalue=3.2544443599647577e-09
comparing p value with alpha 
we reject the null hypothesis and accept alternate hypothesis 
that our mileage is not equal to driver's mileage 
comparing mean we should take the decision to fire the driver"""

""" Q3. Test whether changing your the tyre pressure affects your milage 
or not. """

tyrepresure = pd.read_excel('tyrepressuremileage.xlsx')

tyrepresure.columns

tyrepresure.describe()

"""
X = tyre Pressure (d)
y = Mileage (cont)
alpha = 0.05
ho: mu(p30)==mu(p33)==mu(p35)
h1: mu(p30)!=mu(p33)!=mu(p35)
"""
from scipy.stats import f_oneway

f_oneway(tyrepresure.Psi_30, tyrepresure.Psi_33, tyrepresure.Psi_35)


""" pvalue=3.2523330920703444e-29
comparing p value with alpha 
we reject the null hypothesis and accept alternate hypothesis 
that mileage is affected by the tyre pressure"""

""" Q4. Test whether driving on different road condition changes your 
mileage or not """

road = pd.read_excel('roadcond_mileage.xlsx')

road.columns

road.describe()

"""
X = Road condition (d)
y = Mileage (cont)
alpha = 0.05
ho: mu(G)==mu(A)==mu(C)
h1: mu(G)!=mu(A)!=mu(C)
"""
f_oneway(road.Gravel,road.Asphalt,road.Cement)

""" pvalue=8.989117331832241e-56
comparing p value with alpha 
we reject the null hypothesis and accept alternate hypothesis 
that mileage is affected by the Road conditions 
hence, we conclude the best road to drive is Asphalt 
considering the higest mean"""
