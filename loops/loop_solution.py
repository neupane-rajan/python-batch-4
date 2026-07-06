"""
* * * * *
*       *
*       *
*       *
* * * * *

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0

"""

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


for i in range(5):
    for space in range(4 - i):
        print(" ", end=" ")
    for star in range(2 * i + 1):
        print("*", end=" ")

    print()
