# Week 11

## Thore a)

> Bob is a runner. He has been running 4 km every day of the week, except in the week-ends. What is the worst case number of kilometers he runs per day?

Depends on how we look at it, but i would say the highest is the worst, so 4km.

> He started this new workout schedule on a Saturday. What is the amortised number of kilometers he runs per day?

Well there are 2 weekdays where he doesn't run, making it 
$$
\frac{4\cdot 5}{7}=2.8
$$

## Thore b)

> Ran is also a runner. He rolls a die every morning and runs as many kilometers. (i) What is the expected number of kilometers Ran runs per day, assuming he has a perfect die?

By definition of a perfect die, there would be the same change it lands on either side, therefore the average number would be:
$$
\frac{1+2+3+4+5+6}{6}=3.5
$$
So Ran is expected to run, on average, 3.5 kilometers pr day.

> What about enchanted dice that always come up 1

I mean, 1 kilometer pr day, it's always the same. Therefore constant

> Cursed dice that always come up 6

6 kilometers pr day.

> What is the worst-case number of kilometers Ran runs per day

6 kilometers, that is the highest number available.

> For any sequence of days starting on a Saturday, what is the worst-case amortised number of kilometers Ran runs per day?

The absolute worst case would be getting 6 every day.

## Thore c)

> My phone company charges 10 DKK for 1 minute of voice call. This is exorbitant, but I never use my phone for making a phone call anyway. According to the contract, I have to pay at least 100 DKK per month for voice calls whether I use them or not, but the contract automatically ‘rolls over’ the unused minutes to the next month. I have to call my mum for Christmas for a 2-hour call. Describe the expense in terms of ‘money I spend on voice calls each month’ in the worst case and in the amortised sense

The question states that he never makes phone calls, except for a 2 hour long one on christmas. That would mean that for every month there are 0 call hours, which is 0 minutes, therefore 0 DKK, apart from the 100 DKK he pays.

The worst case then is the december call where he makes a 2 hour long phone call. Because of the 100DKK, every month he makes up 10 minutes of call, which is 120 minutes total, meaning that he pays a constant amount every single month, no matter the phone call in december. Making the amount of money spent constant.

## Thore d)

> A multiride ticket in the Danish amusement part Tivoli costs 200 DKK and is valid for 10 rides. What is the worst case cost for a single ride?

The single cost for a ride would then be 
$$
\frac{200}{10}=20
$$
Which is also the constant cos for a ride. The amortised cost must then also be 20.