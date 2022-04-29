# Write your code here
import random

print("H A N G M A N")

answer_list = ['ada', 'spark', 'arduino', 'bash', 'objective', 'cpp', 'cmake', 'clojure', 'common', 'lisp', 'crystal', 'css', 'less', 'sass', 'dart', 'deno', 'dhall', 'dockerfile', 'elixir', 'erlang', 'elm', 'flow', 'fortran', 'fsharp', 'go', 'godot', 'graphql', 'groovy', 'haskell', 'haxe', 'html', 'javascript', 'java', 'typescript', 'json', 'julia', 'kotlin', 'latex', 'lua', 'markdown', 'nim', 'nix', 'ocaml', 'reasonml', 'perl', 'php', 'purescript', 'python', 'racket', 'robot', 'framework',
			   'rome', 'ruby', 'sorbet', 'steep', 'rust', 'sql', 'scala', 'solidity', 'systemverilog', 'terraform', 'vala', 'vue', 'zig', 'vim', 'erb', 'markdown', 'swift']


def game():
	answer = random.choice(answer_list)
	st = set()  # 已知字母
	life, unknow = 8, len(set(answer))

	while life != 0:
		print()

		# judge win:
		if unknow == 0:
			print(f"You guessed the word {answer}!\nYou survived!")
			break

		# show word:
		for op in answer:
			print(op, end='') if op in st else print('-', end='')
		print()

		# get input:
		c = input("Input a letter: ")

		# check whether is a single:
		if len(c) != 1:
			print("Please, input a single letter.")
		# check whether is a lowercase:
		elif not c.islower():
			print("Please, enter a lowercase letter from the English alphabet.")
		# check whether enter already
		elif c in st:
			print("You've already guessed this letter.")
		# judge
		else:
			st.add(c)
			if c not in answer:
				print("That letter doesn't appear in the word.")
				life -= 1
			else:  unknow -= 1


	else: print("You lost!\n" + f"The word is: {answer}\n")

	return unknow == 0


MENU = 'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:'
user_win, user_lose = 0, 0
while True:
	print(MENU)
	user_enter = input()

	if user_enter == 'play':
		(user_win := user_win + 1) if game() else (user_lose := user_lose + 1)
	elif user_enter == 'results':
		print(f"You won: {user_win} times.\nYou lost: {user_lose} times.")
	elif user_enter == 'exit': break
