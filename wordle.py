"""
wordle copy
made by nick and eli in an afternoon
mit license and all that 
"""
import random
import termcolor
import argparse

def get_word_list(pth, len_word):
	words = []
	with open(pth, 'r') as wl:
		lines = wl.readlines()
		for line in lines:
			line = line.strip()
			if len(line) == len_word:
				words.append(line)
	return words

def pick_word(words):
	return random.choice(words)

def check_answer(ans, word, words):
	assert ans in words
	output =[0]*len(word)

	for l_ind in range(len(word)):
		if ans[l_ind] in word:
			output[l_ind] += 1

			if ans[l_ind] == word[l_ind]:
				output[l_ind] += 1
	return output


color_pallete = {0:'white', 1: 'yellow', 2: 'green'}
def print_word(word, output, pal = color_pallete):
	char_list = []
	for l_ind in range(len(word)):
		color = pal[output[l_ind]]
		char = word[l_ind]
		colored_char = termcolor.colored(char, color)
		char_list.append(colored_char)

	sep = ' | '
	printline = sep.join(char_list)
	print(printline)

def print_board(guesses):
	for guess, output in guesses:
		print_word(guess, output)

def print_letters(lttrs, len_word):
	spacer = ['____']*len_word
	spacer = "".join(spacer)
	rem_letters = " ".join(sorted(list(lttrs)))
	print(f"{spacer} {rem_letters}")
			
def game_loop(len_word = 5, n_guesses = 6, word_list_path = 'word_list.txt'):

	empty_word = ''.join(['_']*len_word)
	guess_words = [empty_word]*n_guesses
	guess_outputs = [[0]*len_word]*n_guesses
	lzobj = list(zip(guess_words, guess_outputs))
	guesses = [list(z) for z in lzobj]

	letters = set('abcdefghijklmnopqrstuvwxyz')

	word_list = get_word_list(pth = word_list_path, len_word = len_word)
	target = pick_word(word_list)

	termcolor.cprint(f'Welcome to Wurdle', 'blue', attrs=['bold'])
	print_board(guesses)

	num = 0
	while num < n_guesses:	
		termcolor.cprint(f'Please enter guess', 'blue', attrs=['bold'])
		g = input().lower()

		if g == '-q':
			termcolor.cprint(f'Goodbye', 'red', attrs=['bold'])
			return

		if not g.isalpha() or  g not in word_list:
			termcolor.cprint(f'Enter a real word stupid', 'red', attrs=['bold'])
			continue

		guesses[num][0] = g
		guesses[num][1] = check_answer(g, target, word_list)

		for c in g:
			letters.discard(c)

		print_board(guesses)
		print_letters(letters, len_word)

		if g == target:
			termcolor.cprint(f'You Win!', 'blue', attrs=['bold'])
			return

		num += 1

	termcolor.cprint(f'You Lose!', 'blue', attrs=['bold'])
	termcolor.cprint(f'Your word was {target}', 'blue', attrs=['bold'])
	return

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"-ng",
		"--number_of_guesses",
		type=int,
		default= 6,
		help="Number of guesses",
		)
	parser.add_argument(
		"-wl",
		"--word_length",
		type=int,
		default= 5,
		help="Length of Words",
		)
	parser.add_argument(
		"-d",
		"--dictionary",
		type=str,
		default= 'word_list.txt',
		help="path to list of words",
		)
	args = parser.parse_args()
	game_loop(len_word = args.word_length, 
				n_guesses = args.number_of_guesses,
				word_list_path = args.dictionary)









