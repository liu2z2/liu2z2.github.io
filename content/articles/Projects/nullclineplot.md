---
Title: Mathematical Steady State Analysis by Plotting in Python
Date: 2019-10-21
Status: published
Tags: project
---
[TOC]

The source of the project can be found [here](https://github.com/liu2z2/nullclineplot).

This is not a whole project, but actually part of the final project on a class called Math Modelling. For the project, my friend, Wayne Stegner (Computer Engineering Undergraduate at UC), and I were supposed to model an age-based predation and analyze the behavior of the model. This article will not focus on how we approached the model mathematically, but rather how we used Python to plot the model for the steady state analysis to avoid solving for multi-variable differential equations. 

### Background
The model was reduced to two equations in (Eq 1), where u and v are independent variables. **Steady state** is where $\frac{du}{dt}$ and $\frac{dv}{dt}$ are both 0. However, it can be difficult to solve by setting both equations to 0, so we can use nullclines of $\frac{du}{dt}$ and $\frac{dv}{dt}$ instead. **Nullcline** of a variable is the plot where the derivative this variable over time is 0. Therefore, the intercept of $u$ and $v$ represents steady state. Moreover, a steady state can also be **stable** or **unstable**. This is done by **linear stability analysis**. In this specific model, it was found that the steady state is stable if the equation in Eq. 2 is positive; otherwise unstable. Thus, the discussion over steady state is around two questions.

- Does steady state exist in the given domain? How many of them?
- Is the steady state stable?

The Python script that plots the model is supposed to give a direct answer to these two questions. 

$$
\frac{d}{d\tau} v = B u - v - D v (u+v) - P v \\
\frac{d}{d\tau} u = v - u (u+v) - Q u
$$
<div style="text-align: right"> Differential Equations of the Model (Eq 1) </div>

$$
D = (- 1 - Du - 2Dv - P)(-2u - v - Q) - (1 - u)(B - D v)
$$
<div style="text-align: right"> Stability Criterion (Eq 2) </div>

### Methodology
The two differential equations in Eq. 1 are both functions of $u$ and $v$, so by plotting the u-nullcline and v-nullcline on a $u$-vs-$v$ coordinate plane, steady state is where the two nullclines intercept. If they ever intercept, steady state exist, and how many intercepts dictates the number of steady states. 

Moreover, the $D$ variable in Eq. 2 is also a function of $u$ and $v$, but now the criterion is its sign, or an inequality between 0. On one hand, plugging in a steady state expression that is already complicated is hard, on the other hand, graphically, such inequality separates the $u-v$ plane into two areas, positive $D$ and negative $D$. Therefore, a contour map of this $D$ function can be superimposed onto the two nullcline plot. If their intercept is located in $D>0$ region, the steady state is stable; otherwise unstable. 

### Result

The plotting was successful. We were able to test the steady states by setting different external parameters ($B$, $D$, $P$ and $Q$) and draw conclusions out of the testings without math-heavy calculations. Some example results are shown figures below. 

<figure>
  <img src="/images/project-nullclineplot/plt1.webp"/>
  <img src="/images/project-nullclineplot/plt2.webp"/>
  <img src="/images/project-nullclineplot/plt3.webp"/>
</figure>

### What I learned from this
Math sometimes can be hard and time-consuming for engineers. Luckily, with adequate programming skills, computer plotting can be helpful, making math analysis experimental. Such implementation, however, requires a clear vision on the math itself as well as an appropriate way to visualize the data. For our math modelling project, we were able to identify the two questions the analysis is based upon, and create a good method to answer both in one plot, making the program useful to the analysis. 

**For questions regarding the program or the math model itself, please contact me using the sidebar or contact Wayne Stegner at stegnewe@mail.uc.edu.**