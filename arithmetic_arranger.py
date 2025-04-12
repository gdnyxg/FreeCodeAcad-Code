def check_all_nums(nums:list):
    """Checking all characters in list are numbers"""
    all_nums = ''.join(nums)
    check = all_nums.isdigit()
    return check

def arithmetic_arranger(problems:list, show_answers=False):
    
    """Function that receives a list of strings which are  
    arithmetic problems, and returns the problems arranged 
    vertically and side-by-side. When the second argument is set 
    to True, the answers are displayed."""

    format_probs = []
    if len(problems)>5:
        return 'Error: Too many problems.'

    answers = []
    str1 = []
    str2 = []
    str3 = []
    str4 = []

    for problem in problems:
        
        #seperating numbers out of calculation
        split_prob_plus = problem.split('+')
        split_prob_minus = problem.split('-')
        #checking if add or subtract
        if len(split_prob_plus) == 2:
            split_prob = split_prob_plus
            plus = True  # corresponds to addition
        elif len(split_prob_minus) == 2:
            split_prob = split_prob_minus
            plus = False
        else:
            #raising error for anything other than add and subtract
            return "Error: Operator must be '+' or '-'."
        
        #removing spaces
        split_prob = [x.strip(' ') for x in split_prob]
        #checking all characters in calc are digits
        if not check_all_nums(split_prob):
            return 'Error: Numbers must only contain digits.'
    
        int_split_prob = [int(x) for x in split_prob]
        for num in int_split_prob:
            if num > 9999:
                return'Error: Numbers cannot be more than four digits.'

        #calculating answers
        if plus: 
            calcul = int_split_prob[0]+int_split_prob[1]
            answers.append(calcul)
        else:
            calcul = int_split_prob[0]-int_split_prob[1]
            answers.append(calcul)
        #formatting to arithmetic setup 
        max_len = len(str(abs(max(int_split_prob))))+2
        for num in split_prob:
            gap = max_len - len(num)
            if split_prob.index(num) == 0:
                str1.append((gap*' ')+num)
            else:
                if plus:
                    str2.append('+'+(' '*(gap-1))+num)
                else:
                    str2.append('-'+(' '*(gap-1))+num)
            
        str3.append('-'*max_len)

        
        answer_string = str(calcul)
        answer_gap = max_len - len(answer_string)
        str4.append((' '*answer_gap)+answer_string)

    line1 = "    ".join(str1)
    line2 = "    ".join(str2)
    line3 = "    ".join(str3)
    line4 = "    ".join(str4)

    formatted = line1+'\n'+line2+'\n'+line3
    if show_answers:
        formatted += '\n'+line4

    return formatted

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
