def arithmetic_arranger(expression: list[str], result: bool = False) -> str:
    if len(expression) > 7:
        raise Exception("Error: Too Many Problems")

    data = []
    
    for exp in expression:
        exp = exp.replace(" ", "")
        if "+" in exp:
            exp = exp.split("+")
            operator = "+"
        elif "-" in exp:
            exp = exp.split("-")
            operator = "-"
        else:
            raise Exception("Error: Operator must be '+' or '-'")

        if (not exp[0].isdigit()) or (not exp[1].isdigit()):
            raise Exception("Error: Numbers must only contain digits")
        if len(exp[0]) > 6 or len(exp[1])> 6:
            raise Exception("Error Numbers cannot be more than six digits")
        
        exp_data = {"operand1":exp[0], "operator":operator, "operand2":exp[1]}
        if result:
            res = str(eval(exp[0] + operator + exp[1]))
            exp_data["result"] = res
        else:
            res  = ""
        
        exp_data["align"] = max([len(exp[0]), len(exp[1]), len(res)])
        data.append(exp_data)
    
    """line1 = ["  " + exp_data["operand1"].rjust(exp_data["align"]) for exp_data in data]
    line1 = "    ".join(line1)

    line2 = [exp_data["operator"] + " " + exp_data["operand2"].rjust(exp_data["align"]) for exp_data in data]
    line2 = "    ".join(line2)

    line3 = [ "-" * (exp_data["align"] + 2) for exp_data in data]
    line3 = "    ".join(line3)

    returnStr = "\n".join([line1, line2, line3])
    if result:
        line4 = ["  " + exp_data["result"].rjust(exp_data["align"]) for exp_data in data]
        line4 = "    ".join(line4)
        returnStr += "\n" + line4
    return returnStr"""

    """ li1 = []
    li2 = []
    li3 = []
    li4 = []
    for exp_data in data:
        li1.append("  " + exp_data["operand1"].rjust(exp_data["align"]))
        li2.append(exp_data["operator"] + " " + exp_data["operand2"].rjust(exp_data["align"]))
        li3.append( "-" * (exp_data["align"] + 2))
        li4.append("  " + exp_data.get("result").rjust(exp_data["align"]))
    line1 = "    ".join(li1)
    line2 = "    ".join(li2)
    line3 = "    ".join(li3)

    return_string = "\n".join([line1, line2, line3])

    if result:
        line4 = "    ".join(li4)
        return_string += "\n" + line4

    return return_string"""
    
    