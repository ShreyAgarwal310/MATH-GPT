DECLARATIVE_THREE_SHOT = '''
Q: Mary had 5 apples. The next morning, she ate 2 apples. Then, in the afternoon, she bought as many apples as she had after eating those apples in the morning. How many apples did she end up with?

Peano solution:


Let a be the number of apples Mary started with [[var a]]. We have [[eq a = 5]]. 
Let b be how many apples she had in the morning after eating 2 apples [[var b]]. We have [[eq b = a - 2]]. 
Let c be the apples she bought in the afternoon [[var c]]. 
Since she bought as many as she had after eating, we have [[eq c = b]]. 
Let d be how many apples she ended up with [[var d]]. We have [[eq d = b + c]]. 
The answer is the value of d [[answer d]].





Q: Mario and Luigi together had 10 years of experience in soccer. Luigi had 3 more than Mario. How many did Mario have?

Peano solution:


Let a be the number of years Mario had [[var a]]. 
Let b be the number of years Luigi had [[var b]]. We have [[eq a + b = 10]]. We also have [[eq b = a + 3]]. 
The answer is the value of a [[answer a]].





Q: The planet Goob completes one revolution after every 2 weeks. How many hours will it take for it to complete half a revolution?

Peano solution:


Let a be the number of hours in a week [[var a]]. We have [[eq a = 168]]. 
Let b be the number of hours in a revolution [[var b]]. We have [[eq b = a * 2]]. 
Let c be the number of hours in half a revolution [[var c]]. We have [[eq c = b / 2]]. 
The answer is the value of c [[answer c]].





Q: {question}

Peano solution:
'''.strip() + '\n\n\n'



DECLARATIVE_THREE_SHOT_AND_PRINCIPLES = '''
Let's solve mathematical word problems in a careful, formal manner. The solution will follow the Peano format: 
1- Each sentence in the solution either introduces a new variable or states a new equation. 
2- The last sentence gives the goal: which variable will contain the answer to the problem. 
3- Each equation only uses previously introduced variables. 
4- Each quantity is only named by one variable.
5- Use all the numbers in the question.

Q: Minh spent $6.25 on five sticker books to give his nephews. Find the cost of each sticker book.

Peano solution:

Let a be the price of all the sticker books [[var a]]. We have [[eq a = 6.25]]
Let b be the number of sticker books [[var b]]. We have [[eq b = 5]]
Let c be the price of an individual sticker book [[var c]]. We have [[eq c = a / b]]
The answer is the value of c [[answer c]].

Q: Tom paid $1166.40 for a new refrigerator, including $86.40 tax. What was the price of the refrigerator?

Peano solution:

Let a be the price Tom paid for the new refrigerator [[var a]]. We have [[eq a = 1660.40]]
Let b be the sales tax Tom paid for the refrigerator [[var b]]. We have [[eq b = 86.40]]
Let c be the price of the refrigerator [[var c]]. We have [[eq c = a - b]]
The answer is the value of c [[answer c]].

Q: At a school concert, the total value of tickets sold was $1,506. Student tickets sold for $6 each and adult tickets sold for $9 each. The number of adult tickets sold was five less than three times the number of student tickets sold. How many student tickets were sold?

Peano solution:

Let a be the price for a student ticket [[var a]]. We have [[eq a = 6]].
Let b be the price for an adult ticket [[var b]]. We have [[eq b = 9]].
Let c be the total value of tickets sold [[var c]]. We have [[eq c = 1506]].
Let d be the number of student tickets sold [[var d]].
Let e be the number of adult tickets sold [[var e]].
Because the total value of tickets sold was $1506, we have the equation [[eq a * d + b * e = 1506]].
Because the number of adult tickets sold was five less than three times the number of student tickets sold, we have the equation [[eq e = 3 * d - 5]].
The answer is the value of d [[answer d]].

Q: Monica paid $8.36 for stamps. The number of 41-cent stamps was four more than twice the number of two-cent stamps. How many 41-cent stamps did Monica buy?

Peano solution:

Let a be the total price of the stamps [[var a]]. We have [[eq a = 8.36]]
Let b be the value of a 41-cent stamp [[var b]]. We have [[eq b = 0.41]]
Let c be the value of a two-cent stamp [[var c]]. We have [[eq c = 0.02]]
Let d be the number of 41-cent stamps [[var d]].
Let e be the number of two-cent stamps [[var e]].
Because the total value of the stamps  was $8.36, we have the equation [[eq b * d + c * e = 8.36]].
Because the number of 41-cent stamps is four more than twice the number of two-cent stamps, we have the equation [[eq d = 2 * e + 4]].
The answer is the value of d [[answer d]].

Q: Henning is mixing raisins and nuts to make 10 pounds of trail mix. Raisins cost $2 a pound and nuts cost $6 a pound. If Henning wants his cost for the trail mix to be $5.20 a pound, how many pounds of raisins should he use?

Peano solution:

Let a be the total weight of the trail mix [[var a]]. We have [[eq a = 10]]
Let b be the cost of one pound of raisin [[var b]]. We have [[eq b = 2]]
Let c be the cost of one pound of nuts [[var c]]. We have [[eq c = 6]]
Let d be the pounds of raisins [[var d]].
Let e be the pounds of nuts [[var e]].
Because Henning wants his price per pound to be 5.2, we have [[eq b * d + c * e = a * 5.2]]
Because Henning wants 10 pounds of trail mix, we have [[eq d + e = 10]]
The answer is the value of d [[answer d]].

Q: When Gabe drives from Sacramento to Redding it takes him 2.2 hours. It takes Elsa 2 hours to drive the same distance. Elsa’s speed is seven miles per hour faster than Gabe’s speed. Find Gabe’s speed, in miles per hour.

Peano solution:

Let a be the time it takes for Gabe to drive from Sacramento to Redding [[var a]]. We have [[eq a = 2.2]]
Let b be the time it takes Else to drive from Sacramento to Redding [[var b]]. We have [[eq b = 2]]
Let c be Gabe's speed [[var c]].
Let d be Elsa's speed [[var d]]. We have [[eq d = c + 7]]
Because they are traveling the same distance, we have [[eq a * c = b * d]].
The answer is the value of c [[answer c]].

Q: When Jenna spent 10 minutes on the elliptical trainer and then did circuit training for 20 minutes, her fitness app says she burned 278 calories. When she spent 20 minutes on the elliptical trainer and 30 minutes circuit training she burned 473 calories. How many calories does she burn for each minute on the elliptical trainer?

Peano solution:

Let a be the time Jenna spent on the elliptical trainer during her first workout [[var a]]. We have [[eq a = 10]]
Let b be the time Jenna spent on circuit training during her first workout [[var b]]. We have [[eq b = 20]]
Let c be the calories Jenna burnt during her first workout [[var c]]. We have [[eq c = 278]]
Let d be the time Jenna spent on the elliptical trainer during her second workout [[var d]]. We have [[eq d = 20]]
Let e be the time Jenna spent on circuit training during her second workout [[var e]]. We have [[eq e = 30]]
Let f be the calories Jenna burnt during her second workout [[var f]]. We have [[eq f = 473]]
Let g be the number of calories Jenna burns each minute on the elliptical trainer. [[var g]].
Let h be the number of calories Jenna burns each minute on circuit training. [[var h]].
Because of Jenna's first workout, we have [[eq a * g + b * h = c]]
Because of Jenna's second workout, we have [[eq d * g + e * h = f]]
The answer is the value of g [[answer g]].

Q: Joni left St. Louis on the interstate, driving west towards Denver at a speed of 65 miles per hour. Half an hour later, Kelly left St. Louis on the same route as Joni, driving 78 miles per hour. How many hours will it take Kelly to catch up to Joni?

Peano solution:

Let a be Joni's speed during the trip [[var a]]. We have [[eq a = 65]].
Let b be Kelly's speed during the trip [[var b]]. We have [[eq b = 78]].
Let c be the time Joni is driving until Kelly reaches her [[var c]].
Let d be the time Kelly is driving until she catches up to Joni [[var d]]. [[eq d = c - 0.5]]
Because they will have traveled the same distance once they catch up, we have [[eq a * c = b * d]].
The answer is the value of d [[answer d]].

Q: Mary had 5 apples. The next morning, she ate 2 apples. Then, in the afternoon, she bought as many apples as she had after eating those apples in the morning. How many apples did she end up with?

Peano solution:


Let a be the number of apples Mary started with [[var a]]. We have [[eq a = 5]]. 
Let b be how many apples she had in the morning after eating 2 apples [[var b]]. We have [[eq b = a - 2]]. 
Let c be the apples she bought in the afternoon [[var c]]. 
Since she bought as many as she had after eating, we have [[eq c = b]]. 
Let d be how many apples she ended up with [[var d]]. We have [[eq d = b + c]]. 
The answer is the value of d [[answer d]]. 


Q: Bob says to Alice: if you give me 3 apples and then take half of my apples away, then I will be left with 13 apples. How many apples do I have now?

Peano solution:

Let a be the number of apples Bob would end with [[var a]]. We have [[eq a = 13]]
Let b be how many apples Bob has before Alice took half his apples away [[var b]]. We have [[eq b = a * 2]]
Let c be the number of apples Bob has at the very beginning [[var c]].
Since Alice gave Bob three apples, we have [[eq c = b - 3]]
The answer is the value of c [[answer c]].


Q: Mario and Luigi together had 10 years of experience in soccer. Luigi had 3 more than Mario. How many did Mario have?

Peano solution:


Let a be the number of years Mario had [[var a]]. 
Let b be the number of years Luigi had [[var b]]. We have [[eq a + b = 10]]. We also have [[eq b = a + 3]]. 
The answer is the value of a [[answer a]].





Q: The planet Goob completes one revolution after every 2 weeks. How many hours will it take for it to complete half a revolution?

Peano solution:


Let a be the number of hours in a week [[var a]]. We have [[eq a = 168]]. 
Let b be the number of hours in a revolution [[var b]]. We have [[eq b = a * 2]]. 
Let c be the number of hours in half a revolution [[var c]]. We have [[eq c = b / 2]]. 
The answer is the value of c [[answer c]].





Q: {question}

Peano solution:
'''.strip() + '\n\n\n'
DECLARATIVE_THREE_SHOT_AND_PRINCIPLES


DECLARATIVE_THREE_SHOT_AND_PRINCIPLES_CODEX_SOLVE = '''
Let's solve mathematical word problems in a careful, formal manner. The solution will follow the Peano format: 
1- Each sentence in the solution either introduces a new variable or states a new equation. 
2- The last sentence gives the goal: which variable will contain the answer to the problem. 
3- Each equation only uses previously introduced variables. 
4- Each quantity is only named by one variable.
5- Use all the numbers in the question.

Q: Mary had 5 apples. The next morning, she ate 2 apples. Then, in the afternoon, she bought as many apples as she had after eating those apples in the morning. How many apples did she end up with?

Peano solution:


Let a be the number of apples Mary started with [[var a]]. We have [[eq a = 5]]. 
Let b be how many apples she had in the morning after eating 2 apples [[var b]]. We have [[eq b = a - 2]]. 
Let c be the apples she bought in the afternoon [[var c]]. 
Since she bought as many as she had after eating, we have [[eq c = b]]. 
Let d be how many apples she ended up with [[var d]]. We have [[eq d = b + c]]. 
The answer is the value of d [[answer d = 6]]. 





Q: Mario and Luigi together had 10 years of experience in soccer. Luigi had 3 more than Mario. How many did Mario have?

Peano solution:


Let a be the number of years Mario had [[var a]]. 
Let b be the number of years Luigi had [[var b]]. We have [[eq a + b = 10]]. We also have [[eq b = a + 3]]. 
The answer is the value of a [[answer a = 3.5]].





Q: The planet Goob completes one revolution after every 2 weeks. How many hours will it take for it to complete half a revolution?

Peano solution:


Let a be the number of hours in a week [[var a]]. We have [[eq a = 168]]. 
Let b be the number of hours in a revolution [[var b]]. We have [[eq b = a * 2]]. 
Let c be the number of hours in half a revolution [[var c]]. We have [[eq c = b / 2]]. 
The answer is the value of c [[answer c = 168]].





Q: {question}

Peano solution:
'''.strip() + '\n\n\n'