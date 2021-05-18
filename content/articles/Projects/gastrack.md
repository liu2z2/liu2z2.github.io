---
Title: Developing a Gas Price Tracking and Prediction Application
Date: 2020-04-29
Status: published
Tags: UHP
---
[TOC]

### Introduction

The project is about developing a web application based on data that is related to automobile gas prices. The desired feature of the application is that it collects gas prices at different places every day (specific to stations), recommends the user the cheapest station in the area, reminds the user of an increasing/decreasing trend of the price, and generates a report of gas prices that is helpful to economic analysis. It falls under creativity competency because by the time the project was proposed, there has not been similar tools for this specific application, so it could be hard to decide on how to implement this idea. 

This experience will let me know the process of developing an application skill-wise, during which I would utilize my programming, math and engineering skills to achieve the end goal of the project.

On one hand, the app will help people save money on their commuting travel. On the other hand, the data I collected would be a useful resource to understand oil-related economy, realize potential problems and possibly propose a solution applicable to the original idea of the project.

### Procedure
I divided the project into a few phases. 1) Setting up the environment and base code; 2) building the database by updating on daily basis; 3) developing a method for data statistics; and 4) developing the application. 

The first phase took longer than expected because I needed to pick up SQL database, which I did not have too much experience working with before. In addition, I also had to make sure everything is set up well so that the data collected later is comprehensive but easy to manage. Afterwards, at the end of October 2019, the code was put in a computer programmed to run once per day (phase two).

During the data collecting process, several issues occurred due to hardware and software, making it inconsistent at a few time stamps, but luckily, they got fixed quickly so the overall data trend was not interrupted. After a few months, the database was found large enough for statistical analysis, so the third phase started after 2019's Christmas.

The development of this part was also time consuming, as I was trying different statistical tools while also learning database merging methods in order for the source files to look professionally organized. Unfortunately, right after I finished my research and decided a way to implement (at the end of February 2020), COVID-19 hit the country hard. During the time I struggled to adapt to working-from-home environment, I decided to close the project as it is considering two reasons. Firstly, I wanted to prioritize finishing my classes and research until the end of the semester; and secondly, the gas market may have been affected by the pandemic, which is an significantly influential variable that may complicate the case study. Therefore, at the end of the Spring semester 2020, I briefly implemented data visualization by plotting the data per city, and concluded the project.

The technical aspect of the project will be explained in the [project](https://liu2z2.github.io/tags#project-ref) category while this reflection mainly focused on the overall execution and the learning experience. 

### Results
Some examples of the visualized data as of the closing phase of the project are shown in Figures 1, 2 and 3. Plotted in different colors, the mean prices of three gas grades are connected together with respect to time, where there are vertical grey bars whose upper and lower bounds illustrate the max and min price number. Then the three curves are put together in the same plot. 

<img src="/images/discuss-gastrack/Lexington.webp"/ width=30%>
<img src="/images/discuss-gastrack/Cincinnati.webp"/ width=30%>
<img src="/images/discuss-gastrack/Columbus.webp"/ width=30%>

Comparing and contrasting the plots result in a few interesting findings:

1. Fluctuations of the prices in three gas grades share similar patterns.
2. Prices in neighbored areas may increase/decrease at similar time, but the amount may vary.
3. Regarding a specific gas grade in one area, lowest price point changes in a similar manner as the mean price, but the max price point is quite stationary.

### Conclusion

Though the end goal of the project was not achieved before closing, the method of web crawling and data mining was proven viable for the intended application, and I believe it can lead to a promising direction if more effort and time are given. Better project management could have been used to improve the productivity, but there are still proud parts in the execution, such as breaking the process down into several phases. 

In addition, if the project is ever to be continued, there are a few recommendations for improvement.

1.  There are a few interruptions in the data collecting phase for various reasons. For example, the program crashed because of unexpected errors. Incidents like this can be avoided by considering more edge cases when writing the code.

2.  The data was obtained by web scraping gasbuddy.com, which is a website where anyone can upload data. This source can be inaccurate and unreliable sometimes. Better sources can be used to improve this.

3.  There must have been more statistical tools that can be used for analysis. More exhaustive research on them could offer more information about the data.

4.  In order to make prediction, apart from a larger amount of dataset and a well-modeled algorithm, a good understanding of economics can be important. Generalizing patterns as discussed in the results section is important, but an educated guess may also come from an existing the economic model.


As a learning experience, this project enhances my software programming skills, which I don't usually learn from my EE curriculum. This was also my first time using SQL database, which I found is a useful tool with a steep learning curve. Finally, as of the closing phase, I came to realize that I did not know enough statistical and economical tools to understand the data comprehensively, and therefore I became interested and motivated to learn them along my study.