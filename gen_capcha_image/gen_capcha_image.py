#! -*-coding:utf-8-*-


from captcha.image import ImageCaptcha
import random

num = [str(x) for x in range(10)]
ALPH = [chr(x) for x in range(65,91)]
alph = [chr(x) for x in range(97,123)]
rand_lists = num + ALPH +alph

#生成随机字符串
def gen_text(size=4,rand_lists=rand_lists):
    text = ''
    for i in range(size):
        text += random.choice(rand_lists)
    return text

#生成随机图片
def gen_image(text):
    image = ImageCaptcha()
    #直接保存
    image.write(text,output = '1.png')


def main():
    text = gen_text()
    gen_image(text)


if __name__ == '__main__':
    main()



