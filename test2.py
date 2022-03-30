"""
 * Project name(项目名称)：Python_seek函数和tell函数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 13:29
 * Version(版本): 1.0
 * Description(描述)： seek()函数
 seek() 函数用于将文件指针移动至指定位置
其中，各个参数的含义如下：
file：表示文件对象；
whence：作为可选参数，用于指定文件指针要放置的位置，该参数的参数值有 3 个选择：0 代表文件头（默认值）、1 代表当前位置、2 代表文件尾。
offset：表示相对于 whence 位置文件指针的偏移量，正数表示向后偏移，负数表示向前偏移。例如，当whence == 0 &&offset == 3
（即 seek(3,0) ），表示文件指针移动至距离文件开头处 3 个字符的位置；当whence == 1 &&offset == 5（即 seek(5,1) ），
表示文件指针向后移动，移动至距离当前位置 5 个字符处。
当 offset 值非 0 时，Python 要求文件必须要以二进制格式打开，否则会抛出 io.UnsupportedOperation 错误。
 """

if __name__ == '__main__':
    file = open("test2.py", "rb")
    file.seek(5, 1)
    print(file.tell())
    file.seek(5, 1)
    print(file.tell())
    file.seek(5, 1)
    print(file.tell())
    file.seek(5, 1)
    print(file.tell())
    file.seek(-5, 2)
    print(file.tell())
    file.seek(-9, 2)
    print(file.tell())
    file.seek(-10, 1)
    print(file.tell())
    file.seek(-10, 1)
    print(file.tell())
    file.seek(-10, 1)
    print(file.tell())
    file.seek(-10, 1)
    print(file.tell())
    file.seek(10, 0)
    print(file.tell())
    file.seek(0, 0)
    print(file.tell())
    file.seek(10, 0)
    print(file.tell())
    file.seek(10, 0)
    print(file.tell())
    file.seek(16, 0)
    print(file.tell())
    file.seek(45, 0)
    print(file.tell())
    file.seek(169, 0)
    print(file.tell())
    print(file.readline())
    print(file.readline())
    print(file.tell())
    print(file.readlines())
    print(file.tell())


    file.close()
