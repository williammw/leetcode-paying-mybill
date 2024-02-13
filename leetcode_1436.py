# %%
def destCity(self, paths):
  """
  :type paths: List[List[str]]
  :rtype: str
  """
  startCities = set()
  destCities = set()

  for startCity, destCity in paths:
    startCities.add(startCity)
    destCities.add(destCity)

  # destcity will never show on startCities, so
  ans = destCities - startCities
  return ans.pop()
# %%
