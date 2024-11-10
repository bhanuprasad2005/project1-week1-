# Quiz Game

# Define the quiz questions, options, and correct answers
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Berlin", "B. New delhi", "C. Madrid", "D. Rome"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who is the  first female Prime minister of India?",
        "options": ["A. Indira Gandhi", "B. Sumitra mahajan", "C. kiran bedi", "D. Sushma swaraj"],
        "answer": "A"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Orca"],
        "answer": "B"
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "answer": "C"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Oxygen", "C. Osmium", "D. Iron"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our Solar System?",
        "options": ["A. Earth", "B. Mars", "C. Saturn", "D. Jupiter"],
        "answer": "D"
    },
    {
        "question": "Which is the largest continent in world ?",
        "options": ["A. Africa", "B. Australia", "C. Asia", "D. Europe"],
        "answer": "C"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "answer": "C"
    }
]

# Function to display a question and get user's answer
def ask_question(question_data):
    print("\n" + question_data["question"])
    for option in question_data["options"]:
        print(option)
    answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
    return answer

# Function to check the answer and give feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Incorrect! The correct answer was", correct_answer)
        return False

# Main function to run the quiz
def run_quiz():
    score = 0
    for question in questions:
        user_answer = ask_question(question)
        
        # Validate user input
        while user_answer not in ["A", "B", "C", "D"]:
            print("Invalid input. Please enter A, B, C, or D.")
            user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        
        # Check the answer and update score
        if check_answer(user_answer, question["answer"]):
            score += 1
    
    # Display the final score
    print(f"\nQuiz completed! Your final score is: {score}/{len(questions)}")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
