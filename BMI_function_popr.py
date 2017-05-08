def get_data():
    weight = float(input('Enter weight: '))
    height = float(input('Enter height: '))
    user_data = {'weight':weight, 'height':height}
    return user_data

def count_BMI(weight, height):
    BMI = weight/height**2
    print('BMI: %f' %(BMI))
    return BMI

def classific(BMI, classification):
    classification = ['underweight', 'normal weight', 'overweight']
    if 0 < BMI <= 18:
        classification = 'underweight'
        #print('underweight')
    elif 18 < BMI <= 25:
        classification = 'normal weight'
        #print('normal weight')
    else:
        classification = 'overweight'
        #print('overweight')
    print(classification)


data = get_data()

BMI = count_BMI(data['weight'], data['height'])

classification = classific(BMI, classification)

