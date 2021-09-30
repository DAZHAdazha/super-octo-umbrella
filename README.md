# COVID-19 data visualization
# Show-me-data system
## Breif Project introduction:
>  Use online epidemic data API to generate visualized charts, toplists and many other functionalities to users.
 > Use Vue as the front-end along with e-charts to present charts.
 > Use Flask as the back-end services to handle data.
 
 
 # Detailed introduction
# 1 Overview
## 1.1 Background:
The novel coronavirus pneumonia is a global public health event. Under the influence of the 
epidemic, hundreds of millions of people around the world are eager to understand the current 
epidemic situation. A few months ago, Alibaba, Baidu, Tencent and other enterprises have 
implemented their own epidemic data websites. People can know the epidemic situation by moving 
their fingers, so as to do their own protection work more scientifically.
## 1.2 Application fields and objects:
All individuals who want to know the basic situation of the epidemic situation
## 1.3 Application requirements:
As novel coronavirus pneumonia is becoming more and more popular, people are increasingly 
concerned about the epidemic situation and data around the world. Therefore, a visualization 
platform for collecting epidemic data, news and knowledge at home and abroad is urgently needed.
## 1.4 Comparison of similar products:
Compared with the similar epidemic data visualization system, the advantage of this system is that it 
not only has many charts and maps of regional epidemic data display, but also has additional 
functions such as propagation simulation, rumor, news search, prevention knowledge, etc., which 
can greatly enrich the user experience.
# 2.System overview:
## 2.1 Introduction to system functions
Comdata the system is a set of visualization system based on the website, which can provide the 
visualization of history and current epidemic situation for all people concerned about the epidemic 
situation. It can provide the visualization of real-time epidemic data by using the credible network 
information sources and the database system built by the team. The rolling display of epidemic 
related news, reliable rumor refutation search system, and real-time heat analysis of epidemic news 
are also included。
## 2.2 System technology description
The system mainly refers to the following technologies: Vue, e-charts, data, ant design, flag, MySQL, webpack, web crawler

**Vue** is a progressive front-end JavaScript framework for building user interfaces, which is designed 
to be applied layer by layer from bottom to top. Its core library only focuses on the view layer, 
which is easy to use and easy to integrate with the third-party library or existing projects. On the 
other hand, when combined with modern tool chain and various supporting class libraries, the 
technology can also provide drivers for complex single page applications.

**E-charts** is an open source visualization library implemented by JavaScript, which can run smoothly 
on PC and mobile devices. It is compatible with most current browsers. The bottom layer relies on 
vector graphics library render to provide intuitive, interactive and highly personalized data 
visualization charts.

Based on Vue framework, data component library is mainly used to build large screen data display 
page, that is, data visualization. It has many types of components for use, and can effectively 
display various types of chartsAs a complete UI component library, ant design is developed by typescript and provides complete 
type definition files. It is extracted from the interactive language and visual style of background 
products in the enterprise level. It has a full link development and design tool system.

**Flask** is a lightweight back-end web application framework written in Python. It is based on Werke
toolbox and jinja2 template engine, and can easily link relational database through Sachem module 
for data storage and operation.

**MySQL** is one of the most popular relational database management systems. In web application, 
MySQL is one of the best RDBMS (relational database management system) application software. 
It has the characteristics of high level, scalability, security, reliability and fault free operation.

**Webpack** is a static module bundler for modern JavaScript applications. When webpack processes 
an application, it recursively builds a dependency graph that contains each module the application 
needs, and then packages all of these modules into one or more bundles.

**Web crawler** is a kind of program or script that can automatically grab the information of the world 
wide web according to certain rules. This project mainly uses the request Library Based on Python 
language and beautiful soup library to crawl a small amount of data within the scope of robot’s
protocol.
## 2.3 system architecture
基于 Flask 的
后端数据处理
运用 MySQL 进行
存储，查询
## 2.4 Operating environment requirements
Front end infrastructure: Vue
Back end infrastructure: Flag
IE8 or above or chrome, Firefox, Safari database: MySQL
## 2.5 Design method
The system adopts the traditional method of system development life cycle, adopts the top-down 
and gradually refined structured system design method. It has gone through the stages of problem 
definition, feasibility study, requirement analysis, outline design, detailed design, software 
implementation, software testing, operation and maintenance.
# 3.Function list
## 3.1 Functional structure:
The system mainly provides the related information and prompt real-time data of Xinyuan epidemic 
situation through the way of Web visualization: mainly displays the current and historical epidemic 
data; public opinion analysis: provides real-time news push and search hot spots; analysis of 
epidemic situation review; mainly shows the development process of epidemic situation; epidemic 
situation simulation and rumor warning; new crown prevention: provides reminder and correlation 
of new crown knowledge Reminders from employees.
## 3.2 Display and description of specific pages
## 1. Real time data:
1. Statistics of the number of infected people: the rolling display of the ranking of the total number 
of infected people in the world by using the rotation chart can continuously display the historical 
epidemic data of different countries
2. New display of domestic epidemic situation: Based on the map of China, the new distribution 
map of China's epidemic situation today and the rose chart of newly imported cases in China can 
highlight the data of a certain region by mouse click or hover.
3. World cumulative display: Based on the world map, the distribution map of cumulative infected 
persons in the world can highlight the data of a certain area by mouse click or hover.
4. Epidemic news display: rolling display and content source analysis of epidemic related news. 
News information can be obtained by clicking links or viewing brief contents.
### Data sources:
1.Global and domestic new data: HTTPs://interface.sina.cn/news/wap/fymap2020_data.d.json
2.Epidemic related news data: HTTPs://api.yonyoucloud.com/apis/dst/ncov/query
3.Global ranking of epidemic situation: 
https://corona.lmao.ninja/v2/countries?yesterday&sort=cases
4.Historical rumors, news data: HTTPs://github.com/BlankerL/DXY-COVID-19-Data
## 2. Public opinion analysis:
1. News fever chart: novel Coronet ranking list of novel coronavirus pneumonia is constructed by 
crawling Baidu index data. By looking at the heat map, we can know the heat words related to the 
epidemic situation.
2. News search: using the existing news data warehouse of the network, establish the connection 
between MySQL database and flash back-end to complete the real-time news search function. The
news can be viewed and retrieved by query.
3. Epidemic news display: a link between the rolling display of epidemic related news and the web 
source. When the user does not perform the news search operation, the current real-time news will 
be provided by default.
### Data sources:
1.Global and domestic new data: HTTPs://interface.sina.cn/news/wap/fymap2020_data.d.json
2.Epidemic related news data: HTTPs://api.yonyoucloud.com/apis/dst/ncov/query
3.News query data: Mining self-built news MySQL database through network
4.Real time hot spot: Baidu Index interface crawled by crawler
## 3. Epidemic situation review:
1. Epidemic situation broken line chart: use e-charts to realize the national and world epidemic 
situation history line chart which can be traced back to the source. The epidemic data can be viewed 
in different time periods by dragging and pulling the mouse.
2. The major event is novel coronavirus pneumonia. The initial development process of the 
epidemic can be known through the marked time and time content.
### Data sources:
1.Historical data: HTTPs://interface.sina.cn/news/wap/fymap2020_data.d.json
2.Time line information: it can be known through network retrieval
## 4. Epidemic Alert:
1. Simulation propagation: the demonstration module of infectious disease transmission process 
based on JS is realized by using e-charts, which can show users the basic and simple simulation of 
virus transmission process. Users can set their own data to simulate the development of the new 
crown in the crowd
2. Rumor search: use the existing rumor data warehouse on the network to establish the 
connection between MySQL database and flash back-end to complete the real-time rumor search 
function. The rumor can be viewed and searched by inquiry.
3. Epidemic news display: the rolling display of epidemic related news and the link to the website 
source. When the user does not perform rumor search operation, the current real-time news will be 
provided by default.
### Data sources:
1.Rumor data: Mining self-built rumor MySQL database through network
## 5. New crown prevention:
1.Epidemic prevention: through the form of rolling column, show the way to fight the new crown 
epidemic. The historical epidemic data of different countries can be displayed continuously
2.Risk index of epidemic situation work: display the risk index of dangerous industries under the 
epidemic situation in the form of rolling, and remind relevant employees to pay attention to 
prevention.
### Data sources:
1.News query data: Mining self-built news MySQL database through network
2.Risk index ranking: network data
## 4.Future improvement plan:
1. diversified display platforms. Based on the display of more platforms (APP, WeChat official 
account, etc.).
2. rationalization of screen structure. Optimize the construction of screen elements to build a more 
reasonable picture arrangement.
3. demonstrate data depth. Build a more powerful crawler system to analyze network public 
opinion.
4. cloud-based website. Because the system is based on the front and back-end framework of Flash 
+ Vue, the database and back-end applications can be easily deployed on the network cloud server, 
such as Alibaba cloud.
## 5.Reference：
https://cn.vuejs.org/ https://echarts.apache.org/zh/index.html 
https://www.webpackjs.com/ https://ant.design/index-cn 
http://datav.jiaminghi.com/ 
https://api.yonyoucloud.com/apis/dst/ncov/query 
https://corona.lmao.ninja/v2/countries?yesterday&sort=cases 
https://github.com/BlankerL/DXY-COVID-19-Data
https://interface.sina.cn/news/wap/fymap2020_data.d.json
 
