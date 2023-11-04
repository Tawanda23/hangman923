import seaborn as sns

#iris.df = sns.load_dataset("iris") ['sepal_length', 'sepal_width']
#print(iris_df.columns) #this prints the columns in the data

#stores only species info
#species = iris.df['species']


#stores petals than are smaller than 4.5
#small_petal_length = iris.df[iris_df["sepal_length"] , 4.5]


#using FOR loop
#for flower in species:
    #print(flower)

#store the mea for sepal width per species
#mean_sepal_width = iris_df.groupby("species")[sepal_width]


#to print stuff using MATPLOTLIB
#plt.figure()

#sns.barplot(x="species", y="sepal_widthj", data=iris_df)

#plt.show()