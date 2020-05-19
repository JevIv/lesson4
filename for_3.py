
list_of_classes= [
                  {'school_class': '4a', 'scores': [3,5,5,5,5,5,5,4,5,5,5,4]},
                  {'school_class': '4b', 'scores': [5,3,5,5,2,3,3,3,5,3,4,3]},
                  {'school_class': '4c', 'scores': [3,5,4,3,2,5,3,2,3,4,2,2]},
                  {'school_class': '4d', 'scores': [2,3,2,3,3,4,5,2,3,4,3,3]},
                  {'school_class': '5a', 'scores': [5,3,3,4,3,5,5,5,3,4,3,5]},
                  {'school_class': '5b', 'scores': [5,3,5,5,3,4,3,4,3,4,3,3]},
                  {'school_class': '5c', 'scores': [4,3,3,4,3,4,5,4,3,4,3,5]},
                  {'school_class': '5d', 'scores': [2,3,5,4,3,5,5,3,3,4,3,3]},
]
avg_school_scores=[]    #список средних оценок по школе
total_sum=0             #сумма средних оценок по школе

for items in list_of_classes:
    sum = 0             #сумма средних оценок по каждому классу
    avg = 0             #средняя оценка по каждому классу
    class_numb = items.get('school_class')

    for item in items.get('scores'):
        sum += item
        avg = sum / len(items.get('scores'))

    avg_school_scores.append(avg)
    print(f"The average score of {class_numb} class is {'%.2f' % avg}")


for i in avg_school_scores:
    total_sum += i


total_avg=total_sum/len(list_of_classes) #средняя оценка по школе

print(f"\nThe average score of the school is {'%.2f' % total_avg}")
