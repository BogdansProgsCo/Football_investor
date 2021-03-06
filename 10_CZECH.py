import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2604&chome=0&new_tid=1726'
home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2604&chome=1&new_tid=1726'
away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2604&chome=2&new_tid=1726'

r = requests.get(both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draw = 5
odd_even = 9
under_15 = 6
over_25 = 9
under_25 = 8
both_scores = 7
drw_frst_tm = 7
no_goal_frst_tm = 6

tours_left = 34 - len(full_time)

a = "10_CZECH.txt"

def adding_team(x):
    c = "Czech_Republic"
    b = "Banik_Ostrava"
    f = str(tours_left)
    new_file = open(a, "a+")
    new_file.write('\n ___ ' + c + ' ___')
    new_file.write('\n\n ___ Tours left = ' + f + ' ___')
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()

def clean_file():
    new_file = open(a, 'w+')
    new_file.seek(0)
    new_file.close()

def create_file():
    new_file = open(a, "a+")
    # print(new_file.name)
    new_file.close()

def draws(x):
    count = 0
    for i in x:
        if (i == '0:0 ' or i == '1:1 ' or i == '2:2 '
                or i == '3:3 ' or i == '4:4 ' or i == '5:5 '):
            count += 1
        else:
            break
    if count >= draw:
        print(f'{count} _ ничьи')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n draws = ' + b)
        new_file.close()

def odd(x):
    count = 0
    for i in x:
        if (i != '0:0 ' and i != '1:1 ' and i != '2:2 ' and i != '3:3 ' and i != '4:4 ' and i != '5:5 '
                and i != '2:0 ' and i != '0:2 ' and i != '1:3 ' and i != '3:1 ' and i != '4:2 ' and i != '2:4 '
                and i != '3:5 ' and i != '5:3 ' and i != '4:6 ' and i != '6:4 ' and i != '4:0 ' and i != '0:4 '
                and i != '1:5 ' and i != '5:1 ' and i != '2:6 ' and i != '6:2 ' and i != '3:7 ' and i != '7:3 '
                and i != '0:6 ' and i != '6:0 ' and i != '1:7 ' and i != '7:1 '):
            count += 1
        else:
            break
    if count >= odd_even:
        print(f'{count} _ не-чет')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n odd = ' + b)
        new_file.close()

def even(x):
    count = 0
    for i in x:
        if (i == '0:0 ' or i == '1:1 ' or i == '2:2 ' or i == '3:3 ' or i == '4:4 ' or i == '5:5 '
                or i == '2:0 ' or i == '0:2 ' or i == '1:3 ' or i == '3:1 ' or i == '4:2 ' or i == '2:4 '
                or i == '3:5 ' or i == '5:3 ' or i == '4:6 ' or i == '6:4 ' or i == '4:0 ' or i == '0:4 '
                or i == '1:5 ' or i == '5:1 ' or i == '2:6 ' or i == '6:2 ' or i == '3:7 ' or i == '7:3 '
                or i == '0:6 ' or i == '6:0 ' or i == '1:7 ' or i == '7:1 '):
            count += 1
        else:
            break
    if count >= odd_even:
        print(f'{count} _ чет')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n even = ' + b)
        new_file.close()

def under_1_5(x):
    count = 0
    for i in x:
        if i == '0:0 ' or i == '1:0 ' or i == '0:1 ':
            count += 1
        else:
            break
    if count >= under_15:
        print(f'{count} _ менее 1.5 гола')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n under_1.5 = ' + b)
        new_file.close()

def over_2_5(x):
    count = 0
    for i in x:
        if (i != '0:0 ' and i != '1:1 ' and i != '1:0 '
                and i != '0:1 ' and i != '2:0 ' and i != '0:2 '):
            count += 1
        else:
            break
    if count >= over_25:
        print(f'{count} _ более 2.5 гола')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n over_2.5 = ' + b)
        new_file.close()

def under_2_5(x):
    count = 0
    for i in x:
        if (i == '0:0 ' or i == '1:1 ' or i == '1:0 '
                or i == '0:1 ' or i == '2:0 ' or i == '0:2 '):
            count += 1
        else:
            break
    if count >= under_25:
        print(f'{count} _ менее 2.5 гола')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n under_2.5 = ' + b)
        new_file.close()

def both_score(x):
    count = 0
    for i in x:
        if (i != '0:0 ' and i != '1:0 ' and i != '0:1 ' and i != '2:0 ' and i != '0:2 ' and i != '0:3 ' and i != '3:0 '
                and i != '4:0 ' and i != '0:4 ' and i != '0:5 ' and i != '5:0 ' and i != '0:6 ' and i != '6:0 '):
            count += 1
        else:
            break
    if count >= both_scores:
        print(f'{count} _ обе зибили')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n both_score = ' + b)
        new_file.close()

def both_no_score(x):
    count = 0
    for i in x:
        if (i == '0:0 ' or i == '1:0 ' or i == '0:1 ' or i == '2:0 ' or i == '0:2 ' or i == '0:3 ' or i == '3:0 '
                or i == '4:0 ' or i == '0:4 ' or i == '0:5 ' or i == '5:0 ' or i == '0:6 ' or i == '6:0 '):
            count += 1
        else:
            break
    if count >= both_scores:
        print(f'{count} _ обе -НЕ- зибили')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n both_no_score = ' + b)
        new_file.close()

def draws_first_time(x):
    count = 0
    for i in x:
        if (i == '(0:0)' or i == '(1:1)' or i == '(2:2)'
                or i == '(3:3)' or i == '(4:4)' or i == '(5:5)'):
            count += 1
        else:
            break
    if count >= drw_frst_tm:
        print(f'{count} _ ничьи _ 1-й тайм')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n draws_first_time = ' + b)
        new_file.close()

def no_goal_first_time(x):
    count = 0
    for i in x:
        if i == '(0:0)':
            count += 1
        else:
            break
    if count >= no_goal_frst_tm:
        print(f'{count} _ 0:0 _ 1-й тайм')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n no_goal_first_time = ' + b)
        new_file.close()


clean_file()
create_file()
adding_team(tours_left)
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def draws_home(x):
    count = 0
    for i in x:
        if (i == '0:0 ' or i == '1:1 ' or i == '2:2 '
                or i == '3:3 ' or i == '4:4 ' or i == '5:5 '):
            count += 1
        else:
            break
    if count >= draw:
        print(f'HOME _ {count} _ ничьи ')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n draws_home = ' + b)
        new_file.close()

def odd_home(x):
    count = 0
    for i in x:
        if (i != '0:0 ' and i != '1:1 ' and i != '2:2 ' and i != '3:3 ' and i != '4:4 ' and i != '5:5 '
                and i != '2:0 ' and i != '0:2 ' and i != '1:3 ' and i != '3:1 ' and i != '4:2 ' and i != '2:4 '
                and i != '3:5 ' and i != '5:3 ' and i != '4:6 ' and i != '6:4 ' and i != '4:0 ' and i != '0:4 '
                and i != '1:5 ' and i != '5:1 ' and i != '2:6 ' and i != '6:2 ' and i != '3:7 ' and i != '7:3 '
                and i != '0:6 ' and i != '6:0 ' and i != '1:7 ' and i != '7:1 '):
            count += 1
        else:
            break
    if count >= odd_even:
        print(f'HOME _ {count} _ не-чет')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n odd_home = ' + b)
        new_file.close()

def even_home(x):
    count = 0
    for i in x:
        if (i == '0:0 ' or i == '1:1 ' or i == '2:2 ' or i == '3:3 ' or i == '4:4 ' or i == '5:5 '
                or i == '2:0 ' or i == '0:2 ' or i == '1:3 ' or i == '3:1 ' or i == '4:2 ' or i == '2:4 '
                or i == '3:5 ' or i == '5:3 ' or i == '4:6 ' or i == '6:4 ' or i == '4:0 ' or i == '0:4 '
                or i == '1:5 ' or i == '5:1 ' or i == '2:6 ' or i == '6:2 ' or i == '3:7 ' or i == '7:3 '
                or i == '0:6 ' or i == '6:0 ' or i == '1:7 ' or i == '7:1 '):
            count += 1
        else:
            break
    if count >= odd_even:
        print(f'HOME _ {count} _ чет')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n even_home = ' + b)
        new_file.close()

def under_1_5_home(x):
    count = 0
    for i in x:
        if i == '0:0 ' or i == '1:0 ' or i == '0:1 ':
            count += 1
        else:
            break
    if count >= under_15:
        print(f'HOME _ {count} _ менее 1.5 гола')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n under_1_5_home = ' + b)
        new_file.close()

def over_2_5_home(x):
    count = 0
    for i in x:
        if (i != '0:0 ' and i != '1:1 ' and i != '1:0 '
                and i != '0:1 ' and i != '2:0 ' and i != '0:2 '):
            count += 1
        else:
            break
    if count >= over_25:
        print(f'HOME _ {count} _ более 2.5 гола')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n over_2_5_home = ' + b)
        new_file.close()

def under_2_5_home(x):
    count = 0
    for i in x:
        if (i == '0:0 ' or i == '1:1 ' or i == '1:0 '
                or i == '0:1 ' or i == '2:0 ' or i == '0:2 '):
            count += 1
        else:
            break
    if count >= under_25:
        print(f'HOME _ {count} _ менее 2.5 гола')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n under_2_5_home = ' + b)
        new_file.close()

def both_score_home(x):
    count = 0
    for i in x:
        if (i != '0:0 ' and i != '1:0 ' and i != '0:1 ' and i != '2:0 ' and i != '0:2 ' and i != '0:3 ' and i != '3:0 '
                and i != '4:0 ' and i != '0:4 ' and i != '0:5 ' and i != '5:0 ' and i != '0:6 ' and i != '6:0 '):
            count += 1
        else:
            break
    if count >= both_scores:
        print(f'HOME _ {count} _ обе зибили')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n both_score_home = ' + b)
        new_file.close()

def both_no_score_home(x):
    count = 0
    for i in x:
        if (i == '0:0 ' or i == '1:0 ' or i == '0:1 ' or i == '2:0 ' or i == '0:2 ' or i == '0:3 ' or i == '3:0 '
                or i == '4:0 ' or i == '0:4 ' or i == '0:5 ' or i == '5:0 ' or i == '0:6 ' or i == '6:0 '):
            count += 1
        else:
            break
    if count >= both_scores:
        print(f'HOME _ {count} _ обе -НЕ- зибили')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n both_no_score_home = ' + b)
        new_file.close()

def draws_first_time_home(x):
    count = 0
    for i in x:
        if (i == '(0:0)' or i == '(1:1)' or i == '(2:2)'
                or i == '(3:3)' or i == '(4:4)' or i == '(5:5)'):
            count += 1
        else:
            break
    if count >= drw_frst_tm:
        print(f'HOME _ {count} _ ничьи _ 1-й тайм')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n draws_first_time_home = ' + b)
        new_file.close()

def no_goal_first_time_home(x):
    count = 0
    for i in x:
        if i == '(0:0)':
            count += 1
        else:
            break
    if count >= no_goal_frst_tm:
        print(f'HOME _ {count} _ 0:0 _ 1-й тайм')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n no_goal_first_time_home = ' + b)
        new_file.close()


draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def draws_away(x):
    count = 0
    for i in x:
        if (i == '0:0 ' or i == '1:1 ' or i == '2:2 '
                 or i == '3:3 ' or i == '4:4 ' or i == '5:5 '):
            count += 1
        else:
            break
    if count >= draw:
        print(f'AWAY _ {count} _ ничьи')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n draws_away =  ' + b)
        new_file.close()

def odd_away(x):
    count = 0
    for i in x:
        if (i != '0:0 ' and i != '1:1 ' and i != '2:2 ' and i != '3:3 ' and i != '4:4 ' and i != '5:5 '
                and i != '2:0 ' and i != '0:2 ' and i != '1:3 ' and i != '3:1 ' and i != '4:2 ' and i != '2:4 '
                and i != '3:5 ' and i != '5:3 ' and i != '4:6 ' and i != '6:4 ' and i != '4:0 ' and i != '0:4 '
                and i != '1:5 ' and i != '5:1 ' and i != '2:6 ' and i != '6:2 ' and i != '3:7 ' and i != '7:3 '
                and i != '0:6 ' and i != '6:0 ' and i != '1:7 ' and i != '7:1 '):
            count += 1
        else:
            break
    if count >= odd_even:
        print(f'AWAY _ {count} _ не-чет')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n odd_away =  ' + b)
        new_file.close()

def even_away(x):
    count = 0
    for i in x:
        if (i == '0:0 ' or i == '1:1 ' or i == '2:2 ' or i == '3:3 ' or i == '4:4 ' or i == '5:5 '
                or i == '2:0 ' or i == '0:2 ' or i == '1:3 ' or i == '3:1 ' or i == '4:2 ' or i == '2:4 '
                or i == '3:5 ' or i == '5:3 ' or i == '4:6 ' or i == '6:4 ' or i == '4:0 ' or i == '0:4 '
                or i == '1:5 ' or i == '5:1 ' or i == '2:6 ' or i == '6:2 ' or i == '3:7 ' or i == '7:3 '
                or i == '0:6 ' or i == '6:0 ' or i == '1:7 ' or i == '7:1 '):
            count += 1
        else:
            break
    if count >= odd_even:
        print(f'AWAY _ {count} _ чет')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n even_away = ' + b)
        new_file.close()

def under_1_5_away(x):
    count = 0
    for i in x:
        if i == '0:0 ' or i == '1:0 ' or i == '0:1 ':
            count += 1
        else:
            break
    if count >= under_15:
        print(f'AWAY _ {count} _ менее 1.5 гола')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n under_1_5_away = ' + b)
        new_file.close()

def over_2_5_away(x):
    count = 0
    for i in x:
        if (i != '0:0 ' and i != '1:1 ' and i != '1:0 '
                and i != '0:1 ' and i != '2:0 ' and i != '0:2 '):
            count += 1
        else:
            break
    if count >= over_25:
        print(f'AWAY _ {count} _ более 2.5 гола')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n over_2_5_away =  ' + b)
        new_file.close()

def under_2_5_away(x):
    count = 0
    for i in x:
        if (i == '0:0 ' or i == '1:1 ' or i == '1:0 '
                or i == '0:1 ' or i == '2:0 ' or i == '0:2 '):
            count += 1
        else:
            break
    if count >= under_25:
        print(f'AWAY _ {count} _ менее 2.5 гола')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n under_2_5_away = ' + b)
        new_file.close()

def both_score_away(x):
    count = 0
    for i in x:
        if (i != '0:0 ' and i != '1:0 ' and i != '0:1 ' and i != '2:0 ' and i != '0:2 ' and i != '0:3 ' and i != '3:0 '
                and i != '4:0 ' and i != '0:4 ' and i != '0:5 ' and i != '5:0 ' and i != '0:6 ' and i != '6:0 '):
            count += 1
        else:
            break
    if count >= both_scores:
        print(f'AWAY _ {count} _ обе зибили')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n both_score_away =  ' + b)
        new_file.close()

def both_no_score_away(x):
    count = 0
    for i in x:
        if (i == '0:0 ' or i == '1:0 ' or i == '0:1 ' or i == '2:0 ' or i == '0:2 ' or i == '0:3 ' or i == '3:0 '
                or i == '4:0 ' or i == '0:4 ' or i == '0:5 ' or i == '5:0 ' or i == '0:6 ' or i == '6:0 '):
            count += 1
        else:
            break
    if count >= both_scores:
        print(f'AWAY _ {count} _ обе -НЕ- зибили')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n both_no_score_away =  ' + b)
        new_file.close()

def draws_first_time_away(x):
    count = 0
    for i in x:
        if (i == '(0:0)' or i == '(1:1)' or i == '(2:2)'
                or i == '(3:3)' or i == '(4:4)' or i == '(5:5)'):
            count += 1
        else:
            break
    if count >= drw_frst_tm:
        print(f'AWAY _ {count} _ ничьи _ 1-й тайм')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n draws_first_time_away =  ' + b)
        new_file.close()

def no_goal_first_time_away(x):
    count = 0
    for i in x:
        if i == '(0:0)':
            count += 1
        else:
            break
    if count >= no_goal_frst_tm:
        print(f'AWAY _ {count} _ 0:0 _ 1-й тайм')
        b = str(count)
        new_file = open(a, "a+")
        new_file.write('\n no_goal_first_time_away =  ' + b)
        new_file.close()


draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2620&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2620&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2620&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Bohemians"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2617&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2617&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2617&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Budejovice"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2601&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2601&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2601&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Jablonec"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2652&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2652&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2652&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Karvina"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2613&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2613&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2613&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Mlada_Boleslav"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2646&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2646&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2646&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Opava"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2692&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2692&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2692&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Pardubice"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2611&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2611&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2611&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Pribram"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2603&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2603&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2603&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Sigma_Olomouc"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2605&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2605&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2605&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Slavia_Prague"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2602&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2602&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2602&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Slovacko"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2614&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2614&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2614&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Slovan_Liberec"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2608&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2608&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2608&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Sparta_Prague"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2616&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2616&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2616&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Teplice"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2607&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2607&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2607&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Viktoria_Plzen"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2612&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2612&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2612&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Zbrojovka_Brno"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
"""___________________________________________________________________________________________"""

url_both = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2609&chome=0&new_tid=1726'
url_home = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2609&chome=1&new_tid=1726'
url_away = 'http://allscores.club/soccer/new_ftour.php?champ=1726&f_team=2609&chome=2&new_tid=1726'

r = requests.get(url_both, headers=headers)
with open('main.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
print("_____________________________________")
print(soup.title.text)
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

def adding_team():
    b = "Zlin"
    new_file = open(a, "a+")
    new_file.write('\n\n --------------------------------- ' + b)
    new_file.close()


adding_team()
draws(rev_full_time)
odd(rev_full_time)
even(rev_full_time)
under_1_5(rev_full_time)
over_2_5(rev_full_time)
under_2_5(rev_full_time)
both_score(rev_full_time)
both_no_score(rev_full_time)
draws_first_time(rev_first_half_time)
no_goal_first_time(rev_first_half_time)

r = requests.get(url_home, headers=headers)
with open('home.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_home(rev_full_time)
odd_home(rev_full_time)
even_home(rev_full_time)
under_1_5_home(rev_full_time)
over_2_5_home(rev_full_time)
under_2_5_home(rev_full_time)
both_score_home(rev_full_time)
both_no_score_home(rev_full_time)
draws_first_time_home(rev_first_half_time)
no_goal_first_time_home(rev_first_half_time)

r = requests.get(url_away, headers=headers)
with open('away.html', 'w', encoding='utf-8-sig') as file:
    text = file.write(r.text)

soup = BeautifulSoup(r.text, 'lxml')
allscores = soup.select(".bluelink")

one = ("...".join((str(i) for i in allscores)))
two = re.findall(r'[0-9]{1}[:-][0-9]{1}\s[(-][0-9]{1}[:-][0-9]{1}[\)-]', one)
three = (".".join((str(i) for i in two)))
four = (three.replace('.', ' '))

full_time = re.findall(r'[0-9]{1}[:-][0-9]{1}\s', four)
first_half_time = re.findall(r'[(][0-9]{1}[:][0-9]{1}[)]', four)

rev_full_time = list(reversed(full_time))
rev_first_half_time = list(reversed(first_half_time))

draws_away(rev_full_time)
odd_away(rev_full_time)
even_away(rev_full_time)
under_1_5_away(rev_full_time)
over_2_5_away(rev_full_time)
under_2_5_away(rev_full_time)
both_score_away(rev_full_time)
both_no_score_away(rev_full_time)
draws_first_time_away(rev_first_half_time)
no_goal_first_time_away(rev_first_half_time)
