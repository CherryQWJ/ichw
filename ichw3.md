# ichw
**1.	详述通用的高速缓存存储器结构及工作原理**

高速缓存存储器Cache,是一种放置在CPU和主存储器之间的存取速度快而规模较小的存储器，可以增加存储器的传输效率和处理机的效能。
一些数据和指令事先由主存储器调入Cache中。当CPU开始处理数据时，先访问Cache，若有数据，则命中，CPU存取Cache即可，不用去访问运行速度较慢的主存储器。若无数据，则CPU到主存储器中复制需要的数据块，覆盖Cache的内容，完成后CPU存取Cache。
