library("readxl")
library(DMwR2)
my_data <- read_excel("Dataset_MOD.xlsx")
my_dataImp<-knnImputation(my_data[,-c(1,2,3,4,5,6,8)],k=10)
my_data<-cbind(my_data[,c(1,2,3,4,5,6)],my_dataImp[,c(1)],my_data[,c(8)],my_dataImp[,c(2:41)])
cjo<-sample(1:1439,1079, FALSE) #se selecciona el 75% datos=1079,25=1079

datos.entrenamiento<-my_data[cjo,]
datos.validacion<-my_data[-cjo,]
write.csv2(datos.entrenamiento,"datos_entrenamiento.csv")
write.csv2(datos.validacion,"datos_validacion.csv")
