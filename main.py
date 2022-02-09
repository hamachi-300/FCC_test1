from arithmetic_arranger import arithmetic_arranger

# print(arithmetic_arranger(['3 + 855', '988 + 40'], False))

problems = []
limit = 0

while True:
	if limit > 4:
		break

	problem = input("Input your problem like [ 3 + 855 ] (limit 5): ")
	limit = limit + 1
	print("Your problems: ", limit, "\n")

	if len(problem) < 1:
		print("Enough?")
		ans = input("Your answer(y/n): ")

		if ans == "y":
			break
		else:
			continue

	problems.append(problem)


display = input("Do you want to show result(y/n): ")
if display == "n":
	showdp = False
else: showdp = True

print(arithmetic_arranger(problems, showdp))