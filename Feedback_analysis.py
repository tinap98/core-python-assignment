def positive_feedback_percentage(ratings):
    if not ratings:
        return 0
    positive_count = sum(1 for rating in ratings if rating >= 4)
    return (positive_count / len(ratings)) * 100

ratings = list(map(int, input("Enter ratings (1-5) separated by spaces: ").split()))
percentage = positive_feedback_percentage(ratings)

if ratings:
    print(f"Positive Feedback: {percentage:.2f}%")
else:
    print("No ratings provided.")
