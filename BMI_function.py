def get_data():
    weight = float(input('Enter weight: '))
    height = float(input('Enter height: '))
    user_data = {'weight':weight, 'height':height}
    return user_data

def count_BMI(weight, height):
    BMI = weight/height**2
    print('BMI: %f' %(BMI))
    return BMI

def classific(BMI):
    if 0 < BMI <= 18:
        classification == 'underweight'
    elif 18 < BMI <= 25:
        classification == 'normal weight'
    else:
        classification == 'overweight'
    print(classification)


data = get_data()

count_BMI(data['weight'], data['height'])

classific(BMI)

