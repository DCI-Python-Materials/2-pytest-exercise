#   TDD pytest

## Objectives
the participants will learn:
- more practice on the usage of pytest
- Error types
    - no parameter passed to function
    - wrong parameter datatype 

## install pytest
    pip install pytest

## run test command
    python3 -m pytest tests

## code file text/tools.py
## test file tests/test_string/test_tools.py

## Tasks:
### task1:
why test 2,3,4 and 6 will fail and how to fix them so they will pass?
### task2:
write a function called word_count which will take one string parameter 
it should return the numbers of the words on the given string parameter
### task3:
write test for the previous function which should check the following cases:
- no parameter passed
- wrong parameter datatype
- wrong output

## very important notice:
the code should be written in a way to be testable like break it down into functions instead of writing the code in a big bunch of one unit 
