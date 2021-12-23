# -*- coding: utf-8 -*-

from app import app, db
from app.models import User, Book, Log, Role, Author, Publisher, Genre, Udc

app_ctx = app.app_context()
app_ctx.push()
db.create_all()
Role.insert_roles()

admin = User(name=u'root',
             email='root@gmail.com',
             password='password',
             major='administrator',
             headline=u"Temporary Administrator One",
             about_me=u"Graduated from the Department of Management, and "
                      u"likes to read, so I work as a librarian part-time.")
user1 = User(name=u'akarin',
             email='akarin@Gmail.com',
             password='123456',
             major='Computer Science',
             headline=u"ordinary student")
user2 = User(name=u'test',
             email='test@test.com',
             password='123456')
user3 = User(name=u'Xiao Ming',
             email='xiaoming@163.com',
             password='123456')
user4 = User(name=u'Li Hua',
             email='lihua@yahoo.com',
             password='123456')

author1 = Author(surnames_initials="dfd")
author2 = Author(surnames_initials="qwqw")
author3 = Author(surnames_initials="zxx")

publisher1 = Publisher(publisher="qwqw")
publisher2 = Publisher(publisher="qwqw1")
publisher3 = Publisher(publisher="qwqw2")

genre1 = Genre(genre="asas")
genre2 = Genre(genre="azxz")
genre3 = Genre(genre="avbv")

udc1 = Udc(udc_number=123)
udc2 = Udc(udc_number=124)
udc3 = Udc(udc_number=125)

book1 = Book(author1, publisher1, genre1, udc1,
             title=u"Flask Web Development",
             isbn='9787115373991',
             pub_year=2004,
             tags_string=u"computer, programming, web development",
             image='http://img3.douban.com/lpic/s27906700.jpg',
             summary=u"""
# This book is not only suitable for junior Web developers to learn to read, but also an excellent reference book for Python programmers to learn advanced Web development techniques.

* Learn the basic structure of Flask applications and write sample applications;
* Use necessary components, including templates, databases, Web forms, and email support;
* Use packages and modules to build scalable large-scale applications;
* Realize user authentication, roles and personal data;
* Reuse templates, paging display lists, and use rich text in blog sites;
* Use Flask-based REST APIs to implement available functions on smartphones, tablets and other third-party clients;
* Learn to run unit tests and improve performance;
* Deploy the web application to the production server.
""")
book2 = Book(author1, publisher1, genre1, udc1,
             title=u"STL source code analysis",
             isbn='9787560926995',
             pub_year=2004,
             tags_string=u"computer, programming, C++",
             image='http://img3.doubanio.com/lpic/s1092076.jpg',
             summary=u"""* Anyone who learns programming knows that reading and analyzing famous codes is a shortcut to improve the level. Before the source code, there is no secret. The meticulous thinking, experience crystallization, technical ideas, and unique styles of the masters are all in the original Reflected in the source code.
* The source code presented in this book allows readers to see the realization of vector, list, heap, deque, Red Black tree, hash table, set/map; see various The realization of algorithms (sorting, searching, permutation and combination, data movement and copying technology); even the realization of the underlying memory pool and high-level abstract traits mechanism can be seen. """)
book3 = Book(author1, publisher1, genre1, udc1,
             title=u"Principle of Compilation (2nd Edition of the Original Book)",
             isbn="9787111251217",
             pub_year=2008,
             tags_string=u"computer, compilation principle",
             image='http://img3.douban.com/lpic/s3392161.jpg',
             summary=u"""* This book comprehensively and in-depth explores important topics in compiler design, including lexical analysis, grammatical analysis, grammar-guided definition and grammar-guided translation, runtime environment, target code generation, code optimization technology, Parallelism detection and inter-process analysis technology, and a large number of examples are given in the relevant chapters. Compared with the previous edition, this book has undergone a comprehensive revision to cover the latest developments in compiler development. Each chapter provides A large number of systems and references.
* This book is a classic textbook for the course of compilation principles, with rich content. It is suitable for use as a textbook for undergraduate and graduate students of computer science and related majors in universities and colleges, and it is also an excellent reference reading for the majority of technical personnel. """)
book4 = Book(author1, publisher1, genre1, udc1,
             title=u"In-depth understanding of computer systems",
             isbn="9787111321330",
             pub_year=2007,
             tags_string=u"computer, computer system",
             image='http://img3.douban.com/lpic/s4510534.jpg',
             summary=u"""* This book elaborates on the essential concepts of computer systems from the perspective of programmers, and shows how these concepts actually affect the correctness, performance and practicability of application programs. The book has 12 chapters, the main content Including information representation and processing, machine-level representation of programs, processor architecture, optimized program performance, memory hierarchy, links, abnormal control flow, virtual memory, system-level I/O, network programming, concurrent programming, etc. In the book Provide a lot of examples and exercises, and give some answers to help readers deepen the understanding of the concepts and knowledge described in the text.
* The biggest advantage of this book is to describe the implementation details of the computer system for programmers, help them construct a hierarchical computer system in the brain, from the representation of the lowest data in memory to the composition of pipeline instructions, to virtual memory, To the compilation system, to the dynamic loading library, to the final user mode application. By mastering how the program is mapped to the system and how the program is executed, readers can better understand why the program behaves like this and how inefficiency is caused.
* This book is suitable for programmers who want to write faster and more reliable programs. It is also suitable as a textbook for undergraduates and graduate students in computer science and related majors in colleges and universities. """)
book5 = Book(author1, publisher1, genre1, udc1,
             title=u"C# in a nutshell",
             isbn="9787517010845",
             pub_year=2006,
             tags_string=u"computer, programming, C#",
             image='http://img3.douban.com/lpic/s28152290.jpg',
             summary=u"""* "c# in the shell-the authoritative guide for c#5.0" is an authoritative technical guide for c#5.0 and the first learning material for the Chinese version of c#5.0. This book has passed 26 chapters The content of this book systematically, comprehensively and meticulously explains the commands, grammar and usage of c#5.0 from basic knowledge to various advanced features. The explanations in this book are simple and easy to understand. At the same time, each point of knowledge is specifically designed to be appropriate, simple and easy Understanding learning cases can help readers accurately understand the meaning of knowledge points and quickly apply what they have learned. Compared with the previous version of c#4.0, this book also adds a wealth of concurrent, asynchronous, dynamic programming, code refinement, Content related to advanced features such as security and com interaction.
* "C# in the shell-c#5.0 authoritative guide" also integrates the author's years of research and practical experience in software development and c#, which is very suitable as a self-study tutorial for c# technology, and it is also a book A must-have reference book for intermediate and advanced c# technicians. """)
book6 = Book(author1, publisher1, genre1, udc1,
             title=u"Introduction to Algorithms (2nd Edition of the Original Book)",
             isbn="9787111187776",
             pub_year=2005,
             tags_string=u"computer, algorithm",
             image='http://img3.doubanio.com/lpic/s1959967.jpg',
             summary=u"This book provides a comprehensive introduction to computer algorithms. The analysis of each algorithm is easy to understand and very interesting, and maintains mathematical rigor. The design goals of this book are comprehensive and suitable for many purposes. Covering The content includes: the role of algorithms in calculations, probability analysis and the introduction of random algorithms. The book specifically discusses linear programming, introduces two applications of dynamic programming, randomization and approximate algorithms of linear programming technology, etc., as well as related Recursive solution, division method and expected linear time sequence statistical algorithm used in quick sort, as well as the discussion of greedy algorithm elements. This book also introduces the proof of the correctness of the strongly connected subgraph algorithm, and the calculation of Hamiltonian cycles and subsets And the proof of the NP completeness of the problem. The book provides more than 900 exercises and thinking questions, as well as more detailed case studies.")
logs = [Log(user1, book2), Log(user1, book3), Log(user1, book4), Log(user1, book6),
        Log(user2, book1), Log(user2, book3), Log(user2, book5),
        Log(user3, book2), Log(user3, book5)]

db.session.add_all([admin, user1, user2, user3, user4, author1, author2, author3,
                    publisher1, publisher2, publisher3, genre1, genre2, genre3,
                    udc1, udc2, udc3,
                    book1, book2, book3, book4, book5, book6] + logs)
db.session.commit()

app_ctx.pop()
