# Motivation
As part of the Computer [Science Bootcamp](https://codigofacilito.com/bootcamps/ciencias-computacionales/pdfs) from [codigo facilito](https://codigofacilito.com/).
While in the third class of **Calculations**, a review of how **regular expressions** work was presented, even though there are multiple types of implementations for them, 
in this occasion we will explore the implementation by using **state machines**. 

# Explanation
For this exercise, the following situation is considered:
A company wants to validate the input of a form in a web page for a specific email structure, this in order to assure that the person filling the form is part of the company.
For now, only the structure of the email is evaluated, other measures such as password, MFA, etc. are not being considered.

Corporate emails are composed as follows:
> C_anaya@evilcompany.com

These emails are formed with:
- The first uppercase letter of the first name
- An underscore
- Last name in lower case
- Domain of the company

Whenever a new collaborator is hired, promoted or sent to another business area a new emails are issued,
this can cause the emails generated to collide.

I order to avoid this, a number is added after the last name and before the @ symbol.

Create a method based in a regex state machine in order to validate that the email belongs to the company.

# State Machine Diagram
This is the state diagram for the regex, steps can be described as follows:

- S0: Initial state, input is received and the first letter must be an upper case letter from A to Z
- S1: State one, an underscore must be present in the input
- S2: State two, here the last name is validated, the last name must contain any combination between lower case a to z
- S3, S4: State three, State four, in these states, a digit is received.
- S5: State five is only achieved if an *@* symbol is received this indicates the start of the domain of the email
- S6 to S20: State six to State twenty, this states only makes sure that the domain *evilcompany.com* is accomplished character by character

This procedure gives us a total of 21 states in order to cover the flow of the regex
![State Machine Diagram](src/state_machine.svg)

Any non-fulfilling condition in the flow will result in an error state -1, for easier readability, links of some states where not drawn,
however it can be stated that any non-continuation or not fulfilling condition will result in this error state.

Getting into the error step will result in the interruption of the entire flow.
![State Machine Diagram with Errors](src/state_machine_failure.svg)

# Pseudocode
In order to translate the state machine diagram into a programming language, is recommended to first translate into pseudocode.
The interpretation of the pseudocode can be thought as follows:

Initialization of state machine:
~~~
state = 0
~~~

Flow function, will help with the state change:
~~~
function flow(char)
    if state equals 0  and char is between [A-Z]
        state = 1
    else if state equals 1 and char equals _
        state = 2
    else if state equals 2 and char is between [0-9]
        state = 3
    else if state equals 3 and char is between [0-9]
        state = 4
    else if state equals 2 or 4 and char equals "@"
        state = 5
    else if state equals 5 and char equals "e"
        state 6
     ... (This will repeat for every character on the string "evilcorporation.com")
     else if state equals 19 and char equals "m"
        state 24
    else
        state = -1
~~~
Validation function, this functions calls the flow function in order to check if the final result of the regex was correct.
~~~
function validate(element):
    if element equals 24
        return true
~~~
Processing the string function for each character in the string, if the evaluated state results in -1, the cycle will break meaning that the regex was not fulfilled
~~~
function process(object):
    for element in object
        state = flow(element)
        if state equals -1
            break cycle
    return validate(element)
~~~