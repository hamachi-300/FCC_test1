# TODO if have argument True show result

def arithmetic_arranger(*problems):

    try:
        rslines = ""
        n1lines = ""
        n2lines = ""
        dashline = ""

        for problem in problems[0]:

            # check error limit 5 problems
            if len(problems[0]) > 5:
                raise SystemError

            pr_split = problem.split()

            num1 = int(pr_split[0])
            num2 = int(pr_split[2])

            lenNum1 = len(str(num1))
            lenNum2 = len(str(num2))

            # check error number > 4 digit
            if lenNum1 > 4:
                raise SyntaxError

            if lenNum2 > 4:
                raise SyntaxError

            width = 2

            if lenNum1 > lenNum2:
                width += lenNum1

                # find num1
                spece1 = width - lenNum1

                fspec1 = ""

                for i in range(spece1):
                    fspec1 += " "

                n1line = fspec1 + str(num1)

                # find num2
                spece2 = width - lenNum2

                fspec2 = ""

                # -1 because sign
                for i in range(spece2-1):
                    fspec2 += " "

                n2line = fspec2 + str(num2)

                # find dash
                dash = ""

                for i in range(width):
                    dash += "-"

                # find result
                if pr_split[1] == "+":
                    result = num1 + num2

                elif pr_split[1] == "-":
                    result = num1 - num2

                else: raise SystemExit

                speceR = width - len(str(result))
                fspeceR = ""

                for i in range(speceR):
                    fspeceR += " "

                rsline = fspeceR + str(result)
            else:
                width += lenNum2

                # find num1
                spece1 = width - lenNum1

                fspec1 = ""

                for i in range(spece1):
                    fspec1 += " "

                n1line = fspec1 + str(num1)

                # find num2
                spece2 = width - lenNum2

                fspec2 = ""

                # -1 because sign
                for i in range(spece2-1):
                    fspec2 += " "

                n2line = fspec2 + str(num2)

                dash = ""

                for i in range(width):
                    dash += "-"

                # find result
                if pr_split[1] == "+":
                    result = num1 + num2

                elif pr_split[1] == "-":
                    result = num1 - num2

                else: raise SystemExit

                speceR = width - len(str(result))
                fspeceR = ""

                for i in range(speceR):
                    fspeceR += " "

                rsline = fspeceR + str(result)

            n1lines += n1line + "    "
            n2lines += pr_split[1] + n2line + "    "
            dashline += dash + "    "
            rslines += rsline + "    "

        outcomeT = n1lines + "\n" + n2lines + "\n" + dashline + "\n" + rslines
        outcome = n1lines + "\n" + n2lines + "\n" + dashline

        if problems[1]:
            return outcomeT

        else:
            return outcome

    except SyntaxError:
        return "Error: Numbers cannot be more than four digits."

    except SystemError:
        return "Error: Too many problems."

    except SystemExit:
        return "Error: Operator must be '+' or '-'."

    except:
        return "Error: Numbers must only contain digits."