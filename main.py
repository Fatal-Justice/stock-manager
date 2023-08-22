import gspread
import pandas as pd
import numpy as np

# Create worksheet
sa = gspread.service_account(filename="service_account.json")
sh = sa.open("Arsh Copy Shares and MF Portfolio ")
wks_trades = sh.worksheet("Trades")
wks_balance = sh.worksheet("Trades Balance")

# Creating Trade DF
df_trade: pd.DataFrame = pd.DataFrame(wks_trades.get_all_values())
df_trade: pd.DataFrame = df_trade.rename(columns=df_trade.iloc[0]).drop(df_trade.index[0])
df_trade.reset_index(inplace=True, drop=True)
df_trade: pd.DataFrame = df_trade.loc[:, "Firm":"Rate"]

# Creating Buy and Sell DFs
df_buy: pd.DataFrame = df_trade.loc[df_trade["B/S"] == "Buy"]
df_sell: pd.DataFrame = df_trade.loc[df_trade["B/S"] == "Sell"]

# Creating Balance DF
df_balance: pd.DataFrame = pd.DataFrame(wks_balance.get_all_values())
df_balance: pd.DataFrame = df_balance.rename(columns=df_balance.iloc[0]).drop(df_balance.index[0])
df_balance.reset_index(inplace=True, drop=True)

# Adding buy entries
for i in df_buy.index:
    buy = [*list(df_buy.loc[i].values)[0:4], *list(df_buy.loc[i].values)[5:], *[np.nan for _ in range(4)]]
    df_balance.loc[len(df_balance)] = buy
