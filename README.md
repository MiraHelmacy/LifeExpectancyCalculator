# Life Expectancy Calculator

Calculate the Life Expectancy of the average adult based on the infant mortality rate and population size. 

## Usage
```
usage: LifeExpectencyCalculator [-h] --infant-mortality-percentage INFANT_MORTALITY_PERCENTAGE
                                [--min-child-age MIN_CHILD_AGE] [--max-child-age MAX_CHILD_AGE]
                                [--min-adult-age MIN_ADULT_AGE] [--max-adult-age MAX_ADULT_AGE]
                                [--population POPULATION]

options:
  -h, --help            show this help message and exit
  --infant-mortality-percentage INFANT_MORTALITY_PERCENTAGE
                        The number of people who die before reaching reproductive age
  --min-child-age MIN_CHILD_AGE
                        The minimum age to consider a child death
  --max-child-age MAX_CHILD_AGE
                        The maximum age to consider a child death
  --min-adult-age MIN_ADULT_AGE
                        The minimum age to consider an adult death
  --max-adult-age MAX_ADULT_AGE
                        The maximum age to consider an adult death
  --population POPULATION
                        The total population size
```

## Examples

The Python interpreter to use and the command to use depends on your operating system and how you invoke your python interpreter. Assuming you are using Linux, the command should be something like the following.

```
python3 main.py --infant-mortality-percentage 40
```

To add a population size use the population flag.
```
python3 main.py --infant-mortality-percentage 40 --population 1000000
```