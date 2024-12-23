def show_seats(total, booked):
    available = [seat for seat in range(1, total + 1) if seat not in booked]
    print(f"Available: {available}")
    print(f"Booked: {booked}")

def book(total, booked, seat):
    if seat < 1 or seat > total:
        return f"Seat {seat} is invalid."
    if seat in booked:
        return f"Seat {seat} is already booked."
    booked.append(seat)
    return f"Seat {seat} booked."

def cancel(booked, seat):
    if seat in booked:
        booked.remove(seat)
        return f"Seat {seat} canceled."
    return f"Seat {seat} was not booked."

total = int(input("Total seats: "))
booked = list(map(int, input("Booked seats (space-separated): ").split()))

while True:
    print("\n1. Show Seats\n2. Book Seat\n3. Cancel Booking\n4. Exit")
    choice = int(input("Choice: "))
    
    if choice == 1:
        show_seats(total, booked)
    elif choice == 2:
        seat = int(input("Seat to book: "))
        print(book(total, booked, seat))
    elif choice == 3:
        seat = int(input("Seat to cancel: "))
        print(cancel(booked, seat))
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
