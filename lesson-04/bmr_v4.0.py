"""
    功能：BMR计算器
    版本：v4.0
    日期：2018/8/21
"""


def main():

    y_or_n = 'n'
    while y_or_n != 'y':

        print("请入一下信息，用空格分割")
        input_str = input('性别 体重(kg) 身高(cm) 年龄：')
        input_arr = input_str.split(' ')
        # 性别
        gender = input_arr[0]

        # 体重（kg）
        weight_str = input_arr[1]

        # 身高(cm)
        height_str = input_arr[2]

        # 年龄
        age_str = input_arr[3]
        try:
            weight = float(weight_str)
            height = float(height_str)
            age = int(age_str)
            if (gender == '男'):
                # 男性
                bmr = 13.7 * weight + 5.0 * \
                    height - 6.8 * age + 66
            elif (gender == '女'):
                # 女性
                bmr = 9.6 * weight + 1.8 * \
                    height - 4.7 * age + 655
            else:
                bmr = -1

            if(bmr != -1):
                print('性别：{}，体重：{}公斤，身高：{}厘米，年龄：{}岁:'.format(
                    gender, weight_str, height_str, age_str))
                print('基础代谢率：{}大卡'.format(bmr))
            else:
                print('不支持')
        except ValueError:
            print('转换数值出错！')
        except IndexError:
            print('输入的信息过少！')
        except:
            print('未知错误！')

        y_or_n = input('是否退出程序(y/n)?')


if __name__ == '__main__':
    main()
