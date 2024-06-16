#!/bin/python

import sys
import enum

class Instructions(enum.Enum):
	# standard brainfuck for testing
	# INCREMENT_PTR = ">"
	# DECREMENT_PTR = "<"
	# INCREMENT_VALUE = "+"
	# DECREMENT_VALUE = "-"
	# GETCHAR = ","
	# PUTCHAR = "."
	# OPEN_LOOP = "["
	# CLOSE_LOOP = "]"
	# COMMENT = "" # comparing to this will never be true
	# IS_BRAINROT = False

	# brainrot
	INCREMENT_PTR = "SKIBIDI"
	DECREMENT_PTR = "TOILET"
	INCREMENT_VALUE = "SIGMA"
	DECREMENT_VALUE = "BETA"
	GETCHAR = "RIZZ"
	PUTCHAR = "GOON"
	OPEN_LOOP = "SUS"
	CLOSE_LOOP = "AMOGUS"
	COMMENT = "GYATT"
	IS_BRAINROT = True

def syntax_error():
	print("Syntax error.", file=sys.stderr)
	sys.exit(1)

def runtime_error():
	print("Runtime error.", file=sys.stderr)
	sys.exit(1)

if len(sys.argv) != 2:
	print("Enter exactly one argument.", file=sys.stderr)
	sys.exit(1)

file_name = sys.argv[1]
try:
	with open(file_name, "r") as file:
		lines = file.readlines()
except:
	print("Error reading file.")
	sys.exit(1)

instructions = []

for line in lines:
	line = line.strip("\n").replace("\t", "")
	if Instructions.IS_BRAINROT.value:
		for instruction in line.split(" "):
			if instruction == "":
				continue
			if instruction == Instructions.COMMENT.value: # comment
				break
			instructions.append(instruction)
	else:
		for instruction in line:
			instructions.append(instruction)

# check for correct matching of SUS-AMOGUS pairs
check = 0
for instruction in instructions:
	if instruction == Instructions.OPEN_LOOP.value:
		check += 1
	elif instruction == Instructions.CLOSE_LOOP.value:
		check -= 1
	if check < 0:
		syntax_error()
if check != 0:
	syntax_error()

cur_instruction = 0
index = 0
array = [0]
# stack to keep track of the index of the highest level SUS instruction
# AMOGUS will continue execution from its corresponding SUS
loop_stack = []

while cur_instruction < len(instructions):
	instruction = instructions[cur_instruction]
	if instruction == Instructions.INCREMENT_PTR.value: # >
		index += 1
		if index >= len(array):
			array.append(0)
	elif instruction == Instructions.DECREMENT_PTR.value: # <
		if index == 0:
			runtime_error()
		index -= 1
	elif instruction == Instructions.INCREMENT_VALUE.value: # +
		array[index] += 1
	elif instruction == Instructions.DECREMENT_VALUE.value: # -
		array[index] -= 1
	elif instruction == Instructions.GETCHAR.value: # .
		array[index] = ord(sys.stdin.read(1))
	elif instruction == Instructions.PUTCHAR.value: # ,
		sys.stdout.write(chr(array[index]))
		sys.stdout.flush()
	elif instruction == Instructions.OPEN_LOOP.value: # [
		if cur_instruction not in loop_stack:
			loop_stack.append(cur_instruction)
		if array[index] == 0:
			loop_stack.pop()
			level_value = 1
			while level_value != 0:
				cur_instruction += 1
				if instructions[cur_instruction] == Instructions.OPEN_LOOP.value:
					level_value += 1
				elif instructions[cur_instruction] == Instructions.CLOSE_LOOP.value:
					level_value -= 1
	elif instruction == Instructions.CLOSE_LOOP.value: # ]
		cur_instruction = loop_stack[-1]
		continue
	elif Instructions.IS_BRAINROT.value:
		syntax_error()
	# print(loop_stack, array, index, cur_instruction)
	cur_instruction += 1
