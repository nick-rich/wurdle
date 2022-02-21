"""
wordle copy
made by nick and eli in an afternoon
mit license and all that 
"""
import random
import termcolor
import argparse

def print_welcome():

	wurdle_pnt = r"""
     __    __    ___  _         __   ___   ___ ___    ___      ______   ___      
    |  T__T  T  /  _]| T       /  ] /   \ |   T   T  /  _]    |      T /   \     
    |  |  |  | /  [_ | |      /  / Y     Y| _   _ | /  [_     |      |Y     Y    
    |  |  |  |Y    _]| l___  /  /  |  O  ||  \_/  |Y    _]    l_j  l_j|  O  |    
    l  `  '  !|   [_ |     T/   \_ |     ||   |   ||   [_       |  |  |     |    
     \      / |     T|     |\     |l     !|   |   ||     T      |  |  l     !    
      \_/\_/  l_____jl_____j \____j \___/ l___j___jl_____j      l__j   \___/     
                 __    __  __ __  ____   ___    _        ___                     
                |  T__T  T|  T  T|    \ |   \  | T      /  _]                    
                |  |  |  ||  |  ||  D  )|    \ | |     /  [_                     
                |  |  |  ||  |  ||    / |  D  Y| l___ Y    _]                    
                l  `  '  !|  :  ||    \ |     ||     T|   [_                     
                 \      / l     ||  .  Y|     ||     ||     T                    
                  \_/\_/   \__,_jl__j\_jl_____jl_____jl_____j      
	"""
	colored_wurdle_pnt = termcolor.colored(wurdle_pnt, 'blue', attrs=['bold'])
	print(colored_wurdle_pnt)

def print_win():

	wurdle_pnt = r"""
	 __ __   ___   __ __      __    __  ____  ____  
	|  T  T /   \ |  T  T    |  T__T  Tl    j|    \ 
	|  |  |Y     Y|  |  |    |  |  |  | |  T |  _  Y
	|  ~  ||  O  ||  |  |    |  |  |  | |  | |  |  |
	l___, ||     ||  :  |    l  `  '  ! |  | |  |  |
	|     !l     !l     |     \      /  j  l |  |  |
	l____/  \___/  \__,_j      \_/\_/  |____jl__j__j
                                                    
	"""
	colored_wurdle_pnt = termcolor.colored(wurdle_pnt, 'green', attrs=['bold'])
	print(colored_wurdle_pnt)

def print_lose():

	wurdle_pnt = r"""
	 __ __   ___   __ __      _       ___    _____   ___ 
	|  T  T /   \ |  T  T    | T     /   \  / ___/  /  _]
	|  |  |Y     Y|  |  |    | |    Y     Y(   \_  /  [_ 
	|  ~  ||  O  ||  |  |    | l___ |  O  | \__  TY    _]
	l___, ||     ||  :  |    |     T|     | /  \ ||   [_ 
	|     !l     !l     |    |     |l     ! \    ||     T
	l____/  \___/  \__,_j    l_____j \___/   \___jl_____j
                                                                                                   
	"""
	colored_wurdle_pnt = termcolor.colored(wurdle_pnt, 'red', attrs=['bold'])
	print(colored_wurdle_pnt)

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

def setup_guesses(n_guesses, len_word):
	empty_word = ''.join(['_']*len_word)
	guess_words = [empty_word]*n_guesses
	guess_outputs = [[0]*len_word]*n_guesses
	lzobj = list(zip(guess_words, guess_outputs))
	guesses = [list(z) for z in lzobj]
	return guesses




def game_loop(len_word,
			 n_guesses, 
			 word_list_path = 'word_list.txt', 
			 target = None):

	

	if target is not None:
		len_word = len(target)
		word_list = get_word_list(pth = word_list_path, len_word = len_word)
		word_list.append(target)
		

	if target is None:
		word_list = get_word_list(pth = word_list_path, len_word = len_word)
		target = pick_word(word_list)

	guesses = setup_guesses(n_guesses, len_word)
	letters = set('abcdefghijklmnopqrstuvwxyz')

	
	print_welcome()
	print_board(guesses)

	num = 0
	while num < n_guesses:	
		termcolor.cprint(f'Please enter guess', 'blue', attrs=['bold'])
		g = input().lower()

		if g == '-q':
			termcolor.cprint(f'Goodbye', 'red', attrs=['bold'])
			return

		if not g.isalpha() or g not in word_list:
			termcolor.cprint(f'Enter a real word stupid', 'red', attrs=['bold'])
			continue

		guesses[num][0] = g
		guesses[num][1] = check_answer(g, target, word_list)

		for c in g:
			letters.discard(c)

		print_board(guesses)
		print_letters(letters, len_word)

		if g == target:
			print_win()
			# termcolor.cprint(f'You Win!', 'blue', attrs=['bold'])
			return

		num += 1

	# termcolor.cprint(f'You Lose!', 'blue', attrs=['bold'])
	print_lose()
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
	parser.add_argument(
		"--target",
		type=str,
		default= None,
		help="target word (optional)",
		)
	args = parser.parse_args()
	game_loop(len_word = args.word_length, 
				n_guesses = args.number_of_guesses,
				word_list_path = args.dictionary,
				target = args.target)









