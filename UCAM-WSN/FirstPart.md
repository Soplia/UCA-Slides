GTS: Guaranteed Times Slots; CFP: Contention Free Peroid; BI: Beacon Interval; BE: Backoff Experiment; NB: Number of Attemp; SAAM: Stochastic Address Allocate Mechanism; DAAM: Distributed...;OLSR: Operating Link State Link; MRP: Multiple Points Relays

![image-20190307230222718](https://ws2.sinaimg.cn/large/006tKfTcgy1g0uyrlbogqj30pp0aomz8.jpg)

GTS用于传输重要的事情不能给太多，CAP是传输的主力；在sleep阶段发送的数据需要等到下一个CAP进行传输;非信标网络的CSMA-CA算法中，没有使用CW变量,只要检测到信道空闲，就会立即发送数据。CW是一个倒计数值，它被初始化为2。当CCA结果为空闲，就会递减1；而一旦为忙，则会重置该值为初始值2；

![image-20190307232645756](https://ws1.sinaimg.cn/large/006tKfTcgy1g0uzgyxb5rj30q10h7di9.jpg)

SAAM: Each device choose a address randomly when error occur all of them change the address. CM: 能够一个分支; RM: 一个节点能够有几个FFD; LM: 树的深度，从零开始. MPR: 全部覆盖2跳节点而是用的一条节点；

![image-20190308001438217](https://ws2.sinaimg.cn/large/006tKfTcgy1g0v0us8d06j30i208xdiu.jpg)

MS(x) = {nodes which having choosen x as MPR};

OLSR: 1) 计算MS(x) 2) the broadcast of tc is optimized by only using MPR 3) the routing uses MPR only as intermedial node 4) 进行路由，但是路径不止一条。Sleep阶段也会产生数据都在下一个CPA开始发送；BE应该加长一些；为什么CPA一开始有很多东西要发送，在结尾却很少？1）有大量数据需要发送 2）BE有点小

