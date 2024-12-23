def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    return base_fare + distance_fare

trips = list(map(int, input("Enter distances for trips (km) separated by spaces: ").split()))

total_fare = 0
for i, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    total_fare += fare
    print(f"Trip {i}: ${fare}")

print(f"Total Fare: ${total_fare}")
