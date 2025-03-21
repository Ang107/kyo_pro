# Description: Calculate AHC rating ver.2
# Usage: python calc_rating.py <user_name>
# Requires: requests
# ref) https://img.atcoder.jp/file/AHC_rating_v2.pdf
import argparse
import math
from datetime import date, datetime

import requests


def download_json(user_name: str):
    url = f"https://atcoder.jp/users/{user_name}/history/json?contestType=heuristic"
    response = requests.get(url)
    response.raise_for_status()

    return response.json()


def calc_rating(json: list):
    Q = []
    S = 724.4744301
    R = 0.8271973364

    for result in json:
        if not result["IsRated"]:
            continue

        end_date = datetime.fromisoformat(result["EndTime"]).date()
        days = (date.today() - end_date).days
        performance = result["Performance"] + 150 - 100 * days / 365
        weight = 1

        for i in range(100):
            Q.append((performance - S * math.log(i + 1), weight))

    if len(Q) == 0:
        return 0

    Q.sort(reverse=True)
    si = 0
    rating = 0

    for q, weight in Q:
        rating += q * (math.pow(R, si) - math.pow(R, si + weight))
        si += weight

    rating = 400 / (math.exp((400 - rating) / 400)) if rating < 400 else rating

    return rating


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user_name", type=str, help="AtCoder user name")
    args = parser.parse_args()
    json = download_json(args.user_name)
    rating = calc_rating(json)
    print(f"rating: {rating}")
