# An Automatic Customized Portfolio Construction CLI Application

# Import modules
import pandas as pd
import questionary
import matplotlib.pyplot as plt
from MCForecastTools import MCSimulation
import utility as ut



# Create a function called `portoflio_construction` that will construct a portfolio based on users' weights
# This function will be called from the `__main__` loop.

def portoflio_construction(tickers_weights, customer_initial_investment, simulation_times):


    ###Part 1: Prepare the data

    print("\n.....Running the App.....\n")

    
    #Get API Data in a dataframe
    prices_df = ut.get_data(tickers)




    ###Part 2: Plot Efficient Frontier
    
    print("\n.....Displaying Efficient Frontier......\n")

    #Prepare data for Efficient Frontier Calculation

    returns = []

    for ticker in tickers:
        returns.append(ut.asset_return(prices_df[ticker]["close"]))

    total_returns = pd.concat(returns, axis = 1)
    er = ut.annualize_rets(total_returns, 252)
    cov = total_returns.cov()
    ef = ut.ef2(100, er, cov)
    plt.title("Efficient Frontier")
    plt.plot(ef["Volatility"], ef["Returns"])
    plt.xlabel("Volatility")
    plt.ylabel("Return")
    plt.show()





    ###Part 3:Run the MC simulation
    
    #set up MC simulation
    MC_weight = MCSimulation(
      portfolio_data = prices_df,
      weights = tickers_weights,
      num_simulation = simulation_times,
      num_trading_days = 252*3)
    
    MC_weight.calc_cumulative_return()
    
    MC_weight_table = MC_weight.summarize_cumulative_return()


    #Display the simulation result
    print("\n......Your Simulated Portfolio Results.....\n")
    print (MC_weight_table)
    



    ###Part 4:Visuallation

    #Print the simulated portfolio allocation
    portfolio_allocation = tickers_weights
    portfolio_labels = tickers

    plt.title("Simulated Portfolio Allocation")
    plt.pie(portfolio_allocation, labels=portfolio_labels, autopct="%0.0f%%")
    plt.show()
    

    #Prepare the simulated returns data
    simulate_mean = list(MC_weight.simulated_return.mean(axis=1))
    simulate_median = list(MC_weight.simulated_return.median(axis=1))
    simulate_min = list(MC_weight.simulated_return.min(axis=1))
    simulate_max = list(MC_weight.simulated_return.max(axis=1))


    #Print the simulated daily returns
    plt.plot(simulate_mean, label = "mean")
    plt.plot(simulate_median, label = "median")
    plt.plot(simulate_min, label = "min")
    plt.plot(simulate_max, label = "max")
    plt.legend(title = "4 Simulation Path")
    plt.title("Simulated Daily Returns Behaviors of Your Portfolio Over the Next 3 Years")
    plt.xlabel("Number of Days")
    plt.ylabel("Portfolio Value Multiplier")
    plt.show()


    #Print the simulated investment result

    simulate_pnl_mean = [element * customer_initial_investment for element in simulate_mean]
    simulate_pnl_median = [element * customer_initial_investment for element in simulate_median]
    simulate_pnl_min = [element * customer_initial_investment for element in simulate_min]
    simulate_pnl_max = [element * customer_initial_investment for element in simulate_max]

    plt.plot(simulate_pnl_mean, label = "mean")
    plt.plot(simulate_pnl_median, label = "median")
    plt.plot(simulate_pnl_min, label = "min")
    plt.plot(simulate_pnl_max, label = "max")
    plt.legend(title = "4 Simulation Path")
    plt.title(f"Your Simulated Portfolio Performance of Initial Investment ${customer_initial_investment} Over the Next 3 Years")
    plt.xlabel("Number of Days")
    plt.ylabel("Portfolio Value")
    plt.show()




    ###Part 4: Calculate the results of the simulated portfolio


    #Calculate the lower and upper bound of returns
    ci_lower_three_cumulative_return = MC_weight_table[8] * customer_initial_investment
    ci_upper_three_cumulative_return = MC_weight_table[9] * customer_initial_investment

    #Suppose the risk-free rate is 2%
    risk_free_rate = 0.02

    #Calculate the Sharpe ratio
    sharpe_ratio = (MC_weight_table[1] - risk_free_rate) / MC_weight_table[2]
    
    # Create a statement that displays the `results` of simulated portfolio calculation.
    # On a separate line (\n) ask the use if they would like to continue running the application.
    results = f"There is a 95% chance that an initial investment of ${customer_initial_investment} in the simulated portfolio over the next 3 years will end within in the range of ${ci_lower_three_cumulative_return: .2f} and ${ci_upper_three_cumulative_return: .2f}. The Sharpe ratio of your simulated portfolio is {sharpe_ratio: .2f}"
    
    # Using the `results` statement created above,
    # prompt the user to run the report again (`y`) or exit the program (`n`).
    continue_running = questionary.select(results, choices=['y', 'n']).ask()

    # Return the `continue_running` variable from the `portoflio_construction` function
    return continue_running



# The `__main__` loop of the application.
# It is the entry point for the program.
if __name__ == "__main__":

    # Print a welcome and instruction message for the application

    print("\n......Welcome to Automatic Portfolio Construction APP.....\n")

    print("The portfolio will be constructed based on your choice\n")

    print("We will forecast and display the result of your simulated portfolio in the next 3 years through Monte Carlo Simulation\n")
    
    print("Before running the simulation, we will show you the Efficient Frontier displaying a set of optimal portfolios that offer the highest expected return for a defined level of risk. Each point on the frontier representing an optimal portfolio\n")

    print("\n......Instruction.....\n")

    print("Step 1: Please enter your desired 2 tickers in your portfolio (for bonds exposure please choose AGG or TLT). For example, AGG BA \n")
    print("Step 2: Please enter your desired tickers weights in your portfolio. For example, 0.3 0.7 \n")
    print("REMEMBER: The numbers entered in the first step and the second step should be added equal to 1. \n")
    print("Step 3: Please enter your initial investment for your simulated portfolio. \n")
    print("Step 4: Please enter how many simulations to run. Recommendation: 400, but please enter the times based on your need. \n")
    
    # Let the users customize their portfolios with tickers' weights, initial investment, and simulation times
    customer_tickers = questionary.text("What are your desired 2 tickers in the portfolio?").ask()
    customer_tickers_weights = questionary.text("What are your desired tickers weights in the portfolio?").ask()
    customer_initial_investment = questionary.text("What's your intial investment for your simulated portfolio?").ask()
    simulation_times = questionary.text("How many simulations do you want to run?").ask()

    tickers = []
    tickers = list(filter(None, customer_tickers.split()))
    tickers_weights = list(map(float, list(filter(None, customer_tickers_weights.split()))))
    customer_initial_investment = float(customer_initial_investment)
    simulation_times = int(simulation_times)


    # Create a variable named running and set it to True
    running = True

    # While running is `True` call the `portoflio_construction` function.
    # Pass the "tickers_weights", "customer_initial_investment", and "simulation_times" as parameters.
    while running:

        # Use the conditional statement to prevent the wrong weights input
        sum_of_tickers_weights = sum(tickers_weights)
        number_of_tickers = len(tickers)

        if number_of_tickers == 2:
            if sum_of_tickers_weights == 1.0:
                continue_running = portoflio_construction(tickers_weights, customer_initial_investment, simulation_times)
                if continue_running == 'y':
                    running = True
                else:
                    running = False
            else:
                print ("Sorry, please input the correct weights and try again. Remember, two weights should be added equal to 1")
                running = False
        else:
            print ("Sorry, please input strictly 2 tickers and try again.")
            running = False
