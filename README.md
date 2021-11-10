# Portfolio Construction Application

## About The Project

This project is a Command Line Interface (CLI) that was created as a tool for investors to visualize various Monte Carlo simulations of a hypothetical portfolio based on bonds and equity markets. The project leverages the Alpaca API to collect 3 years of historical data for bond and equity markets (AGG and SPY). The application uses Questionary to collect input values from the user to construct the simulations and visualizations based on their desired portfolio composition. Users have the ability to customize the portfolio weight for bonds and equities, their desired initial investment, and the number of Monte Carlo simulations they would like to run. After the simulations are run, the users will receive visual plots regarding their portfolio composition, the results of the Monte Carlo simulations, the simulated returns over the next 3 years, the 95% confidence interval of the simulated portfolio, the efficient frontier, and the Sharpe ratio.

## Technologies

This project leverages Python 3.7 with the following packages and libraries:

Pandas
SQLalchemy
Questionary
MCForecastTools
Matplotlib
Numpy
Alpaca API
dotenv
os

## Installation

1. Acquire a free API key from alpaca at https://alpaca.markets/.
2. Enter your API key in a .env file as such:
    ALPACA_API_KEY = “Your Alpaca API Key Here”
    ALPACA_SECRET_KEY = “Your Alpaca Secret Key Here”
3. Clone the repo to your local machine.
4. Install the required packages in your dev environment:
    SQLAlchemy:
    ```
    pip install sqlalchemy
    ```
    
    Fire & Questionary:
    ```
    pip install fire
    pip install questionary
    ```
    Alpaca:
    ```
    pip install alpaca-trade-api
    ```
    

## Usage

To use this application, simply clone the repo and open the Automatic_Portfolio_Construction.py file in your terminal. You will prompted with various questions regarding your desired portfolio composition. You will first be asked for your desired weight for the bonds allocation of your portfolio. Then you will be asked for your desired weight for the stock portion of your portfolio. Enter a percentage value as a decimal (i.e. 0.4 for 40% weight). Then, enter the initial investment size in US dollars that you would like to allocate for your portfolio. Lastly, enter the number of Monte Carlo simulations you would like to run. The higher the number of simulations, the greater the theoretical accuracy of the data. The output will return the results of the simulated portfolio.


## Contributors

Ziwen Chen, Shasha Li, Austin Do, Malika Kudaibergenova


