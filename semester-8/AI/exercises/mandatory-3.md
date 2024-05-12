---
title: "Mandatory 3"
author: Albert Rise Nielsen (albn@itu.dk)
---

## Formulate the state and action space

The state space is the cars in location $L_1$ and $L_2$, $C_1$ and $C_2$ respectively.
Therefore the state is $S = (C_1, C_2)$, where $0 \leq C_1\leq 20 \text{ and }, 0\leq C_2 \leq 20$.

The action space is the number of cars to move from $L_1$ to $L_2$ and $L_2$ to $L_1$. We can denote the action space as $A = (a_1, a_2)$. Where $a_1$ is the number of cars from $L_1$ to $L_2$ and $a_2$ is the number of cars from $L_2$ to $L_1$.

## Define the transition function and reward function

The transition function is the probability of moving cars from $L_1$ to $L_2$ and $L_2$ to $L_1$. Denote the transition function as $T(s'|s, a)$ as the probability of reaching state $s'$ executing $a$ in state $s$.

In our case we move cars from $L_1$ to $L_2$ always if $L_1$ has more than 3 cars and $L_2$ has less than 20 cars. This is because $L_1$ will always get the 3 cars it rents out back, and $L_2$ will continously lose cars, so to maximise the reward we must continously move cars from $L_1$ to $L_2$. Therefore the transition function is:

$$
    P((C_1-a_1,C_2+a_1)|((C_1-a_1)>3,(C_2+a_1) \leq 20),(a_1,0)) = 1
$$

Where $a$ is the number of cars to move from $L_1$ to $L_2$. In all other cases the transition function is 0.

The reward function is the profit of renting out cars and the cost of moving cars. Denote the reward function as $R(s,a, s')$ as the reward of executing $a$ in state $s$ and reach state $s'$.

The reward function at the end of the day is the profit of renting out cars and the cost of moving cars. The profit of renting out cars is $10 \cdot \min(C_1,3) + 10 \cdot \min(C_2,4)$. The cost of moving cars is $2 \cdot a$. The new state is $C_1 + a_2 - a_1$ and $C_2 + a_1 - a_2$. Denote as $C_1'$ and $C_2'$ respectively. Therefore the reward function is:
$$
    R((C_1,C_2),(a_1,a_2),(C_1',C_2')) = 10 \cdot \min(C_1,3) + 10 \cdot \min(C_2,4) - 2 \cdot (a_1+a_2)
$$

## Explain whether it is likely that cars will be moved from location 2 to 1, and whether it is likely that Jack can keep up with total rental demand without losing business 

It is very unlikely that cars are moved from $L_2$ to $L_1$. It's actually impossible since the transition function is 0 in that case.

Jack will be able to keep up with rental demand on $L_1$ for infinity, theoretically, since he will always get the 3 cars he rents out back. He will not be able to keep up with rental demand on $L_2$ since he will continously lose cars, 2 a day to be exact. Therefore it will probably take a while before he runs out of cars, especially since $L_1$ supplies him with it's cars as well, but it will continously approach 0 cars on $L_2$.
