# A Database CLI Application

# Import modules
import pandas as pd
import sqlalchemy as sql
import os
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
import questionary

# Load .env file
load_dotenv()

# Set the variables for the Alpaca API and secret keys
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")


# Create a function called `Portfolio_selection` that will select portfolio for investors who are in the different level of risk-averse.
# This function will be called from the `__main__` loop.

def portoflio_selection(customer_weights):

    # Print a welcome message for the application
    print("\n......Welcome to the Portflio Selection APP.....\n")
    print("The portfolio will be constructed based your choice\n")

    # Using questionary, ask the investor what is his/her risk-aversion level
    customber_choose_weight = questionary.select("Which weights of portfolio you want?", choices = customer_weights).ask()

    print("Running report ...")
    
    #Get API data
    alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version = "v2")
    
    tickers = ["SPY", "AGG"]

    timeframe = "1D"

    start_date = pd.Timestamp("2019-01-02", tz = "America/New_York").isoformat()
    end_date = pd.Timestamp("2021-10-31", tz = "America/New_York").isoformat()
    
    
    prices_df = alpaca.get_barset(
    tickers,
    timeframe,
    start = start_date,
    end = end_date
    ).df
    
    
    
    #Run the MC simulation
    MC_weight = MCSimulation(
      portfolio_data = prices_df,
      weights = customber_choose_weight,
      num_simulation = 500,
      num_trading_days = 252*3)
    
    MC_weight.calc_cumulative_return()
    
    
    MC_weight_line_plot = MC_weight.plot_simulation()
    
    
    MC_weight_distribution_plot = MC_weight.plot_distribution()
    
    
    MC_weight_table = MC_weight.summarize_cumulative_return()
    
    
    #Visuallation
    simulated_returns_data = {
    "mean": list(MC_weight.simulated_return.mean(axis=1)),
    "median": list(MC_weight.simulated_return.median(axis=1)),
    "min": list(MC_weight.simulated_return.min(axis=1)),
    "max": list(MC_weight.simulated_return.max(axis=1))}
    
    
    df_simulated_returns = pd.DataFrame(simulated_returns_data)
    
    df_simulated_returns.plot(title="Simulated Daily Returns Behavior of simulated portfolio Over the Next 3 Years")
    
    initial_investment = 10000

    ci_lower_three_cumulative_return = MC_weight_table[8] * initial_investment
    ci_upper_three_cumulative_return = MC_weight_table[9] * initial_investment

    risk_free_rate = 0.02

    sharpe_ratio = (MC_weight_table[1] - risk_free_rate) / MC_weight_table[2]
    
    # Create a statement that displays the `results` of your sector_yearly_return calculation.
    # On a separate line (\n) ask the use if they would like to continue running the report.
    results = f"There is a 95% chance that an initial investment of ${initial_investment} in the stock and bond portion of portfolio with a simulated portfolio over the next 3 years will end within in the range of {ci_lower_three_cumulative_return: .2f} and ${ci_upper_three_cumulative_return: .2f}. The Sharpe ratio of the simulated portfolio is {sharpe_ratio: .2f}"
    
    cumulative_pnl = initial_investment * df_simulated_returns
    
    cumulative_pnl.plot(title="Simulated Outcomes Behavior of the Portfolio Over the Next 3 Years")
    
    portfolio_allocation = customber_choose_weight

    portfolio_df = pd.DataFrame(
    {"amount": [portfolio_allocation[0], portfolio_allocation[1]]},
    index = ["AGG", "SPY"])
    
    
    portfolio_df.plot(
    kind = "pie",
    y='amount', 
    title="The Money Growth Portfolio Composition: 20% Bond and 80% Stock"
    )
    
    
    # Using the `results` statement created above,
    # prompt the user to run the report again (`y`) or exit the program (`n`).
    continue_running = questionary.select(results, choices=['y', 'n']).ask()

    # Return the `continue_running` variable from the `sector_report` function
    return continue_running



# The `__main__` loop of the application.
# It is the entry point for the program.
if __name__ == "__main__":

    # Want to link investors' risk-averse level with the portfolio
    # Risk-Averse Level is measured from 1 - 5: 
    # 1: Least risk-averse, 5: Most risk-averse
    # 1: Most aggressive portfolio, Portfolio 2080
    # 5: Most conservative portfolio, Portfolio 8020
    customer_weights = [[.2,.8], [.4,.6], [.5,.5], [.6,.4], [.8,.2]]

    # Create a variable named running and set it to True
    running = True

    # While running is `True` call the `sector_report` function.
    # Pass the `nyse_df` DataFrame `sectors` and the database `engine` as parameters.
    while running:
        continue_running = portoflio_selection(customer_weights)
        if continue_running == 'y':
            running = True
        else:
            running = False
