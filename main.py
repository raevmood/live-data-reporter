from astronauts import fetch_astronauts
from iss_tracker import track_iss
from news_or_stock import fetch_news_or_stock

def menu():
    while True:
        print("\n=== Live Data Reporter ===")
        print("1. View astronauts in space")
        print("2. Track ISS location")
        print("3. View business news or IBM stock")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            fetch_astronauts()
        elif choice == '2':
            track_iss()
        elif choice == '3':
            fetch_news_or_stock()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
