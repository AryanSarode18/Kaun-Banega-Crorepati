# Welcome message
print("Welcome To KBC\n")

# List of questions
questions = [
    "Who is the current President of India",
    "Which player has won the most IPL cups",
    "Who was the Captain of Team India in 1983 World Cup",
    "What is the full form of 'py'"
]

# List of options along with the correct answer index
options = [
    ["1. Rajendra Prasad", "2. Droupadi Murmu", "3. Dr. A. P. J. Abdul Kalam", "4. Ram Nath Kovind", 3],  # Correct: 4
    ["1. MSD", "2. Rohit Sharma", "3. Virat Kohli", "4. Shane Watson", 2],  # Correct: 3
    ["1. Mohinder Amarnath", "2. Ravi Shastri", "3. MSD", "4. Kapil Dev", 4],  # Correct: 4
    ["1. Python", "2. Previous Year", "3. Payment Year", "4. Polytechnic", 1]  # Correct: 1
]

# Points system
total_points = 0
points_per_question = 10

# Iterate through questions and options
for i in range(len(questions)):
    print(questions[i])
    for option in options[i][:4]:
        print(option)
    a = int(input("Select the Option : "))
    ans = options[i][4]

    # Check the answer and update points
    if a == ans:
        print("Correct Answer")
        total_points += points_per_question
    else:
        print("Oops, Wrong Answer")
        break  # Exit the loop on the first wrong answer

    print()  # Add a line break after each question

# Display total points earned
print(f"Total Points Earned: {total_points}")
