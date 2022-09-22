score = [35,40,45,50,55,60]
def your_grade(avg_score):
    if avg_score>=80:
        grade='1st'
    elif avg_score>=60:
        grade='2nd'
    else:
        grade= 'Fail'
    return grade
t_subject=len(score)
t_score= sum(score)
av_score=t_score/t_subject
print('তোমার এভারেজ স্কোর: ',av_score)
grad= your_grade(av_score)
print(grad)