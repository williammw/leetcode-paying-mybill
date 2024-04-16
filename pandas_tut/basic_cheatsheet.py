import pandas as pd


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
  return pd.DataFrame(student_data, columns=['student_id', 'ag'])


def getDataframeSize(players: pd.DataFrame) -> List[int]:
  return list(players.shape)


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
  return employees[:3]


def selectData(students: pd.DataFrame) -> pd.DataFrame:
  return students[students['student_id'] == 101][['name', 'age']]

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
  employees['bonus'] = employees['salary'] * 2
  return employees

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
  return customers.drop_duplicates(subset='email')


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
  return students.dropna(subset=['name'])
  # return students.dropna()


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
  employees['salary'] = employees['salary'] + 5000
  return employees


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
  return pd.concat([df1, df2])


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
  return weather.pivot(index='date', columns='city', values='temperature')


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
  melted_table = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
  return melted_table


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
  x = animals[animals['weight'] > 100]
  x = x.sort_values(by='weight', ascending=False)
  return x[['name']]


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
  students = students.rename(columns={'name': 'student_name', 'age': 'student_age'})
  return students