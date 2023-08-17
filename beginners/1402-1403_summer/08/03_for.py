# for 

"""
repetition statement


# int i=0 | initial statement
# i<10 | condition statment/control statement
# i++ | increamental/decremental/step

Java, C
for (int i=0; i<10; i++){
    # for body
}

Flow Chart
https://en.wikipedia.org/wiki/Flowchart
https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/For_loop_example.svg/170px-For_loop_example.svg.png


[initial state]
        |
        v
[control state] <----
        |           |
        v           |
       item         |
      [body]        |
        |           |
        v           |
    [step state]----|


loop over iterator

iterator حلقه زد
iterable قابلیت حلقه زدن

iterable: list, iterator

for-each java
"""

my_list = [1, 2, 3, 4]
# list: iterable
# iter: iterator

for item in my_list:
    # item: 1
    # item: 2
    # item: 3
    # item: 4
    print(item * 2)


# my_list: [1, 2, 3, 4]
# iterable: my_list
# iterator = iter(iterable)
# next(iterator)
# 
for item in my_list:
    # item: 1
    # item: 2
    # item: 3
    # item: 4
    print(item)