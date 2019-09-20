About:
NHL Stats is a project that is aiming to make it easy for anyone to analyze, interpret, and share National Hockey League statistics and insights.

The core of the project is a system where users will be able to play with existing statistics and create new metrics by which to judge players. The goal of this project is to create a simple platform which anyone would be able to use without any prior knowledge.

Building on the core concept, plans include saving metrics and various inputs to user accounts, using that saved information for data visualization, and ultimately being able to write up and share blog-style posts about one's findings.

Interesting Features:
This project is written using Django, a web framework based in Python. There are several features of Django which are utilized in this project. Django has built-in authentication which means this project has secure and efficient login and signup. Django-tables2 is a popular table module which is used in the core statistics display of the website. This project has its own small language associated with metric definitions. There is an interpreter for the mostly math-based language which is complete with lexer, parser, and execution functions. The aim of the interpreted language is to give users a way to create new metrics without any over-complicated features.

Running:
- Download the repository
- Command Line: 'python manage.py runserver' from the main folder
- Visit http://127.0.0.1:8000/stats/ in the browser 

Website:
At the moment, this project is not being hosted. However, it is ultimately the goal of this project to allow others who are interested in NHL statistics to be able to easily find and use it. Therefore, stay tuned for updates on the web hosting front.