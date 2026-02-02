# 36-401:Modern Regression
**URL:** https://www.stat.cmu.edu/~cshalizi/mreg/15
**Page Title:** 36-401, Modern Regression (2015)
--------------------


## 36-401, Modern Regression, Section B

## Fall 2015

Here's the official description:
This is a class on linear statistical models: the oldest, most widely used,
and mathematically simplest sort of statistical model.  It serves
as a first course in serious data analysis, as an introduction to
statistical modeling and prediction, and as an initiation into a community
of inquiry which has developed over two centuries and grown to include
every branch of science, technology and policy.
During the class, you will do data analyses with existing software, and
begin learning to write your own simple programs to implement and extend key
techniques.  You will also have to write reports about your analyses.
Graduate students from other departments wishing to take this course should
register for it under the number "36-607".  Enrollment for 36-607 is very
limited, and by permission of the professor only.
Mathematical statistics: one of 36-226, 36-326 or 36-625, with at least a
grade of C; linear algebra, one of 21-240, 21-241 or 21-242, with at least a
grade of C.  These requirements will not be waived for undergraduates under any
circumstances.  Graduate students wishing to enroll in 36-607 will need to have
had equivalent courses (as determined by the instructor).
Having previously
taken 36-350 ,
introduction to statistical computing, or taking it concurrently, is strongly
recommended but not required.

## Topics, Notes, Readings

This is currently a tentative listing of topics, in order.

## Course Mechanics

There will be two in-class mid-term exams, both focusing on
the theoretical portions of the course.  Both exams will be cumulative.  Each
exam will be 15% of your final grade.
There will be three take-home projects where you will analyze real data
sets, and write up your findings in the form of a scientific report.  You will
be graded both on the technical correctness of your work and on your ability to
clearly communicate your findings; in particular, raw computer output or code
are not acceptable.  (Rubrics and example reports will be made available before
the first DAP is assigned.)
The DAPs are exams; consequently, collaboration is not allowed.
Each DAP will count for 15% of your final grade.
The homework will give you practice in using the techniques you are learning
to analyze data, and to interpret the analyses.  They will also include some
theory questions, requiring you to do calculations or prove results
mathematically.  There will be one homework assignment every week in which
there is not an exam.  Every assignment will count equally towards 25% of your
grade.  Your lowest two homework grades will be dropped;
consequently, no late homework will be accepted for any
reason .
Communicating your results to others is as important as getting good results
in the first place.  A portion of the points available for every homework will
be set aside to reflect the clarity of your writing, figures, data
presentation, and other marks of communication.  (Rubrics will be provided for
each assignment.)  In addition, at least two homeworks will be practice DAPs,
where you will have to write reports in the same manner as the data analysis
projects.
Except as otherwise noted in the schedule, all assignments will be due at 3
pm on Thursdays (i.e., at the beginning of class), through Blackboard.  Late
assignments are not accepted for any reason.  Coming late to class because you
are uploading an assignment is unacceptable.
You will submit a PDF or HTML file containing a readable version of all your
write-ups, mathematics, figures, tables, and selected portions of code
as relevant. Word files will not be graded. (You may
write in Word if you must, but you need to submit either PDF or HTML.)
You are strongly encouraged to use R
Markdown to integrate text, code, images and mathematics.  If you do, you
will submit both the "knitted" PDF or HTML file, and the source .Rmd file.  If
you choose not to use R Markdown, you will submit both a humanly-readable file,
as PDF or HTML, and a separate plain-text file containing all your R code,
clearly commented and formatted to indicate which code section goes with which
problem.
If you do not use an equation editor, LaTeX , etc., you may include pictures
or scans of hand-written mathematics as needed.
If you want help with computing, please bring your laptop.
If you cannot make the scheduled office hours, please e-mail the professor
about making an appointment.
The primary textbook for the course will be Kutner, Nachtsheim and
Neter's Applied Linear Regression Models , 4th edition
(McGraw-Hill, 2004,
ISBN 0-07-238691-6 ).
This is required .  (The fifth edition is also acceptable,
though if you use it, when specific problems or readings are assigned from the
text, you are responsible for ensuring that they match up with what's
intended.)
Four other books are recommended :
- Julian J. Faraway , Linear Models with R , second edition (CRC Press, 2014,
ISBN 978-1-439-88733-2 )
- Paul Teetor, The R Cookbook (O'Reilly Media, 2011,
ISBN 978-0-596-80915-7 )
- D. R. Cox and Christl Donnelly, Principles of Applied Statistics (Cambridge
University Press, 2011,
ISBN 978-1-107-64445-8 )
- Richard A. Berk, Regression Analysis: A Constructive Critique (Sage Press, 2004, ISBN 978-0-7619-2904-8 )

## Computational Work

R is a free, open-source software
package/programming language for statistical computing.  Many of you will have
some prior exposure to the language; for the rest, now is a great time to start
learning.  Almost every assignment will require you to use it.  No other form
of computational work will be accepted.  If you are not able to use R,
or do not have ready, reliable access to a computer on which you can do so, let
me know at once.
R Markdown is an extension to R
which lets you embed your code, and the calculations it produces, in ordinary
text, which can also be formatted, contain figures and equations, etc.  Using R
Markdown is strongly encouraged .  If you do, you need to
submit both your "knitted" file (HTML or PDF, not Word), and the original
.Rmd file.
If you choose to not use R Markdown, for all computational assignments
you need to submit both a properly-formatted humanly-readable write-up,
in PDF, and a raw text file contain your R code, commented so that
it is clear which pieces of code go with which problem.  The write-up
may be a .txt file, PDF, or HTML; Word files will not be graded.
Here are some resources for learning R:
- The official intro, "An Introduction to R", available online in HTML and PDF
- John Verzani, "simpleR",
in PDF
- Quick-R .  This is
primarily aimed at those who already know a commercial statistics package like
SAS, SPSS or Stata, but it's very clear and well-organized, and others may find
it useful as well.
- Patrick
Burns, The R
Inferno .  "If you are using R and you think you're in hell, this is a map
for you."
- Thomas Lumley, "R Fundamentals and Programming Techniques"
( large
PDF )
- Paul Teetor, The R Cookbook , explains how to use R to
do many, many common tasks.  (It's like the inverse to R's help: "What command
does X?", instead of "What does command Y do?").
- The notes for 36-350, Introduction to
Statistical Computing
- There are now many books about R.  Some recommendable ones: Joseph Adler R in a Nutshell ( O'Reilly, 2009 ;
ISBN 9780596801700 ).  Probably most useful for those with previous experience programming in another language. W. John Braun and Duncan
J. Murdoch , A
First Course in Statistical Programming with R (Cambridge University Press, 2008; ISBN 978-0-521-69424-7 ) John M. Chambers, Software for Data Analysis:
Programming with R ( Springer, 2008 ,
ISBN 978-0-387-75935-7 ).
The best book on writing clean and reliable R programs; probably more advanced
than you will need. Norman
Matloff , The Art of R Programming (No Starch Press, 2011,
ISBN 978-1-59327-384-2 ).
Good introduction to programming for complete novices using R.  Less statistics
than Braun and Murdoch, more programming skills.
- Joseph Adler R in a Nutshell ( O'Reilly, 2009 ;
ISBN 9780596801700 ).  Probably most useful for those with previous experience programming in another language.
- W. John Braun and Duncan
J. Murdoch , A
First Course in Statistical Programming with R (Cambridge University Press, 2008; ISBN 978-0-521-69424-7 )
- John M. Chambers, Software for Data Analysis:
Programming with R ( Springer, 2008 ,
ISBN 978-0-387-75935-7 ).
The best book on writing clean and reliable R programs; probably more advanced
than you will need.
- Norman
Matloff , The Art of R Programming (No Starch Press, 2011,
ISBN 978-1-59327-384-2 ).
Good introduction to programming for complete novices using R.  Less statistics
than Braun and Murdoch, more programming skills.
- The R Markdown Cheat Sheet
In fall 2015, Section A of the class is being taught by Prof. Xizhen Cai;
the two sections will be closely coordinated but are separate classes.
If you came here from a search engine, you may be looking for
information on previous versions of the class , as taught by Prof. Rebecca Nugent .

## Schedule


--------------------