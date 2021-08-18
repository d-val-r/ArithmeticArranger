def arithmetic_arranger(problems, *args):
	return_value = ""

	# check if user supplied an argument to display answers
	if (len(args) > 0):
		display_answers = args[0]	
	else:
		display_answers = False

	if (len(problems) > 5):
		return "Error: Too many problems."
	else:

		# will be used to calculate the longest operand 
		# per problem for formatting purposes
		longest_per_equation = []

		# the following lists are used to print values
		top_operands = []
		operators = []
		bottom_operands = []
		totals = []

		for problem in problems:
			
			# split at spaces
			current = problem.split()




			if (current[1] != "+" and current[1] != "-"):
				return "Error: Operator must be '+' or '-'."
			
			try:
				operand_1 = int(current[0])
				operand_2 = int(current[2])
			except: # converting to an int failed
				return "Error: Numbers must only contain digits."

			# if the conversion to ints failed, the function would have
			# returned, never reaching this point
			if (operand_1 > 9999 or operand_2 > 9999):
				return "Error: Numbers cannot be more than four digits."


		
			top_operands.append(operand_1)
			operators.append(current[1])
			bottom_operands.append(operand_2)

			# since the program passed the initial if statement, 
			# the operand is either + or -
			if (current[1] == "+"):
				total = operand_1 + operand_2   
			else:
				total = operand_1 - operand_2

			totals.append(total)


			longest = 0 

			# find the longest operand in the problem and append it
			# to the list
			if (len(current[0]) > longest and len(current[0]) > len(current[2])):
				longest = len(current[0])
			elif (len(current[2]) > longest):
				longest = len(current[2])



			longest_per_equation.append(longest)

			# reset the longest variable
			longest = 0

		# format the first/top operand of each equestion for the return string
		# formatted using the previously-calculated lengths
		for i in range(len(top_operands)):
		    return_value += f"{top_operands[i]:>{2+longest_per_equation[i]}}    "

		
		# Remove the last 4 spaces added by the above loop; this
		# is done to match the exact whitespace requirements in the 
		# project manafest
		return_value = return_value[:len(return_value)-4]
		return_value += "\n"

		for i in range(len(operators)):
		    return_value += f"{operators[i]} {bottom_operands[i]:>{longest_per_equation[i]}}    "


		# Remove the last 4 spaces added by the above loop; this
		# is done to match the exact whitespace requirements in the 
		# project manafest
		return_value = return_value[:len(return_value)-4]
		return_value += "\n"

		for i in range(len(longest_per_equation)):
			return_value += ("-" * (longest_per_equation[i] + 2))
			return_value += "    "


		# Remove the last 4 spaces added by the above loop; this
		# is done to match the exact whitespace requirements in the 
		# project manafest
		return_value = return_value[:len(return_value)-4]
		
		if (display_answers):
			return_value += "\n"
			for i in range(len(totals)):
				return_value += f"{totals[i]:>{2+longest_per_equation[i]}}    "


			# Remove the last 4 spaces added by the above loop; this
			# is done to match the exact whitespace requirements in the 
			# project manafest
			return_value = return_value[:len(return_value)-4]

	return return_value

