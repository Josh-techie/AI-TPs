<p align="center">
<img src ="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.morioh.com%2F2020%2F01%2F06%2F4d245f695904.jpg&f=1&nofb=1&ipt=282362382e7e646584db5531ada62bef80e7d2388592af30e30d2574b7bac945&ipo=images">
</p>

---

**Exercise 1: Linear Regression**

**Objective:** Develop a linear regression model using the provided dataset to predict stock values after the market closes.

**Dataset Link:** [Market Dataset](https://drive.google.com/file/d/1u0rzO67LbbmhBAoJRsXzYhiar9eQ_hql/view?usp=drive_link)

**Features (from the 'market.csv' file):**

1. Date
2. Open
3. High
4. Low
5. Last
6. Close (Target variable)
7. Total Trade Quantity
8. Turnover (Lacs)

---

**Instructions:**

1. **Download the Dataset:**

   - Click on the provided link to access and download the dataset.

2. **Explore the Dataset:**

   - Use tools like Pandas in Python to load and explore the dataset.
   - Check for missing values, data types, and basic statistics.

3. **Data Preparation:**

   - Handle any missing values appropriately (e.g., imputation or removal).
   - Convert the 'Date' column to a datetime object for time-series analysis if needed.

4. **Feature Selection:**

   - Based on the problem statement, select relevant features for training the linear regression model. In this case, consider using 'Open,' 'High,' 'Low,' 'Last,' 'Total Trade Quantity,' and 'Turnover (Lacs)' as potential predictors.

5. **Data Splitting:**

   - Split the dataset into training and testing sets to evaluate the model's performance.

6. **Linear Regression Model:**

   - Utilize a linear regression algorithm to model the relationship between the selected features and the 'Close' target variable.

7. **Model Training:**

   - Train the linear regression model using the training dataset.

8. **Model Evaluation:**

   - Evaluate the model's performance on the testing set, using metrics such as Mean Squared Error (MSE) or R-squared.

9. **Documentation:**

   - Document the steps and code clearly, providing comments and explanations.

10. **Save and Share:**
    - Save the trained model for future use.
    - Share the code, dataset, and any relevant findings in a repository or document.

> Remember to adapt the code and instructions based on the programming language you are using. Feel free to use popular libraries like Pandas, NumPy, and scikit-learn for data manipulation and modeling in Python.
