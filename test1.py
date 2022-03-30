"""
 * Project name(项目名称)：Python_seek函数和tell函数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 13:25
 * Version(版本): 1.0
 * Description(描述)： tell() 函数
 tell() 函数用于判断文件指针当前所处的位置
 """

if __name__ == '__main__':
    file = open("test1.py", "r", encoding="utf-8")
    print(file.name)
    print(file.tell())
    print(file.readline())
    print(file.tell())
    print(file.read(9))
    print(file.tell())
    print(file.read(9))
    print(file.tell())
    print(file.read(9))
    print(file.tell())
    print(file.read(9))
    print(file.tell())
    print(file.read(9))
    print(file.tell())
    print(file.read(9))
    print(file.tell())
    print(file.read(9))
    print(file.tell())
    print(file.read(9))
    print(file.tell())
    print(file.readlines())
    print(file.tell())

    file.close()
