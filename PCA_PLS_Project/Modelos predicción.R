library("readxl")
library(rpart)
library(rpart.plot)
library(DMwR2)
library(class)
library (e1071)
library("kernlab")
library(randomForest)
library(ipred)
library(neuralnet)
library(adabag)
library(mdatools)
set.seed(12345)
datos.entrenamiento <- read_excel("Dataset_MOD_entrenamiento.xlsx")
datos.validacion <- read_excel("Dataset_MOD_validacion.xlsx")

datos.entrenamiento1<-datos.entrenamiento[,-c(1,2,3,4,5,6,8)]
datos.validacion1<-datos.validacion[,-c(1,2,3,4,5,6,8)]

datos_entrenamientoCE<- scale(datos.entrenamiento1[-c(516),], center = TRUE, scale = TRUE)
datos_validacionCE<- scale(datos.validacion1[-c(297),], center = TRUE, scale = TRUE)
PCA_Data <- princomp(datos_entrenamientoCE, cor= T, scores=T)
scores <- PCA_Data$scores[,1:10]
loadings<-PCA_Data$loadings[,1:10]
scores_valid<-datos_validacionCE%*%loadings
datos.entrenamientoS<-cbind(datos.entrenamiento[-c(516),c(4)],scores)
datos.validacionS<-cbind(datos.validacion[-c(297),c(4)],scores_valid)

########################
#CLASSIFICATION TREES
########################

tree1<-rpartXse(factor(Posc)~ . ,data=datos.entrenamientoS, se = 1) 
X11()
prp(tree1,extra=101)

pred <- predict(tree1, datos.validacionS[,-c(1)],type = "class")
tab <- table(pred, datos.validacionS$Posc) 
tab
tasa.aciertos.tree1<-sum(tab[row(tab)==col(tab)])/(sum(tab)+1)

tree2<-rpartXse(factor(Posc)~ . ,data=datos.entrenamientoS, se = 0.5) 
X11()
prp(tree2,extra=101)

pred <- predict(tree2, datos.validacionS[,-c(1)],type = "class")
tab <- table(pred, datos.validacionS$Posc) 
tab
tasa.aciertos.tree2<-sum(tab[row(tab)==col(tab)])/(sum(tab)+1)

########################
#RANDOM FOREST
########################
rf<-randomForest(factor(Posc) ~ ., data = datos.entrenamientoS, mtry=3,
                 method="class",importance=TRUE)

pred<- predict(rf, datos.validacionS[,-c(1)])
#matriz de confusión
tab <- table(pred, datos.validacionS$Posc)
tab
#tasa de acierto
tasa.aciertos.rf<-sum(tab[row(tab)==col(tab)])/(sum(tab)+1)

importance(rf)
# Plot variable importance
varImpPlot(rf, main="",col="dark blue")
varImpPlot(rf, main="",col="dark blue", type=1)
varImpPlot(rf, main="",col="dark blue", type=2)
varImpPlot(rf, main="",col="dark blue", class=TRUE)

#######################
#vecino mas proximo
#####################
datos.entrenamientoS$Posc<-factor(datos.entrenamientoS$Posc)
vecino<-knn(datos.entrenamientoS[,-c(1)], datos.validacionS[,-c(1)], datos.entrenamientoS$Posc, k = 3, prob = TRUE)

tab<-table(factor(datos.validacionS$Posc),vecino)
tab
tasa.aciertos.knn<-sum(tab[row(tab)==col(tab)])/(sum(tab)+1)

#################
#Naive Bayes
###########

nbayes <- naiveBayes(factor(Posc)~ ., data=datos.entrenamientoS) 
pred <- predict(nbayes, datos.validacionS[,-c(1)])
tab <- table(pred, datos.validacionS$Posc) 
tab
tasa.aciertos.nbayes<-sum(tab[row(tab)==col(tab)])/(sum(tab)+1)

## using Laplace smoothing: 
model <- naiveBayes(factor(Posc)~ ., data=datos.entrenamientoS, laplace = 3)
pred <- predict(model, datos.validacionS[,-c(1)]) 
tab <- table(pred, datos.validacionS$Posc) 
tab
tasa.aciertos.nbayes.laplace<-sum(tab[row(tab)==col(tab)])/(sum(tab)+1)

#############
#SVM
#############
svp <- ksvm(factor(Posc)~ ., data=datos.entrenamientoS, type = "C-svc", kernel = "rbfdot",kpar = "automatic")
pred <- predict(svp, datos.validacionS[,-c(1)]) 
tab <- table(pred, datos.validacionS$Posc) 
tab
tasa.aciertos.svp<-sum(tab[row(tab)==col(tab)])/(sum(tab)+1)

model.svm <- svm(factor(Posc)~ ., data = datos.entrenamientoS, method = "C-classification", kernel = "radial",cost = 10, gamma = 0.1)
pred <- predict(model.svm, datos.validacionS[,-c(1)]) 
tab <- table(pred, datos.validacionS$Posc) 
tab
tasa.aciertos.svm<-sum(tab[row(tab)==col(tab)])/(sum(tab)+1)

#############
#Redes Neuronales
#############
modelo.nn<-neuralnet(Posc~.,
                     data          = datos.entrenamientoS,
                     hidden        = c(60),
                     linear.output = FALSE )
# Red
pred<-predict(modelo.nn,datos.validacionS[,-c(1)])
tab <- table(apply(pred, 1, which.max), datos.validacionS$Posc) 
tab
tasa.aciertos.nn<-sum(tab[row(tab)==col(tab)])/(sum(tab)+1)

#############
#Bagging
#############
datos.entrenamientoS$Posc<-factor(datos.entrenamientoS$Posc)
bag.Posc<- bagging(Posc ~., data=datos.entrenamientoS, coob=TRUE)

pred <- predict(bag.Posc, datos.validacionS[,-c(1)]) #para predecir hemos de quitar la clasificación que ocupa el lugar 8
#matriz de confusión
tab <- table(pred$class, datos.validacionS$Posc)
tab
#tasa de acierto
tasa.aciertos.bag<-sum(tab[row(tab)==col(tab)])/(sum(tab)+1)

#############
#Boosting
#############
datos.entrenamientoS$Posc<-factor(datos.entrenamientoS$Posc)
bot.Posc<- boosting(Posc ~., data=datos.entrenamientoS, coob=TRUE)

pred <- predict(bot.Posc, datos.validacionS[,-c(1)]) #pred es una lista y has que acceder a las clase predicha
#matriz de confusión
tab <- table(pred$class, datos.validacionS$Posc) #tabla cruzada de predicciones y clasificación real
tab
#tasa de acierto
tasa.aciertos.bot<-sum(tab[row(tab)==col(tab)])/(sum(tab)+1)



tasa<-cbind(tasa.aciertos.tree1,tasa.aciertos.tree2,tasa.aciertos.knn,
            tasa.aciertos.nbayes,tasa.aciertos.nbayes.laplace,
            tasa.aciertos.svm,tasa.aciertos.svp,tasa.aciertos.rf,
            tasa.aciertos.nn,tasa.aciertos.bag,tasa.aciertos.bot)
tasa
