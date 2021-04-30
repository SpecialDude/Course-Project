> # Course Project (Scientific Programming CSC 231)
-----------------------------------------------------------------Computer Science-------------------------------------------------------------------------

Project: Arithmetic Arranger
Description:
### Assignment

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
```
  235
+  52
-----
```

Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to `True`, the answers should be displayed.

### For example

Function Call:
```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function Call:
```py
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
----	------	  ------    -----
```

### Rules

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will **return** a **string** that describes an error that is meaningful to the user.  


* Situations that will return an error:
  * If there are **too many problems** supplied to the function. The limit is **seven**, anything more will return:
    `Error: Too many problems.`
  * The appropriate operators the function will accept are **addition** and **subtraction**. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
    `Error: Operator must be '+' or '-'.`
  * Each number (operand) should only contain digits (0 - 9). Otherwise, the function will return:
    `Error: Numbers must only contain digits.`
  * Each operand (aka number on each side of the operator) has a max of six digits in width. Otherwise, the error string returned will be:
    `Error: Numbers cannot be more than six digits.`
*  If the user supplied the correct format of problems, the conversion you return will follow these rules:
    * There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
    * Numbers should be right-aligned.
    * There should be four spaces between each problem.
    * There should be dashes at the bottom of each problem and at the bottom of each answer. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)


Write your code in `arithmetic_arranger.py`.

-----------------------------------------------------------------Computer Science-------------------------------------------------------------------------



---------------------------------------------------------------------Geology------------------------------------------------------------------------------

Project: PISA Data Visualization
Description:
The Organisation for Economic Co-operation and Development (OECD), within its Programme for International Student Assessment (PISA), publishes an
evaluation of the educational systems around the world by measuring the performance of 15-year-old school pupils on mathematics, science, and reading.
The evaluation is carried out every three years. Read these data in to a pandas DataFrame and use its grouping functionality to determine and visualize
(a) the overall performance of all studied countries over time;
(b) the gender disparity (if any) in each of Reading, Mathematics and Science
(c) the correlation between the performances in each of these subject areas across all countries.
(d) Any other visualization you think might be insightful

Historical PISA data can be downloaded from https://scipython.com/ex/bza

---------------------------------------------------------------------Geology------------------------------------------------------------------------------



----------------------------------------------------------------------Physics-----------------------------------------------------------------------------

Project: Animation of Voyager 2 Space Probe
Description:
NASA�s Jet Propulsion Laboratory (JPL) maintains a web service and database called HORIZONS
that can be used to calculate ephemerides (the trajectories of objects in the solar system over time).
Use data from this resource, which has been pre-selected, to produce an animation of
the trajectory of the Voyager 2 space probe, between its launch in August 1977 and the end of 1999.
This period includes several gravity-assist (�slingshot�) maneuvers as the spacecraft flies past the larger planets.
Only the (X; Y) coordinates of the relevant bodies need be considered.

Data Source: https://scipython.com/ex/bas

----------------------------------------------------------------------Physics-----------------------------------------------------------------------------



-----------------------------------------------------------------------Statistics-------------------------------------------------------------------------

Project: Statistical Analysis and Visualization
Description:
Stanford University recently released the list of top 2% scientists in the world.
The list can be found in the file available at the URL below.

File: https://data.mendeley.com/public-files/datasets/btchxktzyw/files/dd0904a8-0eba-4cf3-be4a-c6092261fed5/file_downloaded

Your task is to write a program to analyse and visualize different statistics of the list as follows:
1. The number of scientists per institution
2. The number of scientists per country
3. The number of scientists per field (sm-field)
4. The number of scientists per subfield (sm-subfield-1 and sm-subfield-2)
5. The number of scientists per institution in Nigeria
6. The correlation between the year of first publication (firstyr) and the number of pubications (np6019)
7. Any other vis                    ualization you think could be insightful.
-----------------------------------------------------------------------Statistics-------------------------------------------------------------------------