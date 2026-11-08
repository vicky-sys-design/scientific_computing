\# Task 2: NumPy Arrays and Numerical Computation



\## Inputs and operation

\- Input: 24 hourly temperatures in degrees Celsius, stored in one NumPy array.

\- Operations: mean, min and max summarise the day. The formula F = 1.8C + 32 is applied to every value at once (vectorized, no loop).



\## Output

Daily mean temperature: 23.12 C

Minimum temperature: 17.50 C

Maximum temperature: 29.40 C

First six Fahrenheit readings: \[65.3 64.4 64.04 63.5 64.22 66.2]



\## Parameter change

I added 5 C to every reading (a heat wave) with: temperatures\_c = temperatures\_c + 5

\- Mean rose from 23.12 to 28.12 C, minimum from 17.5 to 22.5 C, maximum from 29.4 to 34.4 C.

\- Every statistic shifted by exactly 5 C, because adding a constant shifts the whole data set.

\- The first Fahrenheit reading rose from 65.3 to 74.3 F, an increase of 9 F, because 5 x 1.8 = 9.



\## Interpretation

The day starts cool at about 17.5 C early in the morning, warms to a peak of about 29.4 C in the early afternoon, then cools again. The mean of 23.12 C is one number summarising the whole day, while the 24 readings show its shape.



\## New case: Kenyan greenhouse (new\_case.py)

Assumptions: hourly temperatures are invented. Tomatoes are stressed above 30 C and grow poorly below 18 C.



Output:

Mean: 23.75 C, Min: 15.0 C, Max: 35.6 C

Hours above 30 C: 7

Hours below 18 C: 8

Max in F: 96.1



Interpretation: The average of 23.75 C looks fine, but the greenhouse is outside the tomato range for 15 of 24 hours (7 too hot, 8 too cold). This shows how the mean alone can hide problems, and it suggests shade netting at midday and cover at night.

