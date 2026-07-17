questions = [
    ["What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    ["Which language is used for Python?", "Java", "Python", "C++", "PHP", 2],
    ["2 + 2 = ?", "3", "4", "5", "6", 2],
    ["Who developed Python?", "James Gosling", "Dennis Ritchie", "Guido van Rossum", "Bjarne Stroustrup", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2]
]

prizes = [1000, 5000, 10000, 50000, 100000]

money = 0

print("========== Welcome to KBC ==========\n")

for i in range(len(questions)):
    q = questions[i]

    print(f"Question {i+1} for ₹{prizes[i]}")
    print(q[0])
    print(f"1. {q[1]}")
    print(f"2. {q[2]}")
    print(f"3. {q[3]}")
    print(f"4. {q[4]}")

    answer = int(input("Enter your answer (1-4): "))

    if answer == q[5]:
        money = prizes[i]
        print("✅ Correct Answer!")
        print(f"You won ₹{money}\n")
    else:
        print("❌ Wrong Answer!")
        break

print("\n========== Game Over ==========")
print(f"Your Total Prize Money: ₹{money}")