import numpy as np

class Team:
  def __init__(self, name):
    self.name = name

  def calculate_stats(self, matches_df):
    self.avg_score_against_opposition = self.__calculate_avg_score(matches_df)
    self.std_score_against_opposition = self.__calculate_std_of_score(matches_df)

  def __calculate_avg_score(self, matches_df):
    as_home = matches_df[matches_df["home_team"] == self.name]
    as_home_avg_score = as_home["home_score"].mean()
    
    as_away = matches_df[matches_df["away_team"] == self.name]
    as_away_avg_score = as_away["away_score"].mean()
    return np.mean([as_home_avg_score, as_away_avg_score])
  
  def __calculate_std_of_score(self, matches_df):
    as_home = matches_df[matches_df["home_team"] == self.name]
    as_home_std = as_home["home_score"].std()
    
    as_away = matches_df[matches_df["away_team"] == self.name]
    as_away_std = as_away["away_score"].std()
    return np.mean([as_home_std, as_away_std])


  def predict_score(self):
    self.predicted_score = np.random.normal(
      self.avg_score_against_opposition,
      3 * self.std_score_against_opposition
    )