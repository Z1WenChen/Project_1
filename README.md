# Portfolio Construction Application

## About The Project

This project is a Command Line Interface (CLI) that was created as a tool for investors to visualize various Monte Carlo simulations of a hypothetical portfolio based on bonds and equity markets. Investors face a great deal of uncertainty and risk in their investment decisions. This application was built with the goal of clarifying that uncertainty through the concepts of probability distribution and portfolio forecasting. 

The project leverages the Alpaca API to collect 3 years of historical data for bond and equity markets (AGG and SPY). The historical data is used to predict future outcomes through Monte Carlo simulations. 

This application offers a variety of user customizations. The project uses Questionary to collect input values from the user to construct the simulations and visualizations based on their desired portfolio composition. Users have the ability to customize the portfolio weight for 2 different tickers, their desired initial investment, and the number of Monte Carlo simulations they would like to run. After the simulations are run, the users will receive visual plots regarding their portfolio composition, the results of the Monte Carlo simulations, the simulated returns over the next 3 years, the 95% confidence interval of the simulated portfolio, the efficient frontier, and the Sharpe ratio.

## Technologies

This project leverages Python 3.7 with the following packages and libraries:

Pandas
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
    ```
    ALPACA_API_KEY = “Your Alpaca API Key Here”
    ALPACA_SECRET_KEY = “Your Alpaca Secret Key Here”
    ```
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

To use this application, simply clone the repo and open the Automatic_Portfolio_Construction.py file in your terminal. You will prompted with various questions regarding your desired portfolio composition.

Example of application instructions and hypothetical user input in CLI:
![CLI_1 Instructions](https://user-images.githubusercontent.com/89161654/141343448-46a2b53a-2eab-4dfc-ab19-3a16fea420ba.png)


You will first be asked to input your desired 2 tickers for your simulated portfolio. We recommend mixing asset classes such as bonds and equities. Then you will be asked to input your desired portfolio weight for the tickers you have chosen. Enter a percentage value as a decimal (i.e. 0.4 for 40% weight). Then, enter the initial investment size in US dollars that you would like to allocate for your portfolio. Lastly, enter the number of Monte Carlo simulations you would like to run. The higher the number of simulations, the greater the theoretical accuracy of the data. The output will return the results of the simulated portfolio.

Example of Returned Figures:

1. Efficient Frontier
![Figure_1](https://user-images.githubusercontent.com/89161654/141343598-e23bcc8f-6b5c-4752-999c-60aebd27e753.png)

2. Portfolio Composition
![Figure_2 Portfolio Composition](https://user-images.githubusercontent.com/89161654/141343602-aa0f1881-f0b2-4ee6-b45d-84ab98ffa9ca.png)

3. Simulated Returns Over the Next 3 Years
![Figure_3 Simulated Returns](https://user-images.githubusercontent.com/89161654/141343591-d5fade78-9ead-4cf1-a8e4-fd4d2f5975ce.png)

4. Simulated Portfolio Performance Over the Next 3 Years
![Figure_4 Simulated Portfolio Performance](https://user-images.githubusercontent.com/89161654/141343595-ee22ff71-82fe-4093-93e9-3cfb2596bb2a.png)

5. 95% Confidence Interval and Sharpe Ratio in CLI
![CLI_2 95 CI and Sharpe](https://user-images.githubusercontent.com/89161654/141343720-fdfb572c-608a-4720-a791-bc02e7883f72.png)




## Contributors

Ziwen Chen (zc1418@nyu.edu), Shasha Li (shasha867619.sl@gmail.com), Austin Do (austindotech@gmail.com), Malika Kudaibergenova (malika.kdb@gmail.com)

## License
MIT


