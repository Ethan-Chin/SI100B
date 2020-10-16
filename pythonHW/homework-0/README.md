# SI 100B Homework 0: Submisstion Test

* Author: [Qi Qin](mailto:qinqi@shanghaitech.edu.cn)
* Last modified: Feb. 20, 2020
* Deadline: 23:59:59, Mar. 8, 2020 China Standard Time (UTC+8:00)

## Introduction

This is a dummy homework for you to get familiar with the GitLab grading system.

## Getting Started

To get started, please simply fork this Gitlab repository and follow the structure and submissions guidelines below.
Remember to **make your repository private** before any commits.

*Note*: Markdown text within ***.md*** files could be displayed properly using plug-ins in your browsers, IDEs or specialized markdown editors (like [typora](<https://typora.io/>)).

## Repository Structure

### README.md

Homework descriptions and requirements.

### test.py

A basic template for this homework you need to fill it in.

## Submission

**You should check in test.py to Gitlab.**

First, make a commit and push your files. From the root folder of this repo, run

```sh
git add test.py
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

- No late submissions will be accepted.
- You have 30 chances of grading (i.e. `git tag`) in this homework. If you hand in more 30 times, each extra submission will lead to 10% deduction. In addition, you are able to require grading at most 10 times every 24 hours.
- We enforce academic integrity strictly. **DO NOT** try to hack Gitlab in any way. You can view the full version of the code of conduct on [Course Webpage](https://si100b.org/resource-policy/#policies).
- If you have any questions about this homework, please ask it on Piazza first so that everyone else could benefit from your question and the answer.

## Specification

### Input & Output

* Your program takes no input;
* The output should be exactly the same as "Hello, SI100B!" with no leading or trailing spaces but a newline character at the end(it will be automatically added by `print` function).

Once you finish your implementation, test it in the console by

```sh
python3 test.py
```

You will see

```
Hello, SI100B!
```

if your implementation is correct.

## Feedbacks

* If you find any mistake in this homework, please contact with me ([Qi Qin](mailto:qinqi@shanghaitech.edu.cn)) directly. Any mistake and typo will be corrected ASAP.
* Comments on this homework is always welcomed so that we could do better. You are also welcome to send us feedbacks anonymously if you like.
