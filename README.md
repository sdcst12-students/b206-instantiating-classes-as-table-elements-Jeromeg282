## SDSS Computing Studies Python Assignment
### Assignment More Objects and Classes
Objectives:
* explore different ways of instantiating objects
* keep track of multiple instances at a time

Having named instances is good for keeping track of them, but often, you there will be instances where you will have an unknown number of instances, or may want a way of iterating through them quickly.  At times like these, it is a good idea to create instances as members of a list.

Consider example1.py
Note the creation of the empty table on line 16.  We use a for loop to iterate 10 numbers, and create instances to match those on lines 19 and 20.  This means that later on (line 26-27) we can retrieve those instances by iterating through all members in the list.

Example2 is mostly the same file, but onlines 26-27, instead of iterating through all of the values that were used to instantiate the object, we instead try to iterate through the object directly.  We need to change the conents of line 27 slightly to accomodate for the fact that we are accessing the object directly rather than the index of the objects.  Note that the first i doesn't provide nice output as expected.

Example3 uses a dictionary to store the instances, because here, we are insantiating them using keys selected from the list on line 19.  Again, note that there slight differences to how we access the dictionary of objects.  On line 21, we don't use append to add elements to the dictionary, but directly use the key to create the dictionary element.  Furthermore, on line 27, we can't just iterate through a range of numbers, because the index values are not sequential.  Instead, we iterate through the dictionary, and i takes on the value of the keys, after which we need to reference the dictionary elements by their keys.


##### Task 1
League Scores
Use the class template provided as a base.  Create instances for the following teams:
* Ants, Bears, Cougars, Doges, Elephants, Foxes, Giants

Use the provided game data (stored as dictionaries) to add wins/losses to each time.

Extension:
* Keep track of the games played (with scores) for each time
* Assume t1 in each dictionary is the home team.  Keep track of home/away in your game record

##### Task 2
Mean and Standard Deviation
You may be familiar with the concept of the mean.  This is the same as the average that you have calculated for your marks in school, but the standard deviation may be a new idea to you.  Access the following resources to determine what is meant by the standard deviation and how to calculate it.
**What are mean and standard deviation?**
You may want to access the following resources:
Definitions of Mean and Standard Deviation: 
https://www.youtube.com/watch?v=MRqtXL2WX2M
https://www.scribbr.com/statistics/standard-deviation/
https://www.dummies.com/article/academics-the-arts/math/statistics/standard-deviation-and-variance-147351/

How to calculate mean and standard deviation:
https://bit.ly/3LLOPsB
https://www.youtube.com/watch?v=WVx3MYd-Q9w
https://www.scribbr.com/statistics/standard-deviation/

Determine the mean and standard deviations for the data sets.  This practice for a more complicated problem in task 3.

##### Task 3
Create a database to keep track of random monsters in a game
Use the existing template as a guide and populate a list:

Rules: 
* each primary stat is generated as 3 random dice rolls (random 1-6) (strength, intelligance, piety, agility, stamina, charm)
* distribution of level is 1: 40%, 2: 30%, 3: 20%, 4: 10%
* each npc gets random 1-10 hp per level
* each npc gets some random money
* 30% chance to have 0-6 gold
* 50% chance go have 3-12 silver
* if they had no gold, they have a 75% chance to have 4-20 copper
* each gold is worth 10 silver and each silver is worth 10 copper

Create 100 NPC's
Generate a report that shows the distribution of NPC's by level
Generatea a report that shows the mean and standard deviation for the following:
* HP
* Wealth (in copper. For example 2 gold, 3 silver and 4 copper has a wealth of 234)





