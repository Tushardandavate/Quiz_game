questions = [
    {
        "prompt": "Which is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
        "answer": "B"
    },
    {
        "prompt": "Who is known as the Father of the Indian Constitution?",
        "options": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. Dr. B. R. Ambedkar", "D. Sardar Patel"],
        "answer": "C"
    },
    {
        "prompt": "Which language is used for web development?",
        "options": ["A. HTML", "B. CSS", "C. JavaScript", "D. All of the above"],
        "answer": "D"
    },
    {
        "prompt": "What is the chemical symbol for Gold?",
        "options": ["A. Ag", "B. Au", "C. Fe", "D. Cu"],
        "answer": "B"
    },
    {
        "prompt": "How many continents are there in the world?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "prompt": "Which is the national animal of India?",
        "options": ["A. Lion", "B. Elephant", "C. Tiger", "D. Leopard"],
        "answer": "C"
    },
    {
        "prompt": "Who developed the Python programming language?",
        "options": ["A. James Gosling", "B. Guido van Rossum", "C. Dennis Ritchie", "D. Bjarne Stroustrup"],
        "answer": "B"
    },
    {
        "prompt": "What is the output of 10 // 3 in Python?",
        "options": ["A. 3.33", "B. 3", "C. 4", "D. 1"],
        "answer": "B"
    },
    {
        "prompt": "Which data structure stores key-value pairs in Python?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    },
    {
        "prompt": "Which protocol is used to access web pages?",
        "options": ["A. FTP", "B. HTTP", "C. SMTP", "D. SSH"],
        "answer": "B"
    }
]

def play_quiz(questions):
    score = 0
    for question in questions:
        print(question['prompt'])
        for option in question["options"]:
            print(option)
        answer = input("Enter your option").upper()

        if answer == question["answer"]:
            print("Hooyaah,Correct Answer")
            score +=1
        else:
            print(f"Wrong Answer, Correct Answer is {question['answer']}")   

    print(f"You got {score} out of {len(questions)} questions correct.")

play_quiz(questions)