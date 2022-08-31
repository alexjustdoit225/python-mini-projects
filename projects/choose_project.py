from random import choice

project_ideas = ['login system', 'blackjack', 'turtle game', 'expense tracker excel']

greeting = input('Would you like to add a project?\n')
if greeting == '' or greeting == 'no': 
    print('No new projects')
else: 
    project_ideas.append(greeting)
    print(f'New project added: {greeting}')

print('Choice: ', choice(project_ideas))

