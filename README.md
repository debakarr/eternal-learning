Repository for all my learning stuff. This is going to be a huge repository containing my lifelong learning resources (notes on different courses).

***

# Index

* [Books](#books)

* [Online Courses](#onlineCourses)
	* [[Udemy] Machine Learning A-Z™: Hands-On Python & R In Data Science](#udemyMachineLearning)
	* [[Google Developers] Machine Learning Crash Course with TensorFlow APIs](#googleDevelopersMachineLearning)

* [Languages](#languages)
	* [Python](#python)
		* [Learn Python The Hard Way](#lpthw)

* [My Blog](#myBlog)

***
<a name="books"></a>
## Books


***

<a name="onlineCourses"></a>
## Online Courses

***
<a name="udemyMachineLearning"></a>
#### [Udemy] Machine Learning A-Z™: Hands-On Python & R In Data Science

[Link to the course](https://www.udemy.com/machinelearning/)

[Link to my original seperate repository](https://github.com/Dibakarroy1997/machinelearning)

***

* Materials
* My Notes [Jupyter Notebook]
* [Important links](#importantLinks)

***

* **Part 1 - Data Preprocessing**

	* [[Python] Data Preprocessing](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%201%20-%20Data%20Preprocessing/%5BPython%5D%20Data%20Preprocessing.ipynb)
	* [[R] Data Preprocessing](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%201%20-%20Data%20Preprocessing/%5BR%5D%20Data%20Preprocessing.ipynb)

	* **Steps involved**: *Import the dataset -> Taking care of missing data -> Encoding categorical data -> Splitting the dataset into Trainingset and Test set -> Feature Scaling*

* * *

* **Part 2 - Regression**
	* **Simple Linear Regression** 
		* [[Python] Simple Linear Regression](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%202%20-%20Regression/Simple%20Linear%20Regression/%5BPython%5D%20Simple%20Linear%20Regression.ipynb)
		* [[R] Simple Linear Regression](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%202%20-%20Regression/Simple%20Linear%20Regression/%5BR%5D%20Simple%20Linear%20Regression.ipynb)

		* **Steps involved**: *Data preprocessing -> Fitting Simple Linear Regression to the Training Set -> Predicting the Test set result -> Visualising the Training set results -> Visualising the Test set results*

	* **Multiple Linear Regression**
		* [[Python] Multiple Linear Regression](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%202%20-%20Regression/Multiple%20Linear%20Regression/%5BPython%5D%20Multiple%20Linear%20Regression.ipynb)
		* [[R] Multiple Linear Regression](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%202%20-%20Regression/Multiple%20Linear%20Regression/%5BR%5D%20Multiple%20Linear%20Regression.ipynb)

		* **Steps involved**: *Data prepocessing [Encoding categorical data(if any) -> Avoid dummy variable trap(can be done using Python and R library)] -> Fitting Multiple Linear Regression to the training set -> Predicting the test set reults*

		* [**For steps needed for Backward Elimination please refer to the pdf**](https://github.com/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%202%20-%20Regression/Multiple%20Linear%20Regression/Step-by-step-Blueprints-For-Building-Models)

	* **Polynomial Regression**
		* [[Python] Polynomial Regression](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%202%20-%20Regression/Polynomial%20Regression/%5BPython%5D%20Polynomial%20Regression.ipynb)
		* [[R] Polynomial Regression](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%202%20-%20Regression/Polynomial%20Regression/%5BR%5D%20Polynomial%20Regression.ipynb)

		* **Steps involved**: *Data preprocessing -> Fitting Polynomial Regression to the dataset -> Visualising the Polynomial Regression results -> Adjust degree -> Get a more continuous curve -> Predicting a new result with Polynomial Regression*

	* **Support Vector Regression**
		* [[Python] Support Vector Regression (SVR)](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%202%20-%20Regression/Support%20Vector%20Regression%20%28SVR%29/%5BPython%5D%20Support%20Vector%20Regression%20%28SVR%29.ipynb)
		* [[R] Support Vector Regression (SVR)](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%202%20-%20Regression/Support%20Vector%20Regression%20%28SVR%29/%5BR%5D%20Support%20Vector%20Regression%20%28SVR%29.ipynb)

		* **Steps involved**: *Data preprocessing (for python we need to do Feature Scaling) -> Fitting the SVR Model to the dataset-> Predicting a new result -> Visualising the SVR Regression results*

	* **Decision Tree Regression**
		* [[Python] Decision Tree Regression](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%202%20-%20Regression/Decision%20Tree%20Regression/%5BPython%5D%20Decision%20Tree%20Regression.ipynb)
		* [[R] Decision Tree Regression](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%202%20-%20Regression/Decision%20Tree%20Regression/%5BR%5D%20Decision%20Tree%20Regression.ipynb)

		* **Steps involved**: *Data preprocessing -> Fitting the Decision Tree Regression Model to the dataset -> Predicting a new result -> Visualising the Decision Tree Regression results*

	* **Random Forest Regression**
		* [[Python] Random Forest Regression](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%202%20-%20Regression/Random%20Forest%20Regression/%5BPython%5D%20Random%20Forest%20Regression.ipynb)
		* [[R] Random Forest Regression](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%202%20-%20Regression/Random%20Forest%20Regression/%5BR%5D%20Random%20Forest%20Regression.ipynb)

		* **Steps involved**: *Data preprocessing -> Fitting the Random Forest Regression Model to the dataset (tweak the NTree parameter)-> Predicting a new result -> Visualising the Random Forest Regression results*

* * *

* **Part 3 - Classification**
	* **Logistic Regression** 
		* [[Python] Logistic Regression](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/Logistic%20Regression/%5BPython%5D%20Logistic%20Regression.ipynb)
		* [[R] Logistic Regression](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/Logistic%20Regression/%5BR%5D%20Logistic%20Regression.ipynb)

		* **Steps involved**: *Data preprocessing -> Fitting Logistic Regression to the Training Set -> Predicting the Test set result -> Making and analysing the Confusion Matrix -> Visualising the Training set results -> Visualising the Test set results*

	* **K-Nearest Neighbors** 
		* [[Python] K-Nearest Neighbors](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/K%20Nearest%20Neighbors/%5BPython%5D%20K-Nearest%20Neighbour.ipynb)
		* [[R] K-Nearest Neighbors](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/K%20Nearest%20Neighbors/%5BR%5D%20K-Nearest%20Neighbour.ipynb)

		* **Steps involved**: *Data preprocessing -> Fitting K-Nearest Neighbor Classifier to the Training Set -> Predicting the Test set result -> Making and analysing the Confusion Matrix -> Visualising the Training set results -> Visualising the Test set results*

	* **Support Vector Machine** 
		* [[Python] Support Vector Machine](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/Support%20Vector%20Machine/%5BPython%5D%20Support%20Vector%20Machine.ipynb)
		* [[R] Support Vector Machine](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/Support%20Vector%20Machine/%5BR%5D%20Support%20Vector%20Machine.ipynb)

		* **Steps involved**: *Data preprocessing -> Fitting Support Vector Machine Classifier to the Training Set -> Predicting the Test set result -> Making and analysing the Confusion Matrix -> Visualising the Training set results -> Visualising the Test set results*

	* **Kernel SVM** 
		* [[Python] Kernel SVM](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/Kernel%20SVM/%5BPython%5D%20Kernel%20SVM.ipynb)
		* [[R] Kernel SVM](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/Kernel%20SVM/%5BR%5D%20Kernel%20SVM.ipynb)

		* **Steps involved**: *Data preprocessing -> Fitting Kernel SVM to the Training Set -> Predicting the Test set result -> Making and analysing the Confusion Matrix -> Visualising the Training set results -> Visualising the Test set results*

	* **Naive Bayes** 
		* [[Python] Naive Bayes](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/Naive%20Bayes/%5BPython%5D%20Naive%20Bayes.ipynb)
		* [[R] Naive Bayes](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/Naive%20Bayes/%5BR%5D%20Naive%20Bayes.ipynb)

		* **Steps involved**: *Data preprocessing [Here Encoding the target feature as factor is compulsory in R] -> Fitting Naive Bayes to the Training Set -> Predicting the Test set result -> Making and analysing the Confusion Matrix -> Visualising the Training set results -> Visualising the Test set results*

	* **Decision Tree** 
		* [[Python] Decision Tree](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/Decision%20Tree/%5BPython%5D%20Decision%20Tree.ipynb)
		* [[R] Decision Tree](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/Decision%20Tree/%5BR%5D%20Decision%20Tree.ipynb)

		* **Steps involved**: *Data preprocessing [Here we don't actually need Feature Scaling as decison tree classification does not depends on Euclidean distance] -> Fitting Decision Tree to the Training Set -> Predicting the Test set result -> Making and analysing the Confusion Matrix -> Visualising the Training set results -> Visualising the Test set results [ -> Visualize the Decision Tree (in R)]*

	* **Random Forest** 
		* [[Python] Random Forest](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/Random%20Forest/%5BPython%5D%20Random%20Forest.ipynb)
		* [[R] Random Forest](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%203%20-%20Classification/Random%20Forest/%5BR%5D%20Random%20Forest.ipynb)

		* **Steps involved**: *Data preprocessing [Here we don't actually need Feature Scaling as random forest classification does not depends on Euclidean distance] -> Fitting Random Forest to the Training Set -> Predicting the Test set result -> Making and analysing the Confusion Matrix -> Visualising the Training set results -> Visualising the Test set results*

* * *

* **Part 4 - Clustering**
	* **K-Means Clustering** 
		* [[Python] K-Means Clustering](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%204%20-%20Clustering/K-Means%20Clustering/%5BPython%5D%20K-Means%20Clustering.ipynb)
		* [[R] K-Means Clustering](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%204%20-%20Clustering/K-Means%20Clustering/%5BR%5D%20K-Means%20Clustering.ipynb)

		* **Steps involved**: *Data preprocessing -> Using the elbow method to find the optimal number of clusters -> Applying K-Means to the dataset -> Visualizing the clusters -> Analyse*

	* **Hierarchical Clustering** 
		* [[Python] Hierarchical Clustering](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%204%20-%20Clustering/Hierarchical%20Clustering/%5BPython%5D%20Hierarchical%20Clustering.ipynb)
		* [[R] Hierarchical Clustering](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%204%20-%20Clustering/Hierarchical%20Clustering/%5BR%5D%20Hierarchical%20Clustering.ipynb)

		* **Steps involved**: *Data preprocessing -> Using dendrogram to find the optimal number of clusters -> Applying Agglomerative Hierarchical Clustering to the dataset -> Visualizing the clusters -> Analyse*

* * *

* **Part 5 - Association Rule Learning**
	* **Apriori** 
		* [[Python] Apriori](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%205%20-%20Association%20Rule%20Learning/Apriori/%5BPhython%5D%20Apriori.ipynb)
		* [[R] Apriori](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%205%20-%20Association%20Rule%20Learning/Apriori/%5BR%5D%20Apriori.ipynb)

		* **Steps involved**: *Data preprocessing -> Training Apriori on the dataset -> Visualization of the result*

	* **Eclat**
		* [[R] Eclat](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%205%20-%20Association%20Rule%20Learning/Eclat/%5BR%5D%20Eclat.ipynb)

		* **Steps involved**: *Data preprocessing -> Training Eclat on the dataset -> Visualization of the result*

* * *

* **Part 6 - Reinforcement Learning**
	* **Upper Confidence Bound** 
		* [[Python] Upper Confidence Bound](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%206%20-%20Reinforcement%20Learning/Upper%20Confidence%20Bound/%5BPython%5D%20Upper%20Confidence%20Bound.ipynb)
		* [[R] Upper Confidence Bound](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%206%20-%20Reinforcement%20Learning/Upper%20Confidence%20Bound/%5BR%5D%20Upper%20Confidence%20Bound.ipynb)

		* **Steps involved**: *Data preprocessing -> Implementing the Upper Confidence Bound -> Visualization of the result*

* * *

* **Part 7 - Natural Language Processing**
	* [[Python] Natural Language Processing](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%207%20-%20Natural%20Language%20Processing/%5BPython%5D%20Natural%20Language%20Processing.ipynb)

	* [[R] Natural Language Processing](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%207%20-%20Natural%20Language%20Processing/%5BR%5D%20Natural%20Language%20Processing.ipynb)

	* **Steps involved**: *Data preprocessing -> Cleaning the text -> Creating the Bag of Words model -> Splitting the dataset into the Training set and Test set -> Fitting the Training set in some classification model -> Predicting the Test set results -> Making Confusion Matrix -> Analyse*

* * *

* **Part 8 - Deep Learning**
	* **Artificial Neural Network**
		* [[Python] Artificial Neural Network](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%208%20-%20Deep%20Learning/Artificial%20Neural%20Networks/%5BPython%5D%20Artificial%20Neural%20Network.ipynb)

		* [[R] Artificial Neural Network](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%208%20-%20Deep%20Learning/Artificial%20Neural%20Networks/%5BR%5D%20Artificial%20Neural%20Network.ipynb)

		* **Steps involved**: *Data preprocessing -> [**In Python:** Initialization of ANN -> Adding the input layer and the first hidden layer -> Adding more hidden layer(s) inbetween(optional) -> Adding the output layer -> Compiling the ANN] -> Fiting ANN to the Training set [used **keras** for **Python** and **h2o** for **R**] -> Predicting the Test set results -> Making the confussion Matrix -> Calculating Accuracy -> Analyse and Improve if possible*

	* **Convolutional Neural Network**
		* [[Python] Convolutional Neural Network](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%208%20-%20Deep%20Learning/Convolutional%20Neural%20Networks/%5BPython%5D%20Convolutional%20Neural%20Networks.ipynb)

		* **Steps involved**: *Data preprocessing [It is done manually, please refer to notebook for more information] -> Importing the Keras libraries and packages -> Initialising the CNN -> Convolution -> Pooling -> Adding a second convolutional layer followed by pooling(to improve accuracy) -> Flattening -> Full connection -> Compiling the CNN -> Fitting the CNN to the images*

* * *

* **Part 9 - Dimension Reduction**
	* **Principle Component Analysis**
		* [[Python] Principle Component Analysis](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%209%20-%20Dimension%20Reduction/Principal%20Component%20Analysis/%5BPython%5D%20Principal%20Component%20Analysis.ipynb)

		* [[R] Principle Component Analysis](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%209%20-%20Dimension%20Reduction/Principal%20Component%20Analysis/%5BR%5D%20Principal%20Component%20Analysis.ipynb)

		* **Steps involved**: *Data preprocessing -> Applying PCA -> Fitting classifier to the Training Set -> Predicting the Test set result -> Making and analysing the Confusion Matrix -> Visualising the Training set results -> Visualising the Test set results*

	* **Linear Discriminant Analysis**
		* [[Python] Linear Discriminant Analysis](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%209%20-%20Dimension%20Reduction/Linear%20Discriminant%20Analysis/%5BPython%5D%20Linear%20Discriminant%20Analysis.ipynb)

		* [[R] Linear Discriminant Analysis](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%209%20-%20Dimension%20Reduction/Linear%20Discriminant%20Analysis/%5BR%5D%20Linear%20Discriminant%20Analysis.ipynb)

		* **Steps involved**: *Data preprocessing -> Applying LDA -> Fitting classifier to the Training Set -> Predicting the Test set result -> Making and analysing the Confusion Matrix -> Visualising the Training set results -> Visualising the Test set results*

	* **Kernel PCA**
		* [[Python] Kernel PCA](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%209%20-%20Dimension%20Reduction/Kernel%20PCA/%5BPython%5D%20Kernel%20PCA.ipynb)

		* [[R] Kernel PCA](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%209%20-%20Dimension%20Reduction/Kernel%20PCA/%5BR%5D%20Kernel%20PCA.ipynb)

		* **Steps involved**: *Data preprocessing -> Applying Kernel PCA -> Fitting classifier to the Training Set -> Predicting the Test set result -> Making and analysing the Confusion Matrix -> Visualising the Training set results -> Visualising the Test set results*

* * *

* **Part 10 - Model Selection And Boosting**
	* **k-Fold Cross Validation**
		* [[Python] k-Fold Cross Validation](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%2010%20-%20Model%20Selection%20And%20Boosting/k-Fold%20Cross%20Validation/%5BPython%5D%20k-Fold%20Cross%20Validation.ipynb)

		* [[R] k-Fold Cross Validation](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%2010%20-%20Model%20Selection%20And%20Boosting/k-Fold%20Cross%20Validation/%5BR%5D%20k-Fold%20Cross%20Validation.ipynb)

		* **Steps involved**: *Data preprocessing -> Fitting Kernel SVM to the Training Set [Can use some other method] -> Predicting the Test set result -> Applying k-Fold Cross Validation -> Making and analysing the Confusion Matrix -> Visualising the Training set results -> Visualising the Test set results*

	* **Grid Search**
		* [[Python] Grid Search](https://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%2010%20-%20Model%20Selection%20And%20Boosting/Grid%20Search/%5BPython%5D%20Grid%20Search.ipynb)

		* [[R] Grid Search](https://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%2010%20-%20Model%20Selection%20And%20Boosting/Grid%20Search/%5BR%5D%20Grid%20Search.ipynb)

		* **Steps involved**: *Data preprocessing -> Applying Grid Search to find the best model and the best parameters -> Fitting Kernel SVM to the Training Set with best parameters [Can use some other method] -> Predicting the Test set result -> Applying k-Fold Cross Validation -> Making and analysing the Confusion Matrix -> Visualising the Training set results -> Visualising the Test set results*

	* **XGBoost**
		* [[Python] XGBoost](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%2010%20-%20Model%20Selection%20And%20Boosting/XGBoost/%5BPython%5D%20XGBoost.ipynb)

		* [[R] XGBoost](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20A-Z%E2%84%A2%3A%20Hands-On%20Python%20%26%20R%20In%20Data%20Science/Part%2010%20-%20Model%20Selection%20And%20Boosting/XGBoost/%5BR%5D%20XGBoost.ipynb)

		* **Steps involved**: *Data preprocessing -> Fitting XGBoost to the training set -> Predicting the Test set result -> Making and analysing the Confusion Matrix -> Applying k-Fold Cross Validation [get Accuracy and Standard Deviation] -> Applying Grid Search to find the best model and the best parameters (Optional)*

* * *

<a name="importantLinks"></a>
**Important Links**

* [Installing anaconda](https://conda.io/docs/install/quick.html)
* [Installing Python and R using conda](https://uoftcoders.github.io/studyGroup/lessons/r-python-conda-setup/)
* [Using Jupyter notebook](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/)

***
<a name="googleDevelopersMachineLearning"></a>
#### [Google Developers] Machine Learning Crash Course with TensorFlow APIs

* **Descending into ML**
	* [[Check Your Understanding] Descending into ML](https://github.com/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20Crash%20Course%20with%20TensorFlow%20APIs%20Google%20Developers/Descending%20into%20ML/%5BCheck%20Your%20Understanding%5D%20Descending%20into%20ML.pdf)

	* [[Notes] Descending into ML Linear Regression](https://github.com/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20Crash%20Course%20with%20TensorFlow%20APIs%20Google%20Developers/Descending%20into%20ML/%5BNotes%5D%20Descending%20into%20ML%20Linear%20Regression.pdf)

	* [[Notes] Descending into ML Training and Loss](https://github.com/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20Crash%20Course%20with%20TensorFlow%20APIs%20Google%20Developers/Descending%20into%20ML/%5BNotes%5D%20Descending%20into%20ML%20Training%20and%20Loss.pdf)


* **Framing**
	* [[Check Your Understanding] Framing](https://github.com/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20Crash%20Course%20with%20TensorFlow%20APIs%20Google%20Developers/Framing/%5BCheck%20Your%20Understanding%5D%20Framing.pdf)

	* [[Notes] Framing Key ML Terminology](https://github.com/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20Crash%20Course%20with%20TensorFlow%20APIs%20Google%20Developers/Framing/%5BNotes%5D%20Framing%20Key%20ML%20Terminology.pdf)

* **Reducing Loss**
	* [[Check Your Understanding]  Reducing Loss](https://github.com/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20Crash%20Course%20with%20TensorFlow%20APIs%20Google%20Developers/Reducing%20Loss/%5BCheck%20Your%20Understanding%5D%20%20Reducing%20Loss.pdf)

	* [[Notes] Reducing Loss An Iterative Approach](https://github.com/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20Crash%20Course%20with%20TensorFlow%20APIs%20Google%20Developers/Reducing%20Loss/%5BNotes%5D%20Reducing%20Loss%20An%20Iterative%20Approach.pdf)

	* [[Notes] Reducing Loss Gradient Descent](https://github.com/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20Crash%20Course%20with%20TensorFlow%20APIs%20Google%20Developers/Reducing%20Loss/%5BNotes%5D%20Reducing%20Loss%20Gradient%20Descent.pdf)

	* [[Notes] Reducing Loss Learning Rate](https://github.com/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20Crash%20Course%20with%20TensorFlow%20APIs%20Google%20Developers/Reducing%20Loss/%5BNotes%5D%20Reducing%20Loss%20Learning%20Rate.pdf)

	* [[Notes] Reducing Loss Stochastic Gradient Descent](https://github.com/Dibakarroy1997/eternal-learning/blob/master/Machine%20Learning%20Crash%20Course%20with%20TensorFlow%20APIs%20Google%20Developers/Reducing%20Loss/%5BNotes%5D%20Reducing%20Loss%20Stochastic%20Gradient%20Descent.pdf)


<a name="languages"></a>
## Language

***

<a name="python"></a>
#### Python 

***

<a name="lpthw"></a>
* **Learn Python The Hard Way**
	* [Exercise 1: A Good First Program](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/LPTHW/Learn_Python_the_Hard_Way_Exercise_Notebook.ipynb#Exercise-1-(A-Good-First-Program))

	* [Exercise 2: Comments And Pound Characters](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/LPTHW/Learn_Python_the_Hard_Way_Exercise_Notebook.ipynb#Exercise-2-(Comments-and-Pound-Characters))

	* [Exercise 3: Numbers And Math](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/LPTHW/Learn_Python_the_Hard_Way_Exercise_Notebook.ipynb#Exercise-3-(Numbers-and-Math))

	* [Exercise 4: Variables And Names](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/LPTHW/Learn_Python_the_Hard_Way_Exercise_Notebook.ipynb#Exercise-4-(Variables-and-Names))

	* [Exercise 5: More Variables And Printing](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/LPTHW/Learn_Python_the_Hard_Way_Exercise_Notebook.ipynb#Exercise-5-(More-Variables-and-Printing))

	* [Exercise 6: Strings And Text](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/LPTHW/Learn_Python_the_Hard_Way_Exercise_Notebook.ipynb#Exercise-6-(Strings-and-Text))

	* [Exercise 7: More Printing](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/LPTHW/Learn_Python_the_Hard_Way_Exercise_Notebook.ipynb#Exercise-7-(More-Printing))

	* [Exercise 8: Printing, Printing](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/LPTHW/Learn_Python_the_Hard_Way_Exercise_Notebook.ipynb#Exercise-8-(Printing,-Printing))

	* [Exercise 9: Printing, Printing, Printing](http://nbviewer.jupyter.org/github/Dibakarroy1997/eternal-learning/blob/master/LPTHW/Learn_Python_the_Hard_Way_Exercise_Notebook.ipynb#Exercise-9-(Printing,-Printing,-Printing))

	* (-)[Exercise 10: What Was That?]()

	* [Exercise 11: Asking Questions](https://github.com/Dibakarroy1997/eternal-learning/tree/master/LPTHW/ex11)

	* [Exercise 12: Prompting People](https://github.com/Dibakarroy1997/eternal-learning/tree/master/LPTHW/ex12)

	* [Exercise 13: Parameters, Unpacking, Variables](https://github.com/Dibakarroy1997/eternal-learning/tree/master/LPTHW/ex13)

	* [Exercise 14: Prompting And Passing](https://github.com/Dibakarroy1997/eternal-learning/tree/master/LPTHW/ex14)

	* [Exercise 15: Reading Files](https://github.com/Dibakarroy1997/eternal-learning/tree/master/LPTHW/ex15)

	* [Exercise 16: Reading And Writing Files](https://github.com/Dibakarroy1997/eternal-learning/tree/master/LPTHW/ex16)

	* [Exercise 17: More Files](https://github.com/Dibakarroy1997/eternal-learning/tree/master/LPTHW/ex17)

	* (-)[Exercise 18: Names, Variables, Code, Functions]()

	* (-)[Exercise 19: Functions And Variables]()

	* (-)[Exercise 20: Functions And Files]()

	* (-)[Exercise 21: Functions Can Return Something]()

	* (-)[Exercise 22: What Do You Know So Far?]()

	* (-)[Exercise 23: Read Some Code]()

	* (-)[Exercise 24: More Practice]()

	* (-)[Exercise 25: Even More Practice]()

	* (-)[Exercise 26: Congratulations, Take A Test!]()

	* (-)[Exercise 27: Memorizing Logic]()

	* (-)[Exercise 28: Boolean Practice]()

	* (-)[Exercise 29: What If]()

	* (-)[Exercise 30: Else And If]()

	* (-)[Exercise 31: Making Decisions]()

	* (-)[Exercise 32: Loops And Lists]()

	* (-)[Exercise 33: While Loops]()

	* (-)[Exercise 34: Accessing Elements Of Lists]()

	* (-)[Exercise 35: Branches and Functions]()

	* (-)[Exercise 36: Designing and Debugging]()

	* (-)[Exercise 37: Symbol Review]()

	* (-)[Exercise 38: Doing Things To Lists]()

	* (-)[Exercise 39: Dictionaries, Oh Lovely Dictionaries]()

	* (-)[Exercise 40: Modules, Classes, And Objects]()

	* (-)[Exercise 41: Learning To Speak Object Oriented]()

	* (-)[Exercise 42: Is-A, Has-A, Objects, and Classes]()

	* (-)[Exercise 43: Gothons From Planet Percal #25]()

	* (-)[Exercise 44: Inheritance Vs. Composition]()

	* (-)[Exercise 45: You Make A Game]()

	* (-)[Exercise 46: A Project Skeleton]()

	* (-)[Exercise 47: Automated Testing]()

	* (-)[Exercise 48: Advanced User Input]()

	* (-)[Exercise 49: Making Sentences]()

	* (-)[Exercise 50: Your First Website]()

	* (-)[Exercise 51: Getting Input From A Browser]()

	* (-)[Exercise 52: The Start Of Your Web Game]()
***

<a name="myBlog"></a>
## My Blog

[BakaDigest](https://dibakarroy1997.github.io/BakaDigest/)

***

Respository created on: 9th June 2018