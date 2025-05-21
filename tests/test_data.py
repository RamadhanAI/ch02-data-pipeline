import pandas as pd

def test_airline_delay_data():
    df = pd.read_csv("data/airline_delay.csv")
    assert df["departure_delay"].isna().mean() < 0.10, "Too many missing departure delays"
    assert df["arrival_delay"].isna().mean() < 0.10, "Too many missing arrival delays"
    assert df["air_time"].min() >= 30, "Some air_time values are unrealistically low"
    assert df["distance"].min() >= 100, "Distance values are too low"
    print("✅ All data validation checks passed.")

if __name__ == "__main__":
    test_airline_delay_data()
