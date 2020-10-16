# SI 100B Homework 4: yourSQL

* **Author**: Zihao Diao \<diaozh@shanghaitech.edu.cn\>, with contribution from Longtian Qiu \<qiult@shanghaitech.edu.cn\>
* **Supervised, proofread, edited and approved** by Prof. Yue Qiu \<[qiuyue@shanghaitech.edu.cn](mailto:qiuyue@shanghaitech.edu.cn)\>.
* **Proofread and calibrated** by Ziqi Gao \<[gaozq@shanghaitech.edu.cn](mailto:gaozq@shanghaitech.edu.cn)\> and Qifan Zhang \<[zhangqf@shanghaitech.edu.cn](mailto:zhangqf@shanghaitech.edu.cn)\>.
* **Last Modified**: May 1, 2020
* **Release Time**: May 4, 2020
* **Deadline**: 23:59:00 May 21, 2020, China Standard Time (UTC+8:00)
* **Latest Version**: [[HTML]](https://si100b.org/content/hw/hw/) [[PDF]](https://si100b.org/content/hw/hw4/si100b-sp20-hw4-spec.pdf) [[Template Codebase]](http://gitlab.q71998.cn/homework-20s/homework-4) [[off-campus Template Codebase]](http://gitlab1.q71998.cn/homework-20s/homework-4)

## Introduction

SQL, or Structured Query Language, is a language widely used to manage data stored in the relational database management system (RDBMS). Its usage spans from scientific computing and statistic applications to the building of your daily web applications like online shopping. 

The underlying principle of an RDBMS is quite simple. A typical *database* consists of one or more *tables*. Each *table* is just like the table in your spreadable application (like Microsoft Excel or Apple Numbers) in which it has a list of rows of data and each column of data has a name.

In this homework, you are required to design a simple database called yourSQL in the Python programming language which supports a subset of SQL. This homework will involve your knowledge of file reading and writing, object-oriented programming skills, and iterators. Let's get started!

## Getting Started

To get started, please simply fork the [repository](http://gitlab1.q71998.cn/homework-20s/homework-4) on GitLab and follow the structure and submissions guidelines below and on Piazza.

Remember to **make your repository private** before any commits.

*Note*: Markdown text with file extension ***.md*** could be displayed properly using plug-ins in your browsers, IDEs or specialized markdown editors (like [typora](<https://typora.io/>)).

## Repository Structure

### README.md

Homework description and requirements.

### testcases

Some simple CSV files for testing the correctness of your program.

### test.py

Some facilities and simple test cases for testing the correctness of your program.

### yoursql.py

You need to fill in your answer code in this file. You should only submit this file.

## Submission

**You should check in yoursql.py to GitLab.**

First, make a commit and push your files. From the root folder of this repo, run

```sh
git add yoursql.py
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

Every submission will create a new GitLab issue, where you can track the progress.

## Regulations

- You may **not** use third-party libraries.
- No late submissions will be accepted.
- You have 30 chances of grading (i.e. `git tag`) in this homework. If you hand in more than 30 times, each extra submission will lead to 10% deduction. In addition, you are able to require grading at most 10 times every 24 hours.
- We enforce academic integrity strictly. If you participate in any form of cheating, you will fail this course immediately. **DO NOT** try to hack GitLab in any way. You can view the full version of the code of conduct on the course homepage: https://si100b.org/resource-policy/#policies.
- If you have any questions about this homework, **please ask on Piazza first** so that everyone else could benefit from the questions and the answers.

## Specification

### Task 0: Build up Your Infrastructure

Data in RDBMS is usually organized as multiple *tables*. A single table usually consists of zero or more *rows* of data. Each one (called column) of those rows of data is usually named with a string that could be used for query (every row is just like the `dict` object in Python). In this part you are required to implement two Python classes that will be used in later tasks. This part will account for 60% of your overall score of this homework.

#### Row()

In this part, you are required to implement a Python class `Row()` which is used to store a single row of data in the table. As mentioned above, a single row in the table is very similar to a dictionary data type that you are familiar with in Python. It contains a fixed amount of data fields (columns) and all those columns are named with a key so that you can obtain the data stored in those columns with the key. 

Despite those similarities, there are some differences between your `Row()` object and a Python `dict`. The first is that `Row()` should have a primary key. The primary key is a single key in the row which will be used to uniquely identify a row in a table (which means the data stored in this column is unique in a table). Also, your `Row()` object should order the data fields with their keys in lexicographically ascending order regardless of what order we insert the data into the `Row()` object is.

What we are doing in this part is defining some custom data models in Python. If you are not familiar with this, read more: https://docs.python.org/3.7/reference/datamodel.html.

* `__init__(self, keys, data, primary_key=None)`: In this method, you should initialize your `Row()` object. The `keys` and `data` arguments are the Python list object. They are representing the keys and data in this row. To be more specific, the `i`-th element in `data` is the corresponding data field of the `i`th element in `keys`. The argument `primary_key` defaults to `None`. It indicates the primary key of the row. If it is set to `None`, use the first field in `keys` as the primary key. Otherwise, use the given string value as the primary key. Raise `KeyError` if the `primary_key` is not in the row.

  You can choose any way you want to store the data and keys in your implementation as long as they are not directly accessible from outside (because you do not want them to be modified by someone else!). Also, since the argument `keys` and `data` are all mutable object, you are expected to take measures so that changing the `keys` and `data` passed in will not affect the integrity of your row object.

  To improve the robustness of your implementation, you should raise an exception if any of the following situations occurs:

  * The arguments are of illegal types (raise `TypeError`);

  * The `keys` and the `data` are of different length (raise `keyError`);
  * The `keys` or the `data`  contains no element (raise `ValueError`).

* `keys(self)`, `get_primary_key(self)`: Return the keys in the `Row()` as a list in ascending order and return the primary key as a string respectively. Your implementation should ensure that changing the returned list of keys will not affect the integrity of the row.

* `__getitem__(self, key)`, `__setitem__(self, key, value)`: the data fetch and set methods. When called, they should return the item corresponding to the `key` or set the item corresponding to the `key` with `value` respectively. You should raise `KeyError` when the `key` does not exist.

* `__iter__(self)`, `__next__(self)`: Implement an iterator on the row. You should be familiar with those two methods. What we need to mention is that your iterator should return a single key each time in the row in lexicographically ascending order. Your iterator may be used multiple times and every time we call it, it should give consistent result;

* `__lt__(self, other)`: Compare `self` with `other`. Return `True` if and only if `self`'s field corresponding to the primary key is less than `other`'s (i.e., as pseudo-code, `self[self.get_primary_key()] < other[self.get_primary_key()]`). Your implementation should raise `TypeError` if `other` is not `Row()`-typed or `self` and `other` have different sets of columns (keys) or their primary keys are not the same. The method will be useful when you are sorting your rows in your `Table()` implementation using `storted()`;  

* `__len__(self)`: Return the number of columns in the row.

* Feel free to define other methods and helper classes you like.

Once you finish your implementation, you can test it in your interactive Python interpreter as follow:

```python
>>> from yoursql import Row
>>> row = Row(["a", "b", "c"], [1, 2, 3])
>>> [(i, row[i]) for i in row.keys()]
[('a', 1), ('b', 2), ('c', 3)]
```

#### Table()

As we mentioned above, a table usually consists of multiple rows. Those rows in a table must have the same set of columns. In this task, you are going to build your `Table()` object.

The `Table()` object should read in the table from a comma separated value (CSV, usually `.csv`) text file and divide the table into rows so that you can do some operations in the following tasks. The CSV file usually contains multiple rows. Every row has multiple columns of fields. In a row, different fields are separated by a single comma (`,`) and zero or more spaces before or after it. Each row of data ends with a `\n` in Python. You should ignore the empty lines in the file. The first row in the CSV file is the header, which gives the corresponding keys to each of the columns. An example of a CSV file is given below. The files given to you in testcases are all encoded with `utf-8` and they do not have empty columns (empty columns will occur when two commas have no data or have purely spaces between them. e.g.,  `,,`).

For example,

```csv
id,name,school,major,gpa
23456123,Li Xiaoming,SIST,CS,3.98
45280742,Ge Ziwang,SPST,PHY,3.76
12567923,Wang Dachui,SLST,BIO,4.00
```

The corresponding table is

| id       | name        | school | major | gpa  |
| -------- | ----------- | ------ | ----- | ---- |
| 23456123 | Li Xiaoming | SIST   | CS    | 3.98 |
| 45280742 | Ge Ziwang   | SPST   | PHY   | 3.76 |
| 12567923 | Wang Dachui | SLST   | BIO   | 4.00 |

* `__init__(self, filename, rows=None, keys=None, primary_key=None)`: Initialize your `Table()` object in this method. `filename` will be the relative path to your current working directory to the CSV file you should read in. The file will always be available in the file system.  `primary_key` is the primary key (as we have described in `Row()`) all your `Row()`s should use. Raise a `KeyError` if `primary_key` does not exist in the table. You are allowed to design your own internal structure of this object as long as your attributes are not accessible from outside.

  Your `__init__()` should support two approaches to construct the `Table()` object. The first one is from a file. This approach should happen when the fourth argument `rows` is set to `None`. You should read in the table from the CSV file as specified in `filename`.The file that you will read in is always guaranteed to exist in your file system. The second one is from multiple rows. This should happen when `rows` is set to an iterable that contains a number of instances of the `Row()` object and `keys` is set to a non-empty list of keys in your table. In this case, you should construct your `Table()` object from those rows and you are not supposed to read the file as specified by `filename`. The primary key of the table is then the first element of `keys` unless specified by `primary_key`. Those two argument should be ignored if only one of them is presented. 

  As you may have noticed, the data fields you read from the CSV file are all strings. It is not convenient to use strings to perform some operations in the following tasks. So you should convert all numeral fields into an integer or floating number before storing them into the rows. The rules for the conversion is simple: you should convert the numeral fields into an integer one if it is representable using an integer (e.g., `1`, `12345678`) otherwise, it should be converted to a float-typed one (e.g., `1.0`, `3.1415926`). You are not excepted to do the conversion when constructing from multiple `Row()` objects;

* `keys(self)`, `get_primary_key(self)`: The same as `Row()`. Return the keys in the `Table()` as a list in an ascending order and return the primary key as a string respectively;

* `get_table_name()`: Return the table name of the table. The table's name is the `filename` argument in `__init__()`

* `__getitem__(self, key)`: Index the table by the primary key. This method should return the row with the data field corresponding to the primary key equals to `key` as a `Row()` object (i.e., `Row()[Table().get_primary_key()] == key`). Raise `ValueError` if the table does not contain such a row. You are not expected to return a copy of the row since we want any modification on the row being reflected in the table (think about why);

* `__iter__(self)`, `__next__(self)`: Implement an iterator on the table. Your iterator should return rows as `Row()` objects in the lexicographically ascending order of the primary key. Your iterator is going to be called multiple times;

* `__len__(self)`: Return the number of rows in the table.

* Feel free to define other methods or helper function (classes) you like.

Once you finish your implementation , you can test your implementation in a manner as below:

```python
>>> from yoursql import Table
>>> table = Table("testcases/student.csv")
>>> table[12567923]
<yoursql.Row object at 0x10a955908>
>>> [row['name'] for row in table]
['Wang Dachui', 'Li Xiaoming', 'Ge Ziwang']
```

### Task 1: Query on Single Table

Now your toy database supports loading data into your memory and some simple data retrieving and modification interface. Now you are going to implement some more complex queries on a single table.

There is a widely used domain-specific language (DSL) called SQL in both academia and industry specifically designed to specify a data query in relational databases. However, parsing this language requires some techniques that go beyond the scope of this course. So, we will present the query in a structured manner to you.

We are presenting to you the queries as a Python dictionary. The dictionary contains three parts. The first part is a list of the columns we want to preserve in the result under the key `'select'`. The second one is the list of the conditions under the key `'where'`.  The last part of the query is the file(s) we want to query from under the key `'from'`.  

* The list of columns (keys) should all present in the result table. If any one of them does not exist, a `KeyError` should be raised;

* The list of conditions under `'where'` contains several tuples. Each tuple contains three items. The first item is a key. The second one is a value that we want to test the key on. The last one is the operator. The keys presented in the condition list should be in the table. Otherwise, raise `KeyError`. The operators are strings in the format and semantic of the Python conditional operators. Possible operators are `==`, `>`, `<`, `>=`, `<=`and `!=`. Every two clauses should be joint by an `and` operator (i.e., we only support CNF). If the condition list is empty, you should include all the rows in your result.

  For example, `[('gpa', 4.0, '>'), ('school', 'SIST', '==')]` should be parsed as `row['gpa'] == 4.0 and row['school'] == 'SIST'`. 

An example of the query will be 

```python
query = {
  'select': ['id', 'school', 'name', 'major'],
  'from':  'student.csv',
  'where': [('gpa', 4.0, '==')],
}
```

The query will return all the students with GPA equals to 4.0 and their student ID, school and major from the table in `student.csv`.

Your implementation of the query should be in the class `Query()` .

* `__init__(self, query)`: Do the query. `query` is a single query we've described above;
* `as_table(self)`: Return the result of the query as a new `Table()` object named with the original table name in query and copies of the rows in the original object (i.e., any modification on the new table could not affect the original table). If the primary key is not presented in the `select` field, you need to explicitly add it to the table;
* Feel free to define any other methods to help you to reuse your code.

You could test your implementation using the routines provided in `test.py`. This task will account for 10% of your overall score of the homework.

### Task 2: Join Operation

Often in practice, we would like to store the data in multiple tables. This is for the consideration of flexibility of design and also for saving the space. Yet it is a common use case for us to *jointly* look up two or more tables. Here comes the need of supporting the JOIN operation.

Consider two tables, `student.csv` which stores the student's name, ID, and school and `gpa.csv` which stores the GPA and ID of students. Those two tables are intended for storing the same set of information as the one in task 1.  With join operation, you can *recover* the table we presented in task 1.

**`student.csv`**

| id       | name        | school | major |
| -------- | ----------- | ------ | ----- |
| 23456123 | Li Xiaoming | SIST   | CS    |
| 45280742 | Ge Ziwang   | SPST   | PHY   |
| 12567923 | Wang Dachui | SLST   | BIO   |

**`gpa.csv`**

| id       | gpa  |
| -------- | ---- |
| 23456123 | 3.98 |
| 45280742 | 3.76 |
| 12567923 | 4.00 |

After joining on those two tables, we will get the following one, which is identical to the table we presented in task 1 except for the field names.

| student.id | student.name | student.school | student.major | gpa.gpa |
| ---------- | ------------ | -------------- | ------------- | ------- |
| 23456123   | Li Xiaoming  | SIST           | CS            | 3.98    |
| 45280742   | Ge Ziwang    | SPST           | PHY           | 3.76    |
| 12567923   | Wang Dachui  | SLST           | BIO           | 4.00    |

More formally, the join operation consists of two steps. The first one is to do a [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product) over two tables. For example, if your have two tables $A$ and $B$  where $A = \{(a, 1), (b, 2)\}$ and $B = \{1, 2\}$ then $A \times B = \{(a, 1, 1), (a, 1, 2), (b, 2, 1), (b, 2, 2)\}$. As you could imagine, the operation in the first step may create some undesirable results. For example, in our student-GPA join example, after the first step, every student will have 3 rows with 3 different GPAs. Those GPAs are in fact for some other students instead of the given one. Then we need the second step, filtering. In this step, those inconsistent rows are filtered out. In this homework, the filter operation goes on the primary key. That means you should only preserve the rows where the primary keys of two different rows are identical. In fact, there are many types of join operations that exist in an actual database. However, in this homework, you are asked to only implement the simplest one as we described above.

Your implementation should be in the  `JoinQuery()` class. You may have noticed that the class is inherited from the `Query()` class. This means you should provide identical interfaces for those two classes. The only difference lies in the format of the query. In this class, all the queries will contain two tables in a tuple under the key `'from'` of the query dictionary. Also, in your result table, you should prefix the fields with the filename (exclude the extension `.csv`) and a single `.`. For example, the `id` field of a row in the `student.csv`  table will be renamed to `student.id`. The new primary key of the join table should be any one of the primary key of the two old tables. The fields in a row should be ordered in lexicographically ascending order. The rows should be ordered in the lexicographically ascending order of the primary key. For simplicity, the exported table of this query will be named as `join.csv`.

Your implementation should also support filtering. Yet the filter operation is done after the join operation so the field name will be the prefixed one. You only need to implement the join operation over two tables.

An example of the query will be 

```python
query = {
  'select': ['student.id', 'student.school', 'student.name', 'student.major'],
  'from':  ['student.csv', 'gpa.csv'],
  'where': [('gpa.gpa', 4.0, '==')],
}
```

The query will do the same thing as in task 1 but this time the query is over two separate tables.

This task will account for 20% for your final score of this homework.

### Task 3: Data Exportation

Persistent storage is very important for DBMS. No application wants to use a DB that lives only on memory and will disappear after power been cut off to store important information (despite we have some DB that relies only on memory. But those DB are for caching and speeding up purpose and usually is not for storing important information). The same rule will apply to your DB program.

 Sometimes, the user of your DB program may want to shutodwn his computer so exporting the data from a table to a file on disk for further reference is a necessary. Of course, they could do it by themselves. But it will be a great thing for you as the author of the program to provide an interface to export the table to a file.

Now in your `Table()` class, implement a method named `export()` allowing the exportation of the table to a file on the file system.

* `Table.export(filename=None)`: The method takes in one argument `filename`. It gives you the location where the file should be located. If the file exists at the time, overwrite the file. If it does not exist, create it breforehead. If the argument is `None`, overwrite the file where the table reads in from.

  Your exported table should also be a CSV one. The first row of the output file should be the column names. From the second row on, you should output the data rows. Every row is ended with a single `\n` (including the last row). Different fields in the same row should be separated by a single `,`. The order of fields in a row and between rows should be preserved (in ascending order).

This task will account for 10% for your final score of this homework.

### Bonus: Data Aggregation

You are going to implement data aggregation for your query. 

Sometimes you are going to query some quantity of groups of rows in the table. For example, if you are the staff from the Office of Academic Affairs and you are looking for the average GPA of students from SIST, SPST, SLST, and IMS. Of course he/she could filter out the students' GPAs from all four schools and use a Python program to calculate the average GPA of students. But if your DB program could help him/her to calculate the result with a single query, it will be great!

The operation we described above is called data aggregation formally. In this task, you are implementing a new class called `AggQuery()` which is inherited from `Query()` which allows some aggregation operations on tables.

#### Query Functions

The first thing you need to implement is the query functions. Those functions are pretty simple and could act on a column of data. For example, `AVG(gpa)` will calculate the average value of the `gpa` column of the table and replace all the field in this column with the calculated value in the result. The query function often lies in the `'select'` clause of the query. There is a list of functions you need to implement:

* `AVG()`: take the average value of the column;
* `SUM()`: sum up all the value of the column;
* `MAX()`: get the maximum value of the column;
* `MIN()`: get the minimum value of the column.

The `SUM()` function will only be applied to the columns that support arithmetic addition (i.e., `+`). The `AVG()` function will only be applied to the columns that support both arithmetic addition (`+`) and arithmetic division (`/`). The `MAX()` and `MIN()` function will only be applied to the columns that support comparison. 

For example, a query could be:

```python
 query = {
  'select': ['id', 'school', 'name', 'major', 'MAX(gpa)'],
  'from':  'student.csv',
  'where': [],
}
```

This query will find out the maximum value of all the GPA among all the students and replace the column with the value.

#### Aggregation

Now we are getting down to the real aggregation. Formally, aggregation requires you to perform an equality check on a column and merge the rows with the same value in the column. All other columns are all filtered with a query function.

For this task, we add another key to the query dictionary called `'group_by'`. In this field, we are giving you the field that we are doing aggregation on. Any other fields in `'select'` are wrapped with a query function. 

What you need to do is to first filter out the rows using conditions in `where` and then group the rows with the same value in the column given by `group_by` and then use the aggregation functions to calculate the values corresponding to the columns in the group. 

The result table should have all the fields named with the function name and the field name (e.g., `MAX(gpa)`). The new primary key of the result table exported from the query will be the column you are `group_by` with. You are not required to do join operations in this task.

For the average GPA example presented at the beginning of this task, the corresponding query will be:

```python
query = {
  'select': ['school', 'AVG(gpa)'],
  'from': 'student.csv',
  'group_by': 'school',
  'where': [],
}
```

## Note on Implementation

Relational database is a quite complicated thing to implement in reality to achieve full functionality and high performance. Some parts of the SQL language's semantics are even different from Python or any other languages (an example is how they deal with Boolean variables). In this homework we only select a part of the functionality of SQL.

Your implementation should be quite simple and naïve. When testing your program, we will not use testcases that cause your program to time out or run out of memory if not using some fancy algorithms. So you are not asked to implement those complicated algorithms (e.g., external merge sort or block nested loop join). All you need to do is following the semantic we give in the specification and submit a simple and naïve implementation.

If you are interested in this topic, you can select the CS 150: Database & Data Mining course from SIST in your junior or senior year.

## Testing and Grading

In the `testcases` directory,  we provided you with some simple testcases for you to examine the correctness of your code. Those tests are pretty simple and naïve. Passing them does not guarantee that you will pass testcases in the auto-grader on your submission. **So read carefully about the specification and create your own reasonable testcases, and do not use the auto-grader as your debugging tool.**

The auto-grader will test your code by importing your module and test it in a similar manner to `test.py` once you tagged a commit on Gitlab.

To help your find out which part of your code may be wrong in hope of reducing the time consumption of you on this homework, each testcase will have a label indicating which task it is focusing on. The label will be in the form of `m-n`. For example, the label `task2-1` means this testcase is the 1st testcase aiming to test your implementation in task 2.  Since the test cases are compositional and latter tasks may depends on your implementation of former tasks, **you may also needs to check your code in tasks other than the one the grading label gives if your module fails any of the test cases**.

Good luck!

## Feedbacks

- If you find any mistake in this homework, please contact Zihao Diao via email (diaozh@shanghaitech.edu.cn) directly. Any mistakes or typos will be corrected ASAP.
- Comments on this homework are always welcomed so that we could do better. You are also welcome to send us feedback anonymously if you like. Refer to the [course homepage](https://si100b.org) for feedback channels.