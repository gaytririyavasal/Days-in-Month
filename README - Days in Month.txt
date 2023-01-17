PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

A decision tree provides a systematic approach to addressing a question when there are multiple factors in making the decision.

Note that a decision tree is typically drawn growing downward, unlike a real tree. The top node of the tree is called the "root node." Nodes (decision nodes) inside the tree, including the root node, have associated questions and at each decision node you follow one branch depending on the answer to that question. Each node at the bottom of the tree is called a "leaf node" and represents a final decision.

An alternative representation of a decision tree is a decision table showing possible outcomes given possible inputs. Below is the table that might represent the decision tree in the graphic. This table is "complete" in that it contains all eight possible combinations of values of the three input variables. But not all decision tables are complete in this sense; they may leave out certain combinations of possible inputs.

Free Coffee	Salary	Commute	Accept
Yes	<$50K	>1.0hr	No
Yes	<$50K	≤1.0hr	No
Yes	≥$50K	>1.0hr	No
Yes	≥$50K	≤1.0hr	Yes
No	<$50K	>1.0hr	No
No	<$50K	≤1.0hr	No
No	≥$50K	>1.0hr	No
No	≥$50K	≤1.0hr	No

It's often possible to build a tree that is more "efficient" than just naively implementing the decision table. For example, notice that the decision tree in the graphic doesn't contain eight leaves, as it might in a naive implementation of the corresponding table. In particular, if the salary is too low, we don't care about the commute or whether the company offers free coffee, so it would be a waste of time to ask those questions if we take the "no" branch from the first node. Notice also that we don't necessarily perform tests in the same order they appear in the table. It might be less efficient to put certain tests at the "root" of the tree.

It's pretty easy to write a computer program to implement a decision tree. Each place the tree "branches" write an if-else or if-elif-else statement that does one of the choices depending on the value of the condition. Each leaf node gives an answer.

Here is a possible implementation of the decision tree in the graphic:

if salary < 50000:
   accept = False
elif commuteInHours > 1.0:
   accept = False
elif freeCoffee:
   accept = True
else
   accept = False

where the variables like salary, commuteInHours, and freeCoffee would have been set prior to this code, perhaps with input statements or via some computation.

Assignment:

Your assignment is to implement a decision tree represented by the following decision table. The question to answer is whether a specific individual buys a computer. The inputs to the decision process are the age of the individual, her income level (high, medium or low), whether she is a student, and her credit rating. Under the given combinations of inputs, the last columns tells us whether the individual buys a computer.

Age	Income	Student	Credit	Buys
<=30	High	No	Poor	No
<=30	High	No	Good	No
31..40	High	No	Poor	Yes
>40	Medium	No	Poor	Yes
>40	Low	Yes	Poor	Yes
>40	Low	Yes	Good	No
31..40	Low	Yes	Good	Yes
<=30	Medium	No	Poor	No
<=30	Low	Yes	Poor	Yes
>40	Medium	Yes	Poor	Yes
<=30	Medium	Yes	Good	Yes
31..40	Medium	No	Good	Yes
31..40	High	Yes	Poor	Yes
>40	Medium	No	Good	No

Notice that this table is not "complete"; there are possible combinations of inputs that are not represented by rows in the table. For example, we can't tell from the table whether a 25 year old non-student with low income and bad credit will buy a computer; probably not. But that's good for us because we can optimize our algorithm by ignoring such cases (called "don't cares"). Your algorithm only has to work for the cases in the table; for don't cares you are free to return either answer.

For this problem, it is possible to define and implement a fairly simple decision tree, depending on the order in which you ask the questions. (My solution had 15 total lines of code, not counting comments and blank lines, including the four input lines; I could have done it in 12 lines, but wrote straightforward code.) You will be judged on whether your program gives the correct answers (the final column) for the cases in the table, not for the efficiency of your solution. But it will pay you to think about how to order the tests. Be sure to test your code for most, if not all, of the 14 lines of the table.

You can assume that the user enters legal answers in response to the four input statements. Your program does not have to behave correctly if the values provided are not legal.

Below are some sample runs of the program showing the desired output:

> python decisionTree.py

Please enter person's age: 25
Person's income (High, Medium, Low): High
Is this person a student (Yes or No)? No
Does this person have good credit (Yes or No)? No

This person will not purchase a computer.

> python decisionTree.py

Please enter person's age: 35
Person's income (High, Medium, Low): Low
Is this person a student (Yes or No)? Yes
Does this person have good credit (Yes or No)? Yes

This person will purchase a computer.

> python decisionTree.py

Please enter person's age: 50
Person's income (High, Medium, Low): Medium
Is this person a student (Yes or No)? No
Does this person have good credit (Yes or No)? No

This person will purchase a computer.

> python decisionTree.py

Please enter person's age: 25
Person's income (High, Medium, Low): Low
Is this person a student (Yes or No)? No
Does this person have good credit (Yes or No)? No

This person will not purchase a computer.

>

Notice that the last example tested a combination of inputs not in the table. Either answer would have been acceptable.
