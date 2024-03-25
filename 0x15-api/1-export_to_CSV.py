#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + f"users/{sys.argv[1]}").json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]

    with open(f"{sys.argv[1]}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow([sys.argv[1], user.get("name"),
                             t.get("completed"), t.get("title")])
