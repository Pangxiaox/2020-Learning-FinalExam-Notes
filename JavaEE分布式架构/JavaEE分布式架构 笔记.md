# JavaEE分布式架构 笔记

### 第一节课

### 1. 企业级应用架构

**定义**

需要存储、管理、展现、操作大量的复杂数据，使用数据来支持或自动化企业的业务活动。

如：工资发放管理、电子病历、物流跟踪、信用评分等

**企业级应用特点**

- 大量复杂数据，经常变动，需要永久保存（持久化）
- 对持久数据的并发访问
- 复杂的用户界面
- 需要与其他系统集成
- 复杂的业务逻辑，及针对特定客户在特定情况下的非逻辑的业务规则

**企业环境**

企业级应用的本性约束了我们的架构选择：

- 绝大多数企业需要许多小应用以及少数几个大应用
- 系统需要集成，架构需要整合
- 由于应用之间的相似性，产生了许多强大的设计模式
- 由于应用之间的业务、规则等差异性，应用设计模的时候需要很仔细地定制化

**企业级应用几个重要的质量属性**

- 适应快速变化的市场（Extensibility、Scalability）
- 降低风险（Controllability）
- 让客户满意（Reliability、Efficiency）
- 给大家信心保障（Security）
- Min costs and Max gains

**应对挑战**

- 采用一个灵活的基础
- 采用开放的、可扩展的客户界面
- 充分利用现有的系统和数据
- 采用基于组件的方案

**企业级应用架构**

架构定义了系统是如何构成的以及系统组件是如何交互的

优秀的架构是通过良好定义的层来构成的，每个层都封装了良好定义且可控的服务，代表了一个清晰的、一致的抽象

架构包含了一组标准、策略和工具，使得构建和运行符合业务需要的系统更加高效和经济

**企业级应用系统分层**

- 高层依赖于底层提供服务、底层不需要依赖高层

- 3层架构：

  展现层：处理用户和系统之间的交互，HTML界面或富客户端GUI

  领域层（业务逻辑层）：分配任务、进行验证、各种计算，通常不包含数据源

  数据源层：与其它系统交互、获取和发送数据，通常包含一个DBMS，存储持久数据

通常在大型应用中，每层都是一个软件包

**使用应用框架的好处**

- 定义了构建组件的指导思想
- 定义了所有的组件如何装配到一起
- 保证了代码的一致性
- 让开发人员可专注于业务逻辑
- 降低了开发时间

### 2. Java EE模型

**Java EE模型**

定义了一种实现分布式、多层应用系统的架构。模型将系统开发工作划分为2

部分：业务逻辑和展现逻辑由应用开发人员实现、标准的系统级服务由Java EE平台提供

**Java EE组件**

- 运行在客户端的组件：应用程序客户端和applets
- 运行在服务器的web组件：Java Servlet、Java Server Faces（JSF）、Java Server Pages（JSP）
- 运行在服务器的业务组件：Enterprise JavaBeans（EJB)

**Java EE客户端**

- Web客户端：包含各种标记语言（HTML\XML)的动态网页，一个web浏览器渲染从服务器收到的页面内容
- 应用程序客户端：基于命令行窗口的应用，基于AWT，Swing或其他富客户端技术的GUI应用

**Web组件**

Java Servlet、Java Server Pages、Java Server Face、标记库Tag libraries

**业务组件**

Java Persistence Entities、Session Beans、Message-Driven Beans

**Java EE容器**

- Java EE服务器：以包含各种组件的容器的形式提供底层系统级服务

- web组件，enterprise bean和应用程序客户端必须先打包成一个Java EE模块并部署到相应容器里才能运行

- 容器负责管理资源和安全性、事务管理、并发、消息处理、电子邮件、Java Naming and Directory Interface（JNDI）查找、远程来凝结、数据库连接池、数据持久性、组件生命周期管理等服务。这些服务有一系列JSR（Java Specification Requests):EJB、RMI、JNDI、JDBC、JPA、JSP等来规范

**容器类型**

- Java EE服务器：Java EE平台的运行时。Java EE服务器包括了EJB容器和web容器
- Enterprise JavaBeans（EJB)容器：管理Java EE应用中的enterprise beans的运行
- Web容器：管理Java EE应用中的web页面，servlets等组件的运行

**打包Java EE应用**

Java EE应用可以打包成一个或多个标准单元，部署到Java EE platform-compliant系统。每个单元包含了功能组件（如enterprise bean，web页面，servlet，or applet）和可选的部署描述文档（dd）

**Java EE开发中的各种角色**

- Java EE产品供应商（IBM\JBoss\Sun等）
- 开发工具供应商（JBuilder\Eclipse等）
- 应用组件开发人员：Enterprise Bean开发人员、Web组件开发人员、应用程序客户端开发人员
- 应用程序集成人员
- 应用程序部署和系统管理人员

**Java EE应用开发环境**

- 选择Java EE服务器/Web服务器
- 选择IDE
- 选择DB

⭐本课程使用MySQL+Tomcat+Eclipse/IDEA



### 第二节课

### 1. Web Applications

Web应用就是运行在Web服务器或者应用服务器上的程序

浏览器提交HTTP请求来调用这些服务程序，参数封装在HTTP request里；服务器通过HTTP response将结果返回浏览器

**Web Technologies**

- Servlets 是一些特殊的Java 类，动态地处理请求并构造响应。Servlets 适合用于面向服务的应用（事实上， web service 的一种实现就是使用Servlets ）以及在面向表现层的应用中作为控制函数来使用。
- Java Server Faces 和 Java Server Pages 则更适合于生成页面文件（基于文本的标记文件）。

**Web Container**

- Web 组件是由称为Web容器的一组平台运行期服务程序来提供支持和管理的。 Web容器提供了请求分派、安全管理、并发管理、组件生命周期管理等服务。
- 当Web应用部署到Web容器的时候，其行为的某些方面可以通过一个Web应用部署描述文件来配置。

**Web Modules**

- Java EE的 Web 模块对应于一个 Web应用，是Web资源的最小可部署并使用的单位。
- Web 模块有特定的结构。

### 2. JSP（Java Server Pages）

JSP容许我们轻松创建既包含静态内容又包含动态内容的web页面

**主要特点**

- JSP页面是基于文本的文档，描述了如何处理请求并创建响应
- JSP技术包含了表达式语言，可以很方便快捷地访问服务端对象
- JSP技术提供了一种扩展JSP语言的机制

**JSP Page**

JSP页面是一个文本文件，包含了2种文本：

- 静态数据：可用任何的基于文本的格式来表达，如HTML、SVG、WML和XML等
- JSP元素：必须由servlet引擎解析从而创建出动态内容

**JSP Elements**

- 指令元素，或指令标签、指令标记
- 动作元素，或动作标签、动作标记
- 脚本元素：申明、脚本语句、表达式

**Directives**

```xml
<%@ directive {attr=“value”}* %>
```

JSP标准规定了3种指令：page、include、taglib

**Action Elements**

JSP内建的动作标签：forward、getProperty、include、plugin、setProperty、useBean、param、params

**Scripting in JSP Pages**

脚本元素通常用于创建并访问对象、定义方法、管理控制流程等

**JSP对象的作用范围**

- 在单个JSP页面里定义且仅能被该页面里的对象访问的对象属于page范围，相当于局部变量，很少使用。
- 客户端与服务器的一次”请求响应”对应于request范围，定义在request范围里的对象可被本次”请求响应”所关联的所有组件（include,forward,filter,chain）访问，通过内置变量request的setter/getter方法定义并访问，经常使用。
- 客户端与服务器的一次”完整的交互过程”称为一个session（会话），通常当某个用户登录或初次链接时由后台自动生成，当用户登出或超时后自动结束。定义在session范围里的对象可被本次”会话”里的所有组件访问，通过session的setter/getter方法定义并访问，经常使用。
- 为web应用所有组件共享的对象称为application或context对象。通过内置变量application的setter/getter方法定义并访问，较常使用。

**JavaBeans Components**

JavaBeans组件易于复用、很容易组合到应用中的Java类。任意Java类只要符合一定的设计约定就是一个JavaBeans组件。

JSP使用内建的动作标签直接支持JavaBeans 组件的创建和使用。你可以很容易地创建、初始化JavaBeans 组件并进行存取操作。

🔺使用JavaBeans好处：简单对象的封装、JSP页面语法更简洁，消除了脚本小程序

### 3. Servlet（小服务程序）

Servlet是满足一定规范的Java类，用于处理请求并创建响应

**Servlet Life Cycle**

当某个请求对应到一个servlet时，容器进行以下操作：

1. 如果该servlet的实例不存在，则容器：加载servlet类、创建servlet类的一个实例、调用init方法对该实例进行初始化。
2. 调用service方法，传递请求和响应对象
3. 如果容器需要移除servlet，调用其destroy方法

**Sharing Information**

- Web上下文对象：被整个应用共享
- Session对象：被整个会话共享
- Request对象：被同一个请求里的组件共享
- Page对象：被同一个页面里的组件共享

**Filter过滤器**

主要对请求或者响应的头信息或内容进行转换。过滤器通常不会自己产生响应而是在其他web组件上附加一些功能。

作用：验证users并过滤非法请求、记录请求、对请求字符串进行编码、修改请求内容、URL Rewrite实现网站的伪静态

**Listener监听器**

### 4. EL（表达式语言）

简化的数据访问方式，可访问JSP隐含对象和Java Bean组件

语法：`${expr}`

主要用于：

- 标记中的属性值：`<jsp:include page="${page}"/>`
- 静态文本：`<h1>Welcome,${name}</h1>`

### 5. JSTL（JSP标准标签库）

- `<c:out>`用于输出表达式的值
- `<c:set>`用于设置的值
- `<c:remove>`用于清除变量
- `<c:if>`
- 多选互斥分支：`<c:choose>`、`<c:when>`、`<c:otherwise>`
- `<c:forEach>`用于迭代一个集合或者迭代指定次数
- `<c:forTokens>`字符串token处理
- `<c:import>`
- `<c:url>`用于产生一个url
- `<c:redirect>`



### 第三节课

### 1. 技术讲解（工具篇）

Maven、IDEA、MySQL、Git、Navicat、Docker、Postman、XMind、Typora、Google Browser、Notepad++、Sublime Text、Junit等工具和相关技术的讲解



### 第四节课

### 1. 框架Hibernate

**使用框架的好处**

从软件复用的角度来说：合理使用框架，合理的分层。很多项目中都可以完完全全再用上，既能够提高效率，也能够降低引入的风险。

**ORM框架**

对象——关系映射（Object-Relational Mapping，ORM）：

对象和关系数据是业务实体的两种表现形式，业务实体在内存中表现为对象，在数据库中表现为关系数据。内存中的对象之间存在关联和继承关系，而在数据库中，关系数据无法直接表达多对多关联和继承关系。因此，对象-关系映射(ORM)系统一般以中间件的形式存在，主要实现程序对象到关系数据库数据的映射。

ORM框架包含对持久类对象进行CRUD操作的API，通过这种封装避免了不规范、冗余、风格不统一的SQL语句，可以避免很多人为Bug，方便编码风格的统一和后期维护。

🔺优缺点分析

优点：①提高开发效率，降低开发成本 ②使开发更加对象化 ③可移植 ④可以很方便地引入数据缓存之类的附加功能

缺点： ①自动化进行关系数据库的映射需要消耗系统性能。其实这里的性能消耗还好啦，一般来说都可以忽略之。 ②在处理多表联查、where条件复杂之类的查询时，ORM的语法会变得复杂。

🔺常用ORM框架

Java系列：Hibernate、iBatis、Mybatis、Spring DATA JPA

.Net系列：NHibernate、iBATIS.NET

**Hibernate 简介**

Hibernate是一个开放源代码的对象关系映射框架，它对JDBC进行了非常轻量级的对象封装，它将POJO与数据库表建立映射关系，是一个全自动的orm框架，hibernate可以自动生成SQL语句，自动执行，使得Java程序员可以随心所欲的使用对象编程思维来操纵数据库。

**Hibernate核心API**

Hibernate的API一共有6个，分别为:Session、SessionFactory、Transaction、Query、Criteria和Configuration。通过这些接口，可以对持久化对象进行存取、事务控制

**Session**

Session接口负责执行被持久化对象的CRUD操作(CRUD的任务是完成与数据库的交流，包含了很多常见的SQL语句)。但需要注意的是Session对象是非线程安全的。同时，Hibernate的session不同于JSP应用中的HttpSession。这里当使用session这个术语时，其实指的是Hibernate中的session，而以后会将HttpSession对象称为用户session。

**SessionFactory**

SessionFactory接口负责初始化Hibernate。它充当数据存储源的代理，并负责创建Session对象。这里用到了工厂模式。需要注意的是SessionFactory并不是轻量级的，因为一般情况下，一个项目通常只需要一个SessionFactory就够，当需要操作多个数据库时，可以为每个数据库指定一个SessionFactory。

**Transaction**

Transaction 接口是对实际事务实现的一个抽象，能够让开发者能够使用一个统一事务的操作界面，使得自己的项目可以在不同的环境和容器之间方便地移植。

**Query**

Query接口让你方便地对数据库及持久对象进行查询，它可以有两种表达方式：HQL语言或本地数据库的SQL语句。Query经常被用来绑定查询参数、限制查询记录数量，并最终执行查询操作。

**Criteria**

Criteria接口与Query接口非常类似，允许创建并执行面向对象的标准化查询。值得注意的是Criteria接口也是轻量级的，它不能在Session之外使用。

**Configuration**

Configuration 类的作用是对Hibernate 进行配置，以及对它进行启动。在Hibernate 的启动过程中，Configuration 类的实例首先定位映射文档的位置，读取这些配置，然后创建一个SessionFactory对象。虽然Configuration 类在整个Hibernate 项目中只扮演着一个很小的角色，但它是启动hibernate 时所遇到的第一个对象。

**Hibernate基本步骤**

1. 获取SessionFactory 

2. 通过SessionFactory 获取一个Session

3. 在Session基础上开启一个事务

4. 通过调用Session的save方法把对象保存到数据库

5. 提交事务

6. 关闭Session
7. 关闭SessionFactory

**Hibernate对象的三种状态**

瞬时、持久和脱管

瞬时：指的是没有和hibernate发生任何关系，在数据库中也没有对应的记录，一旦JVM结束，这个对象也就消失了 
持久：指的是一个对象和hibernate发生联系，有对应的session,并且在数据库中有对应的一条记录 
脱管：指的是一个对象虽然在数据库中有对应的一条记录，但是它所对应的session已经关闭了

**Hibernate 缓存**

hibernate默认是开启一级缓存的，一级缓存存放在session上,二级缓存是在SessionFactory上

**Hibernate数据库连接池**

建立数据库连接时比较消耗时间的，所以通常都会采用数据库连接池的技术来建立多条数据库连接，并且在将来持续使用，从而节约掉建立数据库连接的时间 
hibernate本身是提供了数据库连接池的，但是hibernate官网也不推荐使用他自带的数据库连接池。 一般都会使用第三方的数据库连接池 ，C3P0是免费的第三方的数据库连接池，并且有不错的表现。Hibernate使用C3P0连接池较多。

**Hibernate两种获取session方式**

openSession、getCurrentSession

- 获取的是否是同一个session对象

  openSession每次都会得到一个新的Session对象 
  getCurrentSession在同一个线程中，每次都是获取相同的Session对象，但是在不同的线程中获取的是不同的Session对象 

- 事务提交的必要性

  openSession只有在增加，删除，修改的时候需要事务，查询时不需要的 
  getCurrentSession是所有操作都必须放在事务中进行，并且提交事务后，session就自动关闭，不能够再进行关闭 



### 第五节课

