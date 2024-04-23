import pandas as pd
from mc_rugby_match_outcome_prediction.team import Team
from mc_rugby_match_outcome_prediction.match import Match


class MCSimulation:
  def __init__(self, team_a_name, team_b_name, num_simulations):
    self.num_simulations = num_simulations

    self.team_a_name = team_a_name
    self.team_b_name = team_b_name
    self.team_a = Team(team_a_name)
    self.team_b = Team(team_b_name)

    self.__build_df()
  
  def __build_df(self):
    all_data = pd.read_csv("results.csv")
    both_teams = [self.team_a_name, self.team_b_name]
    self.team_a_vs_team_b_data = all_data[
      (all_data["home_team"].isin(both_teams)) & (all_data["away_team"].isin(both_teams))
    ]
  
  def __simulate_a_match(self, iteration):
    if iteration % 500 == 0:
      print(f"Simulation No. {iteration}\n")

    match = Match(self.team_a, self.team_b, self.team_a_vs_team_b_data)
    result = match.simulate()
    return {
      self.team_a_name: result["team_a"],
      self.team_b_name: result["team_b"]
    }
  
  def simulate_multiple_matches(self):
    results = [self.__simulate_a_match(i) for i in range(self.num_simulations)]
    self.results_df = pd.DataFrame(results)
    print("Expected Score:")
    print(self.results_df.mean())


