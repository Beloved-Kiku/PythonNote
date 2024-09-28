user_input = list(map(str, input('>>>身高(cm/m)体重(kg),年龄,性别,姓名:').strip().split()))
PersonMessage = {"name": '', "age": "", "height": '', "sex": '', "heavy": ''}
def FilterData(user_input):
    # 判断用户输入的是m 还是cm 如果是cm 则将cm转化为m 并且去掉单位
    if user_input[0].endswith("cm"):
        # 将cm转化为m并且去掉单位
        Height = (int(user_input[0].rstrip('cm')))
        PersonMessage['height'] = Height / 100
    elif user_input[0].endswith("m"):
        Height = user_input[0].rstrip('m')
        # 使用float保存输入的m
    PersonMessage['height'] = float(Height)
    PersonMessage['heavy'] = int(user_input[1])
    PersonMessage['age'] = int(user_input[2])
    for k in user_input:
        if k.isalpha():
            PersonMessage['name'] = k
        if k == '1':
            PersonMessage['sex'] = '男'
            PersonMessage['id'] = 1
        if k == '0':
            PersonMessage['sex'] = '女'
            PersonMessage['id'] = 0
    return PersonMessage
# BMI =身高(m) /体重(kg)
# body_fat =(1.2*BMI+0.23*age-5.4-10.8*sex)/100
def ComputedBMI(user_input):
    data = FilterData(user_input)
    BMI = data['heavy'] / (data['height'] * data['height'])
    BodyFat = (1.2 * BMI + 0.23 * data['age'] - 5.4 - 10.8 * data['id']) / 100
    Girl = (0.25, 0.28);
    Boy = (0.15, 0.18)
    # 判断男女对应是否为正常
    if 0.25 < BodyFat < 0.28 and data['id'] == 0: print(f"你的体脂率是:{BodyFat},属于正常体脂")
    if 0.15 < BodyFat < 0.18 and data['id'] == 1: print(f"你的体脂率是:{BodyFat},属于正常体脂")
    if data['id'] == 0:
        if BodyFat < Girl[0]: print(f'这是你的体脂率有点过瘦:{BodyFat}')
        if BodyFat > Girl[1]: print(f'这是你的体脂率有点过胖:{BodyFat}')
    if data['id'] == 1:
        if BodyFat > Boy[1]: print(f'这是你的体脂率有点过胖:{BodyFat}')
        if BodyFat < Boy[0]: print(f'这是你的体脂率有点过瘦:{BodyFat}')
ComputedBMI(user_input)
