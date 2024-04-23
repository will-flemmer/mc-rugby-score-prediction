import pandas as pd

from mc_rugby_match_outcome_prediction.team import Team

class Match:
  def __init__(self, team_a: Team, team_b: Team, df: pd.DataFrame):
    self.team_a = team_a
    self.team_b = team_b
    self.df = df
    
  def simulate(self):
    self.team_a.calculate_stats(self.df)
    self.team_a.predict_score()

    self.team_b.calculate_stats(self.df)
    self.team_b.predict_score()
    return {
      "team_a": self.team_a.predicted_score,
      "team_b": self.team_b.predicted_score,
    }