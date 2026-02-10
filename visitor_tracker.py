from datetime import datetime

USER_NAME = "ANEELA IQBAL"

def log_visitor():
    with open("visitors.txt", "a") as file:
        file.write(f"{USER_NAME} - Visited on: {datetime.now()}\n")

def count_visitors():
    try:
        with open("visitors.txt", "r") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0

def main():
    print("👋 Welcome to MyVisitorTracker")

    log_visitor()
    total_visits = count_visitors()

    print(f"Total Visits: {total_visits}")

if __name__ == "__main__":
    main()

