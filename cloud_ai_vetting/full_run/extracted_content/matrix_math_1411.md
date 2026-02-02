# matrix math
**URL:** https://math.libretexts.org/Bookshelves/Applied_Mathematics/Applied_Finite_Mathematics_(Sekhon_and_Bloom)/02%3A_Matrices/2.01%3A_Introduction_to_Matrices
**Page Title:** 2.1: Introduction to Matrices - Mathematics LibreTexts
--------------------

In this section, you will learn to:
- Add and subtract matrices.
- Multiply a matrix by a scalar.
- Multiply two matrices.
A matrix is a 2 dimensional array of numbers arranged in rows and columns. Matrices provide a method of organizing, storing, and working with mathematical information. Matrices have an abundance of applications and use in the real world. Matrices provide a useful tool for working with models based on systems of linear equations. We’ll use matrices in sections 2.2, 2.3, and 2.4 to solve systems of linear equations with several variables in this chapter.
Matrices are used in encryption, which we will explore in section 2.5 and in economic modelling, explored in section 2.6. We use matrices again in chapter 4, in optimization problems such as maximizing profit or revenue, or minimizing cost. Matrices are used in business for scheduling, routing transportation and shipments, and managing inventory.
Just about any application that collects and manages data can apply matrices. Use of matrices has grown as the availability of data in many areas of life and business has increased. They are important tools for organizing data and solving problems in all fields of science, from physics and chemistry, to biology and genetics, to meteorology, and economics. In computer science, matrix mathematics lies behind animation of images in movies and video games.
Computer science analyzes diagrams of networks to understand how things are connected to each other, such as relationships between people on a social website, and relationships between results in line search and how people link from one website to another. The mathematics to work with network diagrams comprise the field of “graph theory”; it relies on matrices to organize the information in the graphs that diagram connections and associations in a network. For example, if you use Facebook or Linked-In, or other social media sites, these sites use network graphs and matrices to organize your relationships with other users.

## Introduction to Matrices

A matrix is a rectangular array of numbers. Matrices are useful in organizing and manipulating large amounts of data. In order to get some idea of what matrices are all about, we will look at the following example.
Fine Furniture Company makes chairs and tables at its San Jose, Hayward, and Oakland factories. The total production, in hundreds, from the three factories for the years 2014 and 2015 is listed in the table below.
- Represent the production for the years 2014 and 2015 as the matrices A and B.
- Find the difference in sales between the years 2014 and 2015.
- The company predicts that in the year 2020 the production at these factories will be double that of the year 2014. What will the production be for the year 2020?
Solution
a) The matrices are as follows:
A = [ 30 18 20 12 16 10 ]
B = [ 36 20 24 18 20 12 ]
b) We are looking for the matrix B − A . When two matrices have the same number of rows and columns, the matrices can be added or subtracted entry by entry. Therefore, we get
B − A = [ 36 − 30 20 − 18 24 − 20 18 − 12 20 − 16 12 − 10 ] = [ 6 2 4 6 4 2 ]
c) We would like a matrix that is twice the matrix of 2014, i.e., 2 ⁢ A .
Whenever a matrix is multiplied by a number, each entry is multiplied by the number.
2 ⁢ A = 2 ⁢ [ 30 18 20 12 16 10 ] = [ 60 36 40 24 32 20 ]
Before we go any further, we need to familiarize ourselves with some terms that are associated with matrices. The numbers in a matrix are called the entries or the elements of a matrix.
Whenever we talk about a matrix, we need to know the size or the dimension of the matrix. The dimension of a matrix is the number of rows and columns it has. When we say a matrix is a “3 by 4 matrix”, we are saying that it has 3 rows and 4 columns. The rows are always mentioned first and the columns second. This means that a 3 × 4 matrix does not have the same dimension as a 4 × 3 matrix.
A = [ 1 4 − 2 0 3 − 1 7 9 6 2 0 5 ]
B = [ 2 9 8 − 3 0 1 6 5 − 2 − 4 7 8 ]
Matrix A has dimensions 3 × 4 and matrix B has dimensions 4 × 3 .
A matrix that has the same number of rows as columns is called a square matrix . A matrix with all entries zero is called a zero matrix. A square matrix with 1's along the main diagonal and zeros everywhere else, is called an identity matrix . When a square matrix is multiplied by an identity matrix of same size, the matrix remains the same.
I = [ 1 0 0 0 1 0 0 0 1 ]
Matrix I is a 3 × 3 identity matrix
A matrix with only one row is called a row matrix or a row vector, and a matrix with only one column is called a column matrix or a column vector . Two matrices are equal if they have the same size and the corresponding entries are equal.
We can perform arithmetic operations with matrices. Next we will define and give examples illustrating the operations of matrix addition and subtraction, scalar multiplication, and matrix multiplication. Note that matrix multiplication is quite different from what you would intuitively expect, so pay careful attention to the explanation. Note also that the ability to perform matrix operations depends on the matrices involved being compatible in size, or dimensions, for that operation. The definition of compatible dimensions is different for different operations, so note the requirements carefully for each.

## Matrix Addition and Subtraction

If two matrices have the same size, they can be added or subtracted. The operations are performed on corresponding entries.
Given the matrices A , B , C and D , below
A = [ 1 2 4 2 3 1 5 0 3 ] B = [ 2 − 1 3 2 4 2 3 6 1 ] C = [ 4 2 3 ] D = [ − 2 − 3 4 ]
Find, if possible.
- A + B
- C − D
- A + D .
Solution
As we mentioned earlier, matrix addition and subtraction involves performing these operations entry by entry.
a) We add each element of A to the corresponding entry of B .
A + B = [ 3 1 7 4 7 3 8 6 4 ]
b) Just like the problem above, we perform the subtraction entry by entry.
C − D = [ 6 5 − 1 ]
c) The sum A + D cannot be found because the two matrices have different sizes.
Note: Two matrices can only be added or subtracted if they have the same dimension.

## Multiplying a Matrix by a Scalar

If a matrix is multiplied by a scalar, each entry is multiplied by that scalar. We can consider scalar multiplication as multiplying a number and a matrix to obtain a new matrix as the product.
Given the matrix A and C in the example above, find 2 ⁢ A and − 3 ⁢ C .
Solution
To find 2 ⁢ A , we multiply each entry of matrix A by 2, and to find − 3 ⁢ C , we multiply each entry of C by -3. The results are given below.
a) We multiply each entry of A by 2.
2 ⁢ A = [ 2 4 8 4 6 2 10 0 6 ]
b) We multiply each entry of C by -3.
− 3 ⁢ C = [ − 12 − 6 − 9 ]

## Multiplication of Two Matrices

To multiply a matrix by another is not as easy as the addition, subtraction, or scalar multiplication of matrices. Because of its wide use in application problems, it is important that we learn it well. Therefore, we will try to learn the process in a step by step manner. We first begin by finding a product of a row matrix and a column matrix.
Find the product A ⁢ B , given
A = [ 2 3 4 ]
and
B = [ a b c ] .
Solution
The product is a 1 × 1 matrix whose entry is obtained by multiplying the corresponding entries and then forming the sum.
AB = [ 2 3 4 ] ⁢ [ a b c ] = [ ( 2 ⁢ a + 3 ⁢ b + 4 ⁢ c ) ]
Note that A ⁢ B is a 1 × 1 matrix, and its only entry is 2 ⁢ a + 3 ⁢ b + 4 ⁢ c .
Find the product A ⁢ B , given
A = [ 2 3 4 ]
and
B = [ 5 6 7 ]
Solution
Again, we multiply the corresponding entries and add.
AB = [ 2 3 4 ] ⁢ [ 5 6 7 ] = [ 2 ⋅ 5 + 3 ⋅ 6 + 4 ⋅ 7 ] = [ 10 + 18 + 28 ] = [ 56 ]
Note: In order for a product of a row matrix and a column matrix to exist, the number of entries in the row matrix must be the same as the number of entries in the column matrix.
Find the product AB, given
A = [ 2 3 4 ]
and
B = [ 5 3 6 4 7 5 ] .
Solution
We know how to multiply a row matrix by a column matrix. To find the product A ⁢ B , in this example, we will multiply the row matrix A to both the first and second columns of matrix B , resulting in a 1 × 2 matrix.
AB = [ 2 ⋅ 5 + 3 ⋅ 6 + 4 ⋅ 7 2 ⋅ 3 + 3 ⋅ 4 + 4 ⋅ 5 ] = [ 56 38 ]
We multiplied a 1 × 3 matrix by a matrix whose size is 3 × 2 . So unlike addition and subtraction, it is possible to multiply two matrices with different dimensions, if the number of entries in the rows of the first matrix is the same as the number of entries in the columns of the second matrix.
Find the product A ⁢ B , given:
A = [ 2 3 4 1 2 3 ]
and
B = [ 5 3 6 4 7 5 ]
Solution
This time we are multiplying two rows of the matrix A with two columns of the matrix B . Since the number of entries in each row of A is the same as the number of entries in each column of B , the product is possible. We do exactly what we did in the last example. The only difference is that the matrix A has one more row.
We multiply the first row of the matrix A with the two columns of B , one at a time, and then repeat the process with the second row of A. We get
AB = [ 2 3 4 1 2 3 ] ⁢ [ 5 3 6 4 7 5 ] = [ 2 ⋅ 5 + 3 ⋅ 6 + 4 ⋅ 7 2 ⋅ 3 + 3 ⋅ 4 + 4 ⋅ 5 1 ⋅ 5 + 2 ⋅ 6 + 3 ⋅ 7 1 ⋅ 3 + 2 ⋅ 4 + 3 ⋅ 5 ]
AB = [ 56 38 38 26 ]
Find, if possible:
- E ⁢ F
- F ⁡ E
- F ⁡ H
- G ⁡ H
- H ⁡ G
E = [ 1 2 4 2 3 1 ] F = [ 2 − 1 3 2 ] G = [ 4 1 ] H = [ − 3 − 1 ]
Solution
a) To find E ⁢ F , we multiply the first row [ 1 2 ]
of E with the columns [ 2 3 ] and [ 1 − 2 ] of the matrix F, and then repeat the process by multiplying the other two rows of E with these columns of F. The result is as follows:
EF = [ 1 2 4 2 3 1 ] ⁢ [ 2 − 1 3 2 ] = [ 1 ⋅ 2 + 2 ⋅ 3 1 ⋅ − 1 + 2 ⋅ 2 4 ⋅ 2 + 2 ⋅ 3 4 ⋅ − 1 + 2 ⋅ 2 3 ⋅ 2 + 1 ⋅ 3 3 ⋅ − 1 + 1 ⋅ 2 ] = [ 8 3 14 0 9 − 1 ]
b) Product F ⁡ E is not possible because the matrix F has two entries in each row, while the matrix E has three entries in each column. In other words, the matrix F has two columns, while the matrix E has three rows.
c) FH = [ 2 − 1 3 2 ] ⁢ [ − 3 − 1 ] = [ 2 ⋅ − 3 + − 1 ⋅ − 1 3 ⋅ − 3 + 2 ⋅ − 1 ] = [ − 5 − 11 ]
d) GH = [ 4 1 ] ⁢ [ − 3 − 1 ] = [ 4 ⋅ − 3 + 1 ⋅ − 1 − 1 ] = [ − 13 ]
e) HG = [ − 3 − 1 ] ⁢ [ 4 1 ] = [ − 3 ⋅ 4 − 3 ⋅ 1 − 1 ⋅ 4 − 1 ⋅ 1 ] = [ − 12 − 3 − 4 − 1 ]
We summarize some important properties of matrix multiplication that we observed in the previous examples.
In order for product A ⁢ B to exist:
- the number of columns of A must equal the number of rows of B
- if matrix A has dimension m × n and matrix B has dimension n × p , then the product A ⁢ B will be a matrix with dimension m × p .
Matrix multiplication is not commutative: if both matrix products A ⁢ B and B ⁢ A exist, most of the time A ⁢ B will not equal B ⁢ A .
Given matrices R , S , and T below, find 2 ⁢ R ⁢ S − 3 ⁢ S ⁢ T .
R = [ 1 0 2 2 1 5 2 3 1 ] S = [ 0 − 1 2 3 1 0 4 2 1 ] T = [ − 2 3 0 − 3 2 2 − 1 1 0 ]
Solution
We multiply the matrices R and S.
( 2.1.1 ) RS = [ 8 3 4 23 9 9 13 3 5 ] 2 ⁢ RS = 2 ⁢ [ 8 3 4 23 9 9 13 3 5 ] = [ 16 6 8 46 18 18 26 6 10 ] ST = [ 1 0 − 2 − 9 11 2 − 15 17 4 ] 3 ⁢ ST = 3 ⁢ [ 1 0 − 2 − 9 11 2 − 15 17 4 ] = [ 3 0 − 6 − 27 33 6 − 45 51 12 ]
Thus
2 ⁢ RS − 3 ⁢ ST = [ 16 6 8 46 18 18 26 6 10 ] − [ 3 0 − 6 − 27 33 6 − 45 51 12 ] = [ 13 6 14 73 − 15 12 71 − 45 − 2 ]
Find F 2 given matrix
F = [ 2 − 1 3 2 ]
Solution
F 2 is found by multiplying matrix F by itself, using matrix multiplication.
F 2 = [ 2 − 1 3 2 ] ⁢ [ 2 − 1 3 2 ] = [ 2 ⋅ 2 + ( − 1 ) ⋅ 3 2 ⋅ ( − 1 ) + ( − 1 ) ⋅ 2 3 ⋅ 2 + 2 ⋅ 3 3 ⋅ ( − 1 ) + 2 ⋅ 2 ] = [ 1 − 4 12 1 ]
Note that F 2 is not found by squaring each entry of matrix F . The process of raising a matrix to a power, such as finding F 2 , is only possible if the matrix is a square matrix.

## USING MATRICES TO REPRESENT A SYSTEM OF LINEAR EQUATIONS

In this chapter, we will be using matrices to solve linear systems. In section 2.4, we will be asked to express linear systems as the matrix equation A ⁢ X = B , where A , X , and B are matrices.
- Matrix A is called the coefficient matrix.
- Matrix X is a matrix with 1 column that contains the variables.
- Matrix B is a matrix with 1 column that contains the constants.
Verify that the system of two linear equations with two unknowns:
( 2.1.2 ) a ⁢ x + b ⁢ y = h c ⁢ x + d ⁢ y = k
can be written as A ⁢ X = B , where
A = [ a b c d ] X = [ x y ] and B = [ h k ]
Solution
If we multiply the matrices A and X , we get
A ⁢ X = [ a b c d ] ⁢ [ x y ] = [ a ⁢ x + b ⁢ y c ⁢ x + d ⁢ y ]
If A ⁢ X = B then
[ a ⁢ x + b ⁢ y c ⁢ x + d ⁢ y ] = [ h k ]
If two matrices are equal, then their corresponding entries are equal. It follows that
( 2.1.3 ) a ⁢ x + b ⁢ y = h c ⁢ x + d ⁢ y = k
Express the following system as a matrix equation in the form A ⁢ X = B .
( 2.1.4 ) 2 ⁢ x + 3 ⁢ y − 4 ⁢ z = 5 3 ⁢ x + 4 ⁢ y − 5 ⁢ z = 6 5 ⁢ x ⁢ − 6 ⁢ z = 7
Solution
This system of equations can be expressed in the form A ⁢ X = B as shown below.
[ 2 3 − 4 3 4 − 5 5 0 − 6 ] ⁢ [ x y z ] = [ 5 6 7 ]

## Support Center

### How can we help?


--------------------