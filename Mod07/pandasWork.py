import pandas as pd

sal = pd.read_csv('C:\Users\tbani\OneDrive\Documents\Homework\SDEV Python\M01 Collab\Mod07\Salaries.csv')

sal.head()
sal.info()
sal['BasePay'].mean()
sal['OvertimePay'].max()
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
sal[['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']
sal[['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName']
sal.groupby('Year').mean()['BasePay']
sal['JobTitle'].nunique()
sal['JobTitle'].value_counts().head(5)
sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)

def chief_count(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

sum(sal['JobTitle'].apply(lambda x: chief_count(x)))


