library(FactoMineR)
library(DMwR2)
library(readxl)
library(factoextra)
library(cluster)
data <- read_excel("C:/Users/JAVI/Downloads/Minería/Dataset_Mineria.xlsx")
head(data)
my_data<-data[,-c(1,2,3,4,5,6,8)]
my_data <- knnImputation(my_data,k=10)
my_dataCE = scale(my_data, center = TRUE, scale = TRUE)
PCA_Data <- princomp(my_dataCE, cor= T, scores=T)
objects(PCA_Data)
scores <- PCA_Data$scores[,1:10]

################################
#fuzzy clustering
####################################
fuzzy_cluster <- fanny(x = scores, k = 3, diss = FALSE,memb.exp = 3, metric = "SqEuclidean",
                       stand = FALSE, maxit=1000,tol=10^(-5))

fuzzy_cluster$membership
fuzzy_cluster$clustering

#prÃ³ximos a 0 indican que la estructura tiene un alto nivel fuzzy y valores prÃ³ximos a 1 lo contrario.
fuzzy_cluster$coeff
fviz_cluster(object = fuzzy_cluster, repel = TRUE, ellipse.type = "norm",
             pallete = "jco") + theme_bw() + labs(title = "Fuzzy Cluster plot")


