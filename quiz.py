"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:

questions_txt = open('questions.txt', 'r')
questions = [line.strip() for line in questions_txt.readlines()]
questions_txt.close()

print(questions)

score = 0
for question in questions:
    split_question = question.split('=')
    answer = input(f'{split_question[0]}=')
    if answer == split_question[1]:
        score = score + 1

results = open('results.txt', 'w')
results.write(f'Your final score is {score / len(questions)}.')
results.close()
print(len(questions))

# ------------------------------------------------------------------

# read from questions.txt and append each line into a list
questions = open("questions.txt", "r")  # read from questions.txt

# read all lines and get rid of line break for each line, then append each stripped line to a list
question_list = [line.strip() for line in questions]
questions.close()

score = 0  # initialize score
total = len(question_list)  # set total score

for line in question_list:
    # split equation with `=` into question and answer
    q, a = line.split("=")

    # print question and wait for user to input their answer
    ans = input(f"{q}=")

    if a == ans:  # if user input matches answer
        score += 1  # increase score

result = open("result.txt", "w")  # open result.txt
# write final score to result.txt
result.write(f"Your final score is {score}/{total}.")
result.close()
