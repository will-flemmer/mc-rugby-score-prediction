from mc_rugby_match_outcome_prediction.mc_simulation import MCSimulation

if __name__ == "__main__":
  NUM_SIMULATION = 10_000
  simulation = MCSimulation("England", "South Africa", NUM_SIMULATION)
  simulation.simulate_multiple_matches()