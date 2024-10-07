#在python中为我们提供了buffer缓冲区域,可以避免我们频繁操作io,从而提高性能
#buffer缓冲区域,在内存中开辟一个区域,将数据先写入到缓冲区中,然后一次性写入到硬盘上
#buff缓冲区是位于内存中的一片区域,一般来说是一个FIFO队列,当缓冲区满了或者达到设定阈值后数据才会被flush到磁盘
#我们可以通过io.DEFAULT_BUFFER_SIZE来查看默认的缓冲区大小
import io
print(io.DEFAULT_BUFFER_SIZE) #一般来说缺省值都是4k或者8k。4096 or 8192
#当我们在打开文件之后使用close()函数后 python会帮我们调用flush()将数据写入磁盘
#buffering =-1 表示使用io.DEFAULT_BUFFER_SIZE作为buffer缓冲区域大小
#buffering =0 只能在二进制模式下使用表示关闭buffer缓冲,直接写入磁盘
#buffering =1 只能在文本模式下使用表示遇到换行符就执行flush()
#buffering>1  只能在二进制模式下使用表示自定义buffer缓冲区域字节大小
file = open('test.txt','a',buffering=io.DEFAULT_BUFFER_SIZE)
file.write('hello world')