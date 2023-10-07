income = int(input('thu thap cua ban: '))
credit_score = int(input('diem tin dung cua ban: '))
if income >= 50000 and  credit_score >= 700:
    print('You are eligible for a loan with low interest rates')
elif income >= 100000:
    print('You are eligible for a loan with low interest rates')
elif income >= 30000 and credit_score >= 500:
    print('You are eligible for a loan with moderate interest rates')
elif income < 30000 or credit_score < 500:
    print('Sorry, you are not eligible for a loan at this time')