def display_question(question, options):
    print(question)
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")
    user_answer = input("Enter your answer: ")
    return user_answer
def check_answer(user_answer, correct_answer, score):
    if user_answer.lower() == correct_answer.lower():
        print("Correct!\n")
        return score + 1
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}\n")
        return score
def quiz():
    score = 0
    questions = [
        {
            "question": "What is the capital of Bangladesh?",
            "options": ["London", "Paris", "Dhaka", "Madrid"],
            "correct_answer": "Dhaka"
        },
        {
            "question": "Which city is known as pink city? ''?",
            "options": ["Bhubaneswar", "Kolkata", "Jaipur", "mumbai"],
            "correct_answer": "Jaipur"
        },
        {
            "question": " What is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_answer": "Jupiter"
        },
        {
          "question": " Who was the first woman to win a Nobel Prize?",
          "options": ["Ada Yonath", "Indira Gandhi", "Mother Teresa", "Marie Curie"],
          "correct_answer": "Marie Curie"  
        },
        {
          "question": "What is the capital of India?",
          "options": ["Delhi", "Ankara", "Dhaka", "Marie Paris"],
          "correct_answer": "Delhi"  
        }
    ]
    print("Welcome to the Quiz!\n")
    for q in questions:
        user_answer = display_question(q["question"], q["options"])
        score = check_answer(user_answer, q["correct_answer"], score)
    print(f"Quiz complete! Your final score is {score}/{len(questions)}.")
if __name__ == "__main__":
    quiz()

