## Linear Regression
---
is a prominent statistical method and machine learning algorithm used to find the linear relationship between a target (dependent) variable and one or more predictor variables. 


It maps numeric inputs to numeric outputs by fitting a line to a set of data points.

The core objective of linear regression is to obtain a "best fit line".


- **There 2 types of LR**  `simple & multiple`: <br>
- **Simple LR:** has only one `x` (1 Predictor Vairiable) & the target Variable (Predicted Variable). <br>
- **Multiple LR:** 2 or more predictor variables & the target variable.

- **Examples:**

When we predict rent based on square feet alone that is simple linear regression. `[Simple]` <br>
When we predict rent based on square feet and age of the building that is an example of multiple linear regression. `[Multiple]`

---

The best fit line is the one where the total prediction error measured as the distance between the actual data points and the regression line is as small as possible.

To achieve this, the model uses a loss function.

---

## Simple LR
---
**y<sub>p</sub> = m * x + c**

<center>

<img src='simple_linear_regression.jpg' height=300px width=400px/>
</center>

m & c are changed to minimize the error (control the position of the line)

---
**Sum of Squared Error:**

This calculates the total squared distance between the true data points and the regression line:<br>
Error = SUM[(actual_output - predicted_output)<sup>2</sup>]

**Mean Squared Error (MSE):**

This is the specific loss function used to evaluate the accuracy of the chosen `m` and `c` values <br>
<center>
<img src='MSE_Eq.png' alt = 'MSE Equation' height=200px width=400px/>
</center>

---


### Gradient descent
---

Gradient descent is an iterative optimization algorithm to find the minimum of a function (Minimizing the Error).



### Multiple LR:

Multiple regression considers the influence of multiple independent variables on a dependent variable `Y`.

y<sub>p</sub> = b<sub>0</sub> + b<sub>1</sub> * x<sub>1</sub> + b<sub>2</sub> * x<sub>2</sub> + ... + b<sub>n</sub> * x<sub>n</sub>

- **b<sub>0</sub>** is `c`
- **b<sub>n</sub>** is `m`


**Multiple regression analysis has three main uses:-**
1. You can look at the strength of the effect of the independent variables on the dependent variable.
2. You can use it to ask how much the dependent variable will change if the independent variables are changed.
3. You can also use it to predict trends and future values.

---

## Polynomial Regression:
---

Change in the degree of input value to make the line more fit the data.

`More Fit the Data Means:` passes through more data points.

<center>
<img src='Polynomial_Regression.png' width=490px height=310px  />
</center>

---

**What is overfitting?**

Overfitting is a common problem in machine learning and data science where a model fails to generalize well from its training data to new, unseen data.

**When does overfitting happen?** 

It typically happens when a model is overly complex, such as when you drastically increase the degree in polynomial regression (for example, using a degree of 20). <br>
This high degree forces the regression curve to bend sharply to pass through almost all of the specific data points in your training set.


**noise:** refers to the random points, fluctuations, or extreme outliers in your training data that do not represent the actual relationship you are trying to predict.

---