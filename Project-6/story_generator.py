
from random import choice

url = 'https://github.com/anjaliaks'

def story_gen():
    who = ['Anjali', 'Asha', 'Ketan', 'Divya', 'Ishika', 'Ritika']
    what = ['was eating a cockroach', 'dancing in saree', 'beaten by his/her father', 'making tik-tok']
    when = ['last night', 'yesterday', 'a few days ago', 'just then']
    action = ['and has no regrets.', 'but instantly regretted it.', 'and starts laughing.', 'and post the video in insta.']
    return print('\033[94m' + choice(who) + ' ' + choice(what) + ' ' + choice(when) + ' ' + choice(action) + '\033[0m')

def print_story():
    print('-------------------------------------------------------------------------------')
    story_gen()
    print(
        '-------------------------------------------------------------------------------\n''Thanks for trying: Story Generator\n''Click the link to check out more of my projects:\n',
        url)
    print('*****------------------------------------------*****')

if __name__ == '__main__':
    print_story()
