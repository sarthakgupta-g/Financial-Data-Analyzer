# Financial-Data-Analyzer
# Financial Data Analyzer

## Overview

A Python-based financial data analysis project that uses Pandas to analyze historical stock price and trading volume data from a CSV file.

The program calculates price statistics, overall returns, daily returns, trading volume statistics, and identifies significant price movements.

## Features

- Loads historical stock data from a CSV file
- Inspects dataset structure and dimensions
- Calculates average, maximum, and minimum stock prices
- Calculates overall percentage return
- Calculates average trading volume
- Identifies the highest-volume trading day
- Identifies the highest and lowest stock prices and their dates
- Calculates daily percentage returns
- Identifies the best and worst daily returns
- Identifies days with price movements greater than ±2%
- Counts positive and negative trading days

## Technologies

- Python
- Pandas
- CSV

## Dataset

The dataset contains:

- `Date` — Trading date
- `Price` — Stock closing price
- `Volume` — Trading volume

The dataset is currently a small sample dataset created for learning and analysis.

## Example Analysis

The program outputs statistics such as:

- Average stock price
- Highest and lowest stock price
- Starting and ending price
- Overall return
- Average trading volume
- Highest-volume trading day
- Average daily return
- Best and worst daily returns
- Number of positive and negative trading days
- Days with daily returns greater than ±2%

## What I Learned

This project helped me practice using Pandas for financial data analysis, including:

- Loading CSV data into a DataFrame
- Inspecting DataFrames
- Selecting columns and rows
- Boolean filtering
- Working with Pandas Series
- Using `.iloc`
- Creating calculated columns
- Calculating percentage changes with `pct_change()`
- Using DataFrame methods such as `mean()`, `max()`, `min()`, and `shape`

## How to Run

1. Clone the repository.
2. Install the required dependency:

```bash
pip install pandas
