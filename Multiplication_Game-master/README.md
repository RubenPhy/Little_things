# Multiplication Game

I wanted to create a game where I could practice mental calculus with my phone connected to my Rasberry.
The idea was easy.

    1.You choose the range of number to multiplicate.
    2.Choose the max time you need.
    3.Start the random multiplication and if you pass the time, the game will finish.

But when I arrived to the last point the troubles started. Because the input function is a **blocking call**, i.e. the code **will not continue until you input something**. 

I start to seek a solution but all the answers come up with the same solution as I did in my first try (main_v1).

With consist in say *Time is out!* after you reach the time but after you input any date.

Also there was a solution with **signal.SIGALRM** but it doesn’t work for Windows.

So I realize that this problem had to be threaded but in a way that if one process is finish, it will kill the others. I put the links that I used.

https://stackoverflow.com/questions/53064280/equivalent-of-thread-interrupt-main-in-python-3

https://docs.python.org/3.6/library/_thread.html

https://kite.com/python/docs/thread.interrupt_main

Finally, I added a few thinks to make it more friendly.

    1.Score.
    2.Be able to safe your score.
    3.Stop the game if you where wrong, to think about the correct answered.

So... I am using **main_v2** in my Rasberry which I can connect with myh phone and it works perfect!

I will appreciate any comments.
