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

score = 0
for question in questions:
    split_question = question.split('=')
    print(f'{split_question[0]}=')
    answer = input("")
    if answer == split_question[1]:
        score = score + 1

results = open('results.txt', 'w')
results.write(f'Your final score is {score / len(questions)}.')
results.close()
