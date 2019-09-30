# Class5

In previous classes we saw how to perform a loop for a finite number of times. In this class we will see how to perform the loop indefinitely, while some condition is matched.

- [Class5](#class5)
  - [While loop](#while-loop)
    - [Notes about the while loop](#notes-about-the-while-loop)
  - [Example](#example)
  - [Exercise](#exercise)

## While loop

The *while* loop is responsible to accomplish infinite loops. the syntax is the following:


**Warning**:If you execute this code, it will run without stopping
```python
condition = True
while condition:
    print('hello world')
```

The while loop can is used when we don't know when the exit condition will happen, or when we don't know how exactly how many times we have to perform the loop. This is particular useful when working with text files, spreadsheets, etc., because we don't know how many lines or rows we have in the file.

### Notes about the while loop

1.Since the *while* will run while the condition is matched, we may wnd up with programs that will never end. For this reason, we usually think about the *exit condition* before start working on the main feature.
2.Loops are also used to develop IOT devices, raspberry pi, arduino, mobile apps (implicitly), user interfaces (implicitly),etc. For this reason, it's important to get familiar with this concept, and how it works.
3. Inside a *while* statement, we can use the keyword *break* to exit the loop.



## Example

We are going to create a simple calculator that will add numbers. When we type 0, the program will who us the sum, and exit the program

```python
answer = None
sum = 0
# is not means the same as not ==
while answer is not 0:
    answer = int(input('type a number: '))
    sum = sum + answer
    
print(sum)
```

## Exercise

Still using the example of the number of cups of coffee, You have to update it to keep asking for the numbers of cups taken, until the number is negative. Then, you have to print the following information:

- Name of user
- Total number of days
- Total number of cups
- Average number of coffees per day
- Message based on the average number of coffees per day (same from the previous classes)