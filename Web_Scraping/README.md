<p align="center">
<img src ="https://www.techtodayinfo.com/wp-content/uploads/2020/01/Web-Scraping.jpg">
</p>

---

<h2> Web Scraping </h2>

- Web scraping is a method used to extract data from websites. This is done by making HTTP requests to the specific URLs of the websites and then parsing the HTML data to retrieve the needed information. Web scraping is commonly used for a variety of applications, such as data mining, data analysis, data visualization, and many more. It's a powerful tool for handling and manipulating web data, making it easier for users to gather and utilize information from the internet.

---

<h2> Steps to Follow </h2>

- In this part I'll be using Beautiful Soup (bs4) which is a Python library used for web scraping and parsing HTML and XML documents. It is a powerful tool for extracting data from websites. To use Beautiful Soup for web scraping, you need to follow these steps:

1. **Install Required Libraries** :

```python
pip install html5lib

pip install requests

pip install bs4
```

2. **Access HTML Content**: Send an HTTP request to the webpage you want to scrape using the requests library in Python

3. **Parse HTML Content** : Using bs4 (Beautiful soup), which creates a parse tree for the web page based on specific criteria, allowing you to extract, navigate, search, and modify data from HTML)

4. **Search and Navigate**: Once you have parsed the HTML content, you can search and navigate through the parse tree to extract the desired data programmatically

---

<h2> Exercices </h2>

- In this section, I'll be exploring how to do Web Scraping, in various methods and scenarios:

  - [Web-Scraping-Quotes](./Web_Scraping.ipynb): scraping [Quotes-Authors](https://quotes.toscrape.com/), which is a classic example of web scraping (scrape Authors and Quotes 🍀)

  - [Workshop-Scraping-API](./Workshop_Web_Scraping.ipynb): Conducting a web scraping to gather emergency pharmcy information from [Glossary-Pharmacies](https://www.annuaire-gratuit.ma/) and then use the **API** [OpenWeather Map](https://openweathermap.org/) to collect informartion about the weather in those cities and then ouput the scraped with the collected info from the API and merge all that in one dataframe ⭐

  > [Drug-Stores](./drug_store.py) : That was my first try into solving the problem of workshop in my **IDE**, but refer to the collab notebook which is the complete version of the workshop, even though it still has an area of improvements in a lot of aspects 🛡

---

<h2> Author </h2>

- [`@Josh-techie`](https://github.com/Josh-techie) | Software Engineer Student

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
