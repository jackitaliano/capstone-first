import requests


def get_grid_forecast(gridx: str, gridy: str) -> dict:
    r = requests.get(f'https://api.weather.gov/gridpoints/TOP/{gridx},{gridy}/forecast')

    r_json = r.json()
    return r_json


def main():
    grid_x: str = "31"
    grid_y: str = "80"

    weather = get_grid_forecast(grid_x, grid_y)

    if weather is None:
        print("No weather :(")
        return

    forecast = weather.get("properties")

    if forecast is None:
        print("No forecast :(")
        return

    forecast_periods = forecast.get("periods")

    if forecast_periods is None:
        print("No forecast periods :(")
        return

    WIDTH: int = 80
    for period in forecast_periods:
        print("-" * WIDTH, "\n")
        print(f"{period.get('name'): ^80}", "\n")
        print("Temperature: ", period.get("temperature"), period.get("temperatureUnit"), "\n")
        print("Forecast: ", period.get("shortForecast"), "\n")


    print("-" * WIDTH)

main()
