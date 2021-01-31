---
Title: Using Google Calendar API to Auto-Create Tutoring Events
Date: 2019-10-21
Status: published
Tags: project
---
[TOC]

The source of the project can be found [here](https://github.com/liu2z2/TutorCal).

This is a project I started personally since March 2019 when I worked as a peer tutor at UC Tutoring Center (previously called Learning Commons). 

### Motivation
The way Peer Tutoring works at UC is that students schedule appointments with me, and I get email notification when they do so. TutorTrac is a system where students schedule appointments, and I see my appointments beforehand. An example of how the system looks is shown in Figure 1. However, though being a stable system maintained since 2011, TutorTrac has some inconvenient features

- It is hard for me to navigate when I use my phone to look at my schedule
- For every event, it shows Last name first, but we usually refer to students' first name
- It only shows the class code of the assisting course instead of full name, making me hard to identify the class

This encourages me to develop my own method of seeing the schedule.

<figure>
  <img src="/images/project-tutorcal/tutortrac.webp"/>
  <figcaption> <small> Figure 1 - TutorTrac System </small> </figcaption>
</figure>

### Design
The system reads the email notification of incoming tutoring appointments, scrapes the necessary information, and pushes it to my Google calendar in a better format. Thus I can see my schedule directly from the calendar widget of my phone (Android). Ideally it should scan the email notifications every 10-30 minutes and automatically generate events without being monitored. Additional good-to-have feature is that it will also store the appointment info at local, and try to match everyday's schedule reminder sent from TutorTrac. Later it was found this part was hard to implement given the time, so it was deserted. 

#### Design diagram 

<figure>
  <img src="/images/project-tutorcal/design.webp"/>
  <figcaption> <small> Figure 2 - Design Diagram </small> </figcaption>
</figure>

#### Reading UC Email Notifications
The notification received from TutorTrac follows a specific format (Figure 3). Therefore it is viable to hard-code the format into the program, making the scraping info method easier. Additionally, considering UC email is my most important mail address, as well as the fact that getting around UC server is hard and possibly not allowed, I created a rule at my UC mailbox to automatically forward any emails from TutorTrac to a gmail account I created for this project. 

<figure>
  <img src="/images/project-tutorcal/email.webp"/>
  <figcaption> <small> Figure 3 - TutorTrac Email Notif </small> </figcaption>
</figure>

#### Main Program

The program is made up of three python scripts. 

`email_read.py`: contains functions that reads email from Gmail account and scrape appointment info. Email interface is through imaplib module. Additionally, there is a csv look-up table, where the program can find the matching full name of the class from the course code. 

`google_cal.py`: contains functions that pushes the appointment info to my Google calendar. This script is inspired by an article on Google site [Google Calendar API Python Quickstart](https://developers.google.com/calendar/quickstart/python)

`controller.py`: uses the two modules and sets up the logging.

#### Hardware Implementation

The project does not requires too much in hardware except for the ability to run Python scripts and Internet accessibility. Therefore a Raspberry Pi 3 Model B (Figure 4) was used to implement the design. VNC Viewer is used to remote control the machine wirelessly from other computers. Raspbian with Kernel verion 4.14 was installed on the board, where it was found that there is a Scheduling tool (Figure 5) that lets a command run every period of time. This can also be done by hard-coding in CRON, which is the core of scheduling tool (i.e. scheduling is a GUI of CRON). Detail info about using CRON or scheduling tool see /CRONtest/note.txt on GitHub repo. 

<figure>
  <img src="/images/project-tutorcal/rpi.webp"/>
  <figcaption> <small> Figure 4 - Raspberry Pi 3 in Operation </small> </figcaption>
</figure>

<figure>
  <img src="/images/project-tutorcal/rpi.webp"/>
  <figcaption> <small> Figure 5 - Cron Task Setup </small> </figcaption>
</figure>

#### Long-Term Management and Maintenance

To make sure the program runs completely without errors stopping the process, I changed the script so that the error message will show in log file while the erroneous part is passed. Using `logging` module, the code also logs important stages in the operations (Figure 6). I also coded parts where the Internet is used to push/pull data to allow 99 retries, reducing the odds of getting bad connections. 

<figure>
  <img src="/images/project-tutorcal/log.webp"/>
  <figcaption> <small> Figure 6 - Cron Task Setup </small> </figcaption>
</figure>

### Results

The project was successful. It helped me manage my tutoring schedule over the last month of the semester. I was able to see who scheduled what class at my phone easily. Figure 8 is a side-by-side comparison between TutorTrac and how it turns out in my Google calendar. 

<figure>
  <img src="/images/project-tutorcal/gcal.webp"/>
  <figcaption> <small> Figure 7 - TutorTrac schedule (left, yellow blocks) vs Google Calendar (right, blue blocks) </small> </figcaption>
</figure>

### What I Learned From the Project

- Access emails in Python with imaplib
- Create Google calendar events with Google API
- Use logging to maintain a constantly running program
- Create a hardware environment (Raspberry Pi) and method to support a mini-server

### Future Recommendations

Pushing events can be easy, but retrieving them from my calendar may be hard. For future implementation, it will be good to have an additional module to retrieve the events, check with the local record, thus making sure the schedule is correct. 

