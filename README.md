<div align="center">

# **BICIMAD - TEMPLOS CATOLICOS MADRID** </div>
![Imagen](https://www.emesa-m30.es/wp-content/uploads/2020/08/1-estaciones-bici-mad.jpg)

---

#### <div align="center">**This is a data analysis pipeline for shared bicycle data in Madrid, Spain. The pipeline retrieves data from the Bicimad shared bicycle stations, along with data on points of interest in Madrid, and calculates the distance between each shared bicycle station and each point of interest.** </div>

&nbsp;

## 💻 **Requirements:** ##

* Python `3.11` or superior
* Jupyter Notebook
* All necessary packages/libraries are listed in the 'requirements.txt' file.

&nbsp;

##  ⚙️ **Configuration:**

+ Clone this repository: git clone https://github.com/ChristianLameda/ironhack_m1_project.git
+ Install required packages: `pip install -r requirements.txt`
+ You will find the bicimad.db database in the folder data/raw/.
+ Download the points of interest data into the data/raw/ directory. You can download the data from [here](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/Templos32e32iglesias32no32cat243licas). The file should be named templos-catolicos.json.

&nbsp;
## 💾  **Usage:**
* Run the pipeline by typing the following command: 
```
python main.py 

Optional arguments:
--help               show this help message and exit
--all                show the entire table with all places
--place              show the table with selected places
```

&nbsp;
## 🎯 **Output**
* The pipeline generates a CSV file stored in data/result/bicimad_distance.csv, which contains the distance in meters between each shared bicycle station and each point of interest.

&nbsp;
## ⭐️ **Credits**
* This pipeline was created by Christian Lameda as part of the "Data Analytics" Bootcamp at IronHack Madrid. 











