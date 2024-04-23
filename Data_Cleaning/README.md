<p align="center">
<img src ="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ytimg.com%2Fvi%2FjN3MD_UoaMs%2Fmaxresdefault.jpg&f=1&nofb=1&ipt=fe9ca313afb733650e8aa8ba16ac7d0c2dc7ea5bdea7400d99c4ea51373bf21a&ipo=images">
</p>

---

<h2> Data Cleaning : Python </h2>

- Data cleaning is an essential step in the data analysis and machine learning process. It involves preparing and preprocessing data for use in a model by converting data format, removing duplicate data, dealing with missing data, detecting outliers, feature engineering, and feature selection.

---

<h2> Exercices </h2>

- In this section, I'll be exploring some data cleaning techniques, summarized in the following exercices:

  - [Data-Cleaning](./Data_Cleaning.ipynb): Create dataframe, create a new column in a df, or delete it. Populate a newly added column, replace a value in a df.
    > You can access it directly in google colab at this link: [Google-Colab-Data-Cleaning](https://colab.research.google.com/drive/1yppmGDxaOKZZq1eRsWxk-BFM9aEpk2fM?usp=sharing)

- Here, we will be discussing the Levenshtein-Distance ALgorithm, below you'll find a simple explanation of the Levenshtein Distance algorithm:

**The Levenshtein Distance** algorithm calculates the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into another. It works like this:

    - **Take two words/strings as input**
    - **Compare the characters of both strings one by one**
    - **If the characters are the same, go to the next pair**
    - **If the characters are different, it's an edit**
    - **An edit can be an insertion, deletion or substitution of a character**
    - **Count each difference as 1 edit**
    - **Keep track of the minimum number of edits needed**
    - **Go through all possible edit scenarios**
    - **The lowest count of edits is the Levenshtein Distance**

    > Example:
    ```
    Strings: kitten, sitting

    Compare k vs s -> difference, 1 edit
    Compare i vs i -> same, no edit
    Compare t vs t -> same, no edit
    Compare t vs i -> difference, 1 more edit
    Compare e vs t -> difference, 1 more edit
    Compare n vs n -> same, no edit
    Compare vs g -> difference, 1 more edit

    Minimum edits needed is 3 (substitution, insertion, substitution)
    So Levenshtein Distance between the words is 3
    ```

    > In simple terms, it finds the minimum number of single-character changes required to transform one word into another. This gives a measure of difference between strings.

[Levenshtein-Distance-Algorithm-Implementation](./Levenshtein_Distance.py): Simple implementation of the algorithm with python 🌟

---

<h2> Author </h2>

- [`@Josh-techie`]() | Software Engineer Student

  > Reach out to me if you need any help or have any questions.

  <a href="mailto:youssef.abouyahia@e-polytechnique.ma">
  	<img alt="Feel free to contact me" src="https://img.shields.io/badge/-Ask_me_anything-blue?style=flat&logo=Gmail&logoColor=white&link=mailto:youssef.abouyahia@e-polytechnique.ma&color=3d85c6" />
  </a>
  <span> | </span>
    <a href="https://www.linkedin.com/in/youssef-abouyahia/">
        <img alt="Linkedin Profile" src="https://img.shields.io/badge/-Linkedin-0072b1?style=flat&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/youssef-abouyahia/" />
    </a>
    <span> | </span>
    <a href="https://twitter.com/JoesephAb">
        <img alt="Twitter Profile" src="https://img.shields.io/badge/-Twitter-0072b1?style=flat&logo=Twitter&logoColor=white&link=https://twitter.com/JoesephAb&color=1DA1F2" />
    </a>
