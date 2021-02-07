# BreastCancerClassification
Course Project of IEE-03 Artificial Neural Networks 

## Abstract 
The project aims to develop classifierfor Classification of Breast Tumor into Malignant ( cancer tumor) and Benign (non cancer tumor) using features obtained from several cell images The dataset we used for this purpose was Breast Cancer Wisconsin dataset from Scikit Learn The classification process was carried out by three models, Support Vector Machine(SVM), Neural Network (with Particle Swarm Optimizer), and Neural Network (with Gradient Descent). The main bjective is to compare these three models and find the most suitable model.<br>
<br>
## Introduction
Breast cancer is the most common cancer amongst women in the world. It accounts for 25% of all cancer cases, and affected over 2.1 Million people in 2015 alone. It starts when
cells in the breast begin to grow out of control. These cells usually form tumors that can be seen via X ray or felt as lumps in the breast area. <br>
Early diagnosis significantly increases the chances of survival. The key challenge against its detection is how to classify tumors into malignant (cancerous) or benign (non cancerous). A tumor is considered malignant if the cells can grow into surrounding tissues or spread to distant areas of the body. A benign tumor does not invade nearby tissue nor spread to other parts of the body the way cancerous tumors can. But benign tumors can be serious if they press on vital structures such as blood vessels or nerves. <br>
Machine Learning technique can dramatically improve the level of diagnosis in breast cancer. Research shows that experienced physicians can detect cancer by 79% accuracy, while a 91% (sometimes up to 97%) accuracy can be achieved using Machine Learning techniques. <br>
<br>
## Dataset
In this study, our task is to classify tumors into malignant (cancerous) or benign (non-cancerous) using features obtained from several cell images. The dataset was originally developed by Dr. William H. Wolberg, W. Nick Street, and Olvi L. Mangasarian from University of Wisconsin and is famously know as “Breast Cancer Wisconsin Dataset”. Features are computed from a digitized image of a Fine Needle Aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image. <br>
The dataset has <b>569 instances, 357 for benign and 212 for malignant</b>. There are <b>30 features</b> in the dataset each of which is described below: -<br>
1.	mean radius = mean of distances from center to points on the perimeter
2.	mean texture = standard deviation of gray-scale values
3.	mean perimeter = mean size of the core tumor
4.	mean area 
5.	mean smoothness = mean of local variation in radius lengths
6.	mean compactness = mean of perimeter^2 / area - 1.0
7.	mean concavity = mean of severity of concave portions of the contour
8.	mean concave points = mean for number of concave portions of the contour
9.	mean symmetry 
10.	mean fractal dimension = mean for "coastline approximation" – 1
11.	radius error = standard error for the mean of distances from center to points on the perimeter
12.	texture error = standard error for standard deviation of gray-scale values
13.	perimeter error 
14.	area error 
15.	smoothness error = standard error for local variation in radius lengths
16.	compactness error = standard error for perimeter^2 / area - 1.0
17.	concavity error = standard error for severity of concave portions of the contour
18.	concave points error = standard error for number of concave portions of the contour
19.	symmetry error 
20.	fractal dimension error = standard error for "coastline approximation" – 1
21.	worst radius = "worst" or largest mean value for mean of distances from center to points on the perimeter
22.	worst texture = "worst" or largest mean value for standard deviation of gray-scale values
23.	worst perimeter 
24.	worst smoothness = "worst" or largest mean value for local variation in radius lengths
25.	worst compactness = "worst" or largest mean value for perimeter^2 / area - 1.0
26.	worst concavity = "worst" or largest mean value for severity of concave portions of the contour
27.	worst concave points = "worst" or largest mean value for number of concave portions of the contour
28.	worst fractal dimension = "worst" or largest mean value for "coastline approximation" – 1<br>
<br>


