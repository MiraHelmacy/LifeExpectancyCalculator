import argparse
import random

parser = argparse.ArgumentParser("LifeExpectencyCalculator",description="Calulates the life expectency based on child mortality rate")

MIN_CHILD_AGE = 0
MAX_CHILD_AGE = 16
MIN_ADULT_AGE = 35
MAX_ADULT_AGE = 70
POPULATION = 1000

def init():
  global parser
  global MIN_CHILD_AGE
  global MAX_CHILD_AGE
  global MIN_ADULT_AGE
  global MAX_ADULT_AGE
  global POPULATION

  parser.add_argument("--infant-mortality-percentage", type=int, required=True, help="The number of people who die before reaching reproductive age")
  parser.add_argument("--min-child-age", type=int, required=False, default=MIN_CHILD_AGE, help="The minimum age to consider a child death")
  parser.add_argument("--max-child-age", type=int, required=False, default=MAX_CHILD_AGE, help="The maximum age to consider a child death")
  parser.add_argument("--min-adult-age", type=int, required=False, default=MIN_ADULT_AGE, help="The minimum age to consider an adult death")
  parser.add_argument("--max-adult-age", type=int, required=False, default=MAX_ADULT_AGE, help="The maximum age to consider an adult death")
  parser.add_argument("--population", type=int, required=False, default=POPULATION, help="The total population size")

def validateArgs(infant_mortality_rate, min_child_age, max_child_age, min_adult_age, max_adult_age, population):
  #validate there are people
  if population <= 0:
    raise ValueError("Population must be greater than 0")
  
  #min child age cannot be negative
  if min_child_age < 0:
    raise ValueError("Min Child Arge must be greater than 0")

  #max child age cannot be negative
  if max_child_age < 0:
    raise ValueError("Max Child Age must be greater than 0")

  #max child age must be greater than min child age
  if min_child_age >= max_child_age:
    raise ValueError("Min Child Age must be less than Max Child Age")

  #min adult age must be less than max adult age
  if min_adult_age >= max_adult_age:
    raise ValueError("Min Adult Age must be less than Max Adult Age")

  #min adult age must be greater than max child age
  if min_adult_age <= max_child_age:
    raise ValueError("Min Adult Age must be greater than Max Child Age")

  if infant_mortality_rate not in range(0, 101):
    raise ValueError("Infant Mortality Percentage must be between 0 and 100")

def calculateDeathAge(low, high):  
  return random.randrange(low, high)

def surviveToAdulthood(infant_mortality_percentage):
  return random.randrange(0, 100) > infant_mortality_percentage

def calculateLifeExpectency(infant_mortality_percentage, min_child_age, max_child_age, min_adult_age, max_adult_age, population):
  total_population_age = 0

  for _ in range(0, population):
    age_of_current_person = None
    
    if surviveToAdulthood(infant_mortality_percentage):
      age_of_current_person = calculateDeathAge(min_adult_age, max_adult_age)
    else:
      age_of_current_person = calculateDeathAge(min_child_age, max_child_age)
    total_population_age += age_of_current_person

  return total_population_age / population

def main(args):
  infant_mortality_percentage = args.infant_mortality_percentage
  min_child_age = args.min_child_age
  max_child_age = args.max_child_age
  min_adult_age = args.min_adult_age
  max_adult_age = args.max_adult_age
  population = args.population

  try:
    validateArgs(infant_mortality_percentage, min_child_age, max_child_age, min_adult_age, max_adult_age, population)
  except ValueError as ve:
    global parser
    parser.print_help()
    print(ve)
    exit(1)

  

  print("Average Life Expetency: %s" % calculateLifeExpectency(infant_mortality_percentage, min_child_age, max_child_age, min_adult_age, max_adult_age, population))

if __name__ == '__main__':
  init()
  main(parser.parse_args())