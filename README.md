### Problem:
Given two teams predict the score

### Usage
Change the teams in `mc_rugby_match_outcome_prediction/main.py` to calculate the predicted score

### Data:
We will only use data from the last 
results.csv
```
date,
home_team,
away_team,
home_score,
away_score,
competition,
stadium,
city,
country,
neutral,
world_cup
```

## Formula Options

### Basic (Current implementation)
**Score for team A** = avg(score_for_team_when_playing_team_b) + random(-1 -> 1) * std(score_for_team_when_playing_team_b)

### Weighted Approach based on time (Not Implemented)
More recent results should be weighted higher when calculating the avg and std
- results > 50 years ago should not be included
- 25 < results <= 50 years ago can be weighted with a 0.1 coefficient
- 5 < results <= 25 years ago can be weighted with a 0.2 coefficient
- 2 < results <= 5 years ago can be weighted with a 0.3 coefficient
- results <= 2 years ago can be weighted with a 0.4 coefficient

## Model Evaluation
We will use backtesting