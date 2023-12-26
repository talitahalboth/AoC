## Advent of Code Solutions

### 2023

#### Day 1

Part 1 and Part 2: AD Hoc


#### Day 2

Part 1 and 2: Used regex to count matches

#### Day 12

Use a pd that stores the position in the row, positiong in the rules list, and number of used of current rule

#### Day 17

Part 1 and 2: djikstra, change the count


#### Day 18

Part 1: BFS

Part 2: important things to notice:
shoelace formula

to account for the walls:
if last direction was right and current is down, or other way around: the "outside" of the shape points ↗️ Northeast. 
Increase column by one.


if last direction was left and current is down, or other way around: the "outside" of the shape points ↘️ Southeast. 
Increase row and column by one.


if last direction was left and current is up, or other way around: the "outside" of the shape points ↙️ Southwest. 
Increase row by one.


if last direction was right and current is up, or other way around: the "outside" of the shape points ↖️ Northwest. 
Dont increase row nor column.

Use new row/columns for shoelace formula.

r,c are current row/columns, r0,c0 are previous.

h = (r + r0) / 2
w = c0 - c
a = h*w   
sum+=a 


#### Day 19

Part 1:  just follow the rules
Part 2: create ranges from 0..4001 and cut the ranges when needed

#### Day 20

Part 1: ad hoc, just follow the path until all signals were sent

#### Day 21

Part 1: simples bfs until dist is 64.

#### Day 22

Part 1: let each line fall 1 step at a time, until all blocks are either touching the ground or another block.
For each block (A), check if it supports anotehr block (B). If so, add it to the list of blocks that support it (add A to list of blocks that support B). Check all blocks that have a list of size one, add the block that supports it to a set. Size of the set is how many can't be removed. Print number of blocks - size of set.

Part 2: use list of blocks that support each block. Check for each one if it supports other blocks.

#### Day 24

Part 1: created end point for each vectpr outside of search area, used simple intersection point to check where they intersect. Afterwards, check it intersection point belongs to vector.

#### Day 25

Part 1: Min-Cut Max-Flow problem
