regnar_det = input("regnar det?")


if regnar_det == "ja":
    print("ta med paraplyet")


else:
    print("ta med solkräm")


a = 100
b =300
if b > a:
    print ("b är större än a")

else:
    print ("a är större än b")


print ("0")

class Question
    def_init_(self,prompt, answer):
        self.prompt = prompt
        self.prompt = answer

question_prompts = [
    "What is Big Ben?\n(a) A clocktower\n(b)A person"
    "Hur många underverk finns det i världen?\n(a)Fem\n(b)Sju"
    ]
questions = [
    Question(questionprompts[0], "a"
    Question(questionprompts[1], "b")
]

def run_quiz(questions):
    score = 0
    for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
        score += 1
    print ("you got", score, "out of", len(questions))

run_quiz(questions)


