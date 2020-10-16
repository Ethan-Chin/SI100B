# SI 100B Homework 1: SKY PRIORITY

* **Authors**: Diao Zihao \<diaozh@shanghaitech.edu.cn\>,  Jiang Yingwenqi \<jiangywq@shanghaitech.edu.cn\>, Qiu Longtian \<qiult@shanghaitech.edu.cn\>
* **Supervised, proofread, edited and approved by** Prof. Haipeng Zhang
* **Last Modified**:  Mar. 16, 2020
* **Release Time**: Mar. 17, 2020
* **Deadline**: 23:59:00 Apr. 2, 2020 China Standard Time (UTC+8:00)
* **Latest Version**: [[Online]](https://si100b.org/content/hw/hw1/) [[PDF]](https://si100b.org/content/hw/hw1/si100b-sp20-hw1-spec.pdf) [[Template Codebase]](http://gitlab1.q71998.cn/homework-20s/homework-1)

## Introduction

You are working as a ground service agent in a really small airport and your job is to handle the boarding process for the flights of China Eastern Airlines from your airport to Shanghai Pudong.

Your airport is quite small, yet the air route to Pudong is quite popular and you need to board all the passengers on time so that the plane can take off on schedule. However, since the airport is quite small, it does not have a boarding bridge, which means that all passengers need to be transferred to the plane using a shuttle bus. Since the airport is small (again), you only have one shuttle bus available which can only take 20 passengers to the plane at a time. And the bus will take 10 minutes to depart from the boarding gate and return back. You need to board all passengers using the bus on time or they will become unhappy!

Your passengers have already waited in line in front of the boarding gate. Now it’s your job to design a program in the Python programming language to assign a passenger a round of shuttle bus given lines of passengers and their arrival time. See detailed descriptions below.

## Getting Started

To get started, please simply fork the [repository](http://gitlab1.q71998.cn/homework-20s/homework-1) on GitLab and follow the structure and submissions guidelines below and on Piazza.

Remember to **make your repository private** before any commits.

*Note*: Markdown text with file extension ***.md*** could be displayed properly using plug-ins in your browsers, IDEs or specialized markdown editors (like [typora](<https://typora.io/>)).

## Repository Structure

### README.md

Homework description and requirements.

### testcases

Some simple testcases for testing the correctness of your program.

### task1.py, task2.py, task3.py, and bonus.py

You need to fill in your answer code for task 1, task 2, task 3 and (optional) bonus in task1.py, task2.py task3.py and bonus.py respectively.

## Submission

**You should check in task1.py, task2.py, task3.py and bonus.py to Gitlab.**

First, make a commit and push your files. From the root folder of this repo, run

```sh
git add task1.py task2.py task3.py bonus.py
git commit -m '{your commit message}'
git push
```

Then add a tag to create a submission.

```sh
git tag {tagname} && git push origin {tagname}
```

You need to define your own submission tag by changing `{tagname}`, e.g.

```sh
git tag first_trial && git push origin first_trial
```

**Please use a new tag for every new submission.**

Every submission will create a new Gitlab issue, where you can track the progress.

## Regulations

- You may **not** use third-party libraries.
- No late submissions will be accepted.
- You have 30 chances of grading (i.e. `git tag`) in this homework. If you hand in more than 30 times, each extra submission will lead to 10% deduction. In addition, you are able to require grading at most 10 times every 24 hours.
- We enforce academic integrity strictly. If you participate in any form of cheating, you will fail this course immediately. **DO NOT** try to hack Gitlab in any way. You can view the full version of the code of conduct on the course homepage: https://si100b.org/resource-policy/#policies.
- If you have any questions about this homework, please ask on Piazza first so that everyone else could benefit from the questions and the answers.

## Specification

### Task 1: Boarding Scheduling

Let’s first consider the simplest case.

Now you are in charge of a flight that only sells economy class seats thus there is only one line of passengers. You are now boarding those passengers using the only shuttle bus available which can only take 20 people to the plane every time. Assume that your shuttle bus can carry a batch of passengers from the boarding gate to the plane and get back in 10 minutes. As soon as the bus returns to the gate, it is ready to depart again with new passengers.

You have a list of passengers that are waiting in the queue marked with their arrival time, your flight number and the time when your boarding should start. Your boarding should start as soon as the boarding time comes. The boarding process shall follow the principle of FCFS (First Come First Served, i.e. the passenger who arrives at the boarding gate first gets on the shuttle bus first). Your program should output the departure time of each round followed by a list of passengers that are transferred to the airplane in each specific round. You could assume that the list of passengers in the program input is ordered by their arrival time to the gate in ascending order. 

Also, aviation security is important. To prevent hijacking, you should prevent passengers who do not have a boarding pass to the flight from boarding the plane. To do this, you need to check the flight number of every passenger trying to board the plane. If the flight number of his/her boarding pass is not the same as the flight number, you should not board the passenger to the bus (and the plane).

Your boarding process scheduling program should follow the following rules for task 1 and also the following two tasks:

- It is very dangerous for the shuttle bus to be overloaded. You should only assign a number of passengers less than or equal to the capacity (20 passengers) of the shuttle bus for one round of transfer;

- To make the process more efficient, the bus should depart only if the bus is full except for the last round when there may be less than 20 waiting passengers at the boarding gate;

- Passengers can board the bus only if they arrive at the boarding gate before or exactly at the time when the bus departs;

- Stop outputting once there are no more passengers needed to be transferred. And the passengers in the program output shall be ordered by their arrival time to the gate. 

You could refer to Appendix A for a specification of the input and output of your program. Your solution should be in `task1.py`. Tests for this task will account for 60% of your overall score of this homework.

### Task 2: Priority Boarding

Now the task is getting more complex. You are dealing with an airplane that sells both economy class seats and business class ones. China Eastern Airlines requires that business class passengers and the gold card members of its frequent-flyers program shall board first.

Now you have two lines of passengers. The first one is the ordinary lane which is for economy class passengers. The second one is the priority lane which is for business class passengers and the gold card members of their frequent flyer program. You can assume that the passengers in the priority lane are all eligible for priority boarding (i.e., they all have business class tickets or are gold card members of their frequent flyer program). 

The boarding process shall also follow the principle of FCFS within a single lane. But the passengers in the priority lane have priority over those in the ordinary lane. To be more specific, the passengers in the priority lane should be on the shuttle bus as soon as it gets to the boarding gate if nobody is in front of him/her in the priority lane, no matter whether there is anyone waiting to be boarded in the ordinary lane. If the shuttle bus is on the way to/from the airplane or the bus is full, they should be immediately put onto the next rounds of shuttle buses available. If a passenger in the priority lane arrives at the same time as one in the ordinary lane, you should board the passenger in the priority lane first.

All other requirements in task 1 will be preserved. And you should again order the list of passengers in your program output by their arrival time to the gate (i.e., get onto the bus) in the acceding order. You should finish your solution in `task2.py`. Tests for this task will account for 30% of your overall score of this homework.

### Task 3: No Waiting!

Assume that now it is summertime, and your passengers will get very mad if they are put on the bus and are waiting for too long!

Now the boarding rule is changed to keep your passenger satisfied. Your bus should depart for the plane immediately if any of the passengers on the bus have been waiting in the bus for no less than 10 minutes, even if the bus is not full.

Now you should write a new program in `task3.py` to schedule the boarding process under the new constraint. All other rules in task 2 are preserved and you also have two lines of passengers. Tests for this task will account for 10% of your overall score of this homework.

### Bonus: Boarding with Parents

Small children will get freaked out if they can’t find their parents! Now consider the situation that kids are boarding the airplane with his/her parents.

Now we add another rule to our boarding process under the assumption of **task 3** that a child shall board the airplane in the same round of shuttle bus as his/her mother/father. A common practice in the aviation industry to identify a child under the age of 12 is to add three capitalized letters CHD at the end of the kid’s name. We will take the same approach to identify children. For example, a passenger named `WANG/XIAOMING` should be considered as an adult and a passenger named `WANG/XIAOMINGCHD` should be considered as a child that need to board with his/her parent.

We also assume that one of a child’s parents is always the next passenger in the queue with him/her and you can assume that a child will never be the last one in the queue. 

To be more specific, the new rule is that a child shall board the airplane in the same round as one of his/her mother/father. If the bus has only one empty seat and could not transfer a child along with his/her parent, we should arrange the child and his/her parent onto the next round and let the next available passenger board the shuttle bus (you need to think carefully what *available* means). 

You should finish this task in `bonus.py`. Finishing this task and passing all tests will give you an additional 20% in your overall score of this homework.

## Testing and Grading

In the `testcases` directory we provided you with some simple testcases for you to examine the correctness of your code. Those tests are pretty simple and naïve. Passing them does not guarantee that you will pass test cases in the auto-grader on your submission. **So read carefully about the specification and create your own reasonable testcase, and do not use the auto-grader as your debugging tool.**

To help your find out which part of your code may be wrong in hope to reduce the time consumption of you on this homework, each testcase will have a label indicating which task the testcase is focusing on. The label will be in the form of `m-n`. For example, the label `2-1` means this testcase is the 1st testcase aiming to test your implementation in task 2.

Good luck!

## Feedbacks

- If you find any mistake in this homework, please contact any of the authors directly. Any mistakes or typos will be corrected ASAP.
- Comments on this homework are always welcomed so that we could do better. You are also welcome to send us feedback anonymously if you like. Refer to the [course homepage](https://si100b.org) for feedback channels.

## Appendix A. Input and Output

We will test your program by giving a list of queuing passengers and other information to your program through the standard input(i.e. `stdin`), and your program shall output the name of passengers to the standard output (i.e. `stdout`) so that we could examine whether the program is correct or not. You can find some sample inputs and outputs in the `testcases` directory of your homework [repository](http://gitlab1.q71998.cn/homework-20s/homework-1).

You can test your program in a manner as the following code snippet in your shell:

```shell
$ python3 task1.py < testcase > output
```

where the input is in a file named `testcase` and the output of your program will be in a file named `output`.

The input format will be given in the format as below.

```
<flight-num> <passenger-num> <boarding-time>

<ordinary-lane-passenger-num>
<passenger1-arrival-time> <passenger1-name> <passenger1-flight-num>
<passenger2-arrival-time> <passenger2-name> <passenger2-flight-num>
...
<passengern-arrival-time> <passengern-name> <passengern-flight-num>

<priority-lane-passenger-num>
<passenger1-arrival-time> <passenger1-name> <passenger1-flight-num>
<passenger2-arrival-time> <passenger2-name> <passenger2-flight-num>
...
<passengern-arrival-time> <passengern-name> <passengern-flight-num>
```

Interpret the input following the semantics below. 

- Different tokens are separated by one or more white spaces;

- Every line of the input is ending with a single newline character, i.e. `\n`;

- The input is divided into three parts, and different parts are separated by an additional newline. The first one gives you some basic information about the flight. The second one gives you the list of passengers waiting in the ordinary lane. The third part will give you the list of passengers waiting in the priority lane. For task 1, the third part (and the last newline) is omitted;

- `<flight-num>` is a string that could uniquely identify a single flight out of your airport in which there is no white space (an example is `MU233`);

- `<passenger-num>` will give you the total number of passengers that will finally board the flight;

- `<boarding-time>` gives you the time when the boarding starts (in seconds). It is an integer;

- Each passenger list section is divided into two parts. The first part is a single number `<*-lane-passenger-num> `which is an integer indicating the number of passengers in the queue. The second one is lines of passenger entries that can give you information about passengers in the queue;

- `<passengerk-arrival-time>` is an integer indicating the arrival time (in seconds) of the passenger . A larger arrival time means that the passenger arrives later.

- `<passengerk-name>` is the name of the passenger, and you could assume that it uniquely identifies a passenger;

- `<passengerk-flight-num>` gives the flight number of a passenger in the same format as the `<flight-num>` ;

- You can assume that the list of passengers is in the time order of their arrival.

Your output should be in the following format:

```
<round1-departure-time>: <name-passenger1> ... <name-passengerm>
...
<roundn-departure-time>: <name-passenger1> ... <name-passengerm>
```

where

* output shall include $n$ sections and different sections shall be separated by a single newline (i.e. `\n`) where $n$ is the number of rounds that your program thinks it will take to finish the process;
* every section should include the departing time of the bus for this round and a list of passengers in the round. The list should be ordered by the order of the passenger arriving at the gate (i.e., get onto the bus). Every element in this section should be separated by a single space. No additional space is allowed at the end of the section;
* `<roundk-departure-time>` should give the departure time of this round;
* `<name-passengerk>` should give the name of a single passenger in the round.


