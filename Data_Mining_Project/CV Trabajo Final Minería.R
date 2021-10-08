library("readxl")
library(fastDummies)
library(rpart)
library(DMwR2)
library(class)
library (e1071)
library("kernlab")
library(randomForest)
library(ipred)
library(neuralnet)
library(adabag)
library(mdatools)
my_data <- read_excel("Dataset_Mineria.xlsx")
my_data<-my_data[,-c(1,2,3,5,6,8)]
my_data<-my_data[-c(1017,1166),]
my_dataImp<-knnImputation(my_data[,-c(1)],k=10)
summary(my_data)
tasa.aciertos.tree<-NA
tasa.aciertos.knn<-NA
tasa.aciertos.nbayes<-NA
tasa.aciertos.nbayes.laplace<-NA
tasa.aciertos.svm<-NA
tasa.aciertos.svp<-NA
tasa.aciertos.rf<-NA
tasa.aciertos.nn<-NA
tasa.aciertos.pls<-NA
tasa.aciertos.simca<-NA
tasa.aciertos.bag<-NA
tasa.aciertos.bot<-NA

my_dataCE<- scale(my_dataImp, center = TRUE, scale = TRUE)
PCA_Data <- princomp(my_dataCE, cor= T, scores=T)
scores <- PCA_Data$scores[,1:10]
my_dataCE<-cbind(my_data[,c(1)],my_dataCE)
matriz<-cbind(my_data[,c(1)],scores)

cjo<-sample(1:nrow(my_data),nrow(my_data), FALSE) 
seq(1,1437, 143)
for(i in 1:10){
  if(i==10){
    datos.entrenamiento<- matriz[-cjo[(9*143+1):1437],]
    datos.validacion<- matriz[cjo[(9*143+1):1437],]
  }else{
  datos.entrenamiento<- matriz[-cjo[(143*(i-1)+1):(i*143)],]
  datos.validacion<- matriz[cjo[(143*(i-1)+1):(i*143)],]
  }
  
  ########################
  #CLASSIFICATION TREES
  ########################
  
  tree3<-rpartXse(factor(Posc)~ . ,data=datos.entrenamiento, se = 0.5) 
  
  pred <- predict(tree3, datos.validacion[,-c(1)],type = "class")
  tab <- table(pred, datos.validacion$Posc) 
  tab
  tasa.aciertos.tree[i]<-sum(tab[row(tab)==col(tab)])/sum(tab)
  
  ########################
  #RANDOM FOREST
  ########################
  rf<-randomForest(factor(Posc) ~ ., data = datos.entrenamiento, mtry=3,
                   method="class",importance=TRUE)
  
  pred<- predict(rf, datos.validacion[,-c(1)])
  #matriz de confusión
  tab <- table(pred, datos.validacion$Posc)
  tab
  #tasa de acierto
  tasa.aciertos.rf[i]<-sum(tab[row(tab)==col(tab)])/sum(tab)
  
  #######################
  #vecino mas proximo
  #####################
  datos.entrenamiento$Posc<-factor(datos.entrenamiento$Posc)
  vecino<-knn(datos.entrenamiento[,-c(1)], datos.validacion[,-c(1)], datos.entrenamiento$Posc, k = 3, prob = TRUE)
  
  tab<-table(factor(datos.validacion$Posc),vecino)
  tab
  tasa.aciertos.knn[i]<-sum(tab[row(tab)==col(tab)])/sum(tab)
  
  #################
  #Naive Bayes
  ###########
  
  nbayes <- naiveBayes(factor(Posc)~ ., data=datos.entrenamiento) 
  pred <- predict(nbayes, datos.validacion[,-c(1)])
  tab <- table(pred, datos.validacion$Posc) 
  tab
  tasa.aciertos.nbayes[i]<-sum(tab[row(tab)==col(tab)])/sum(tab)
  
  ## using Laplace smoothing: 
  model <- naiveBayes(factor(Posc)~ ., data=datos.entrenamiento, laplace = 3)
  pred <- predict(model, datos.validacion[,-c(1)]) 
  tab <- table(pred, datos.validacion$Posc) 
  tab
  tasa.aciertos.nbayes.laplace[i]<-sum(tab[row(tab)==col(tab)])/sum(tab)
  
  #############
  #SVM
  #############
  svp <- ksvm(factor(Posc)~ ., data=datos.entrenamiento, type = "C-svc", kernel = "rbfdot",kpar = "automatic")
  pred <- predict(svp, datos.validacion[,-c(1)]) 
  tab <- table(pred, datos.validacion$Posc) 
  tab
  tasa.aciertos.svp[i]<-sum(tab[row(tab)==col(tab)])/sum(tab)
  
  model.svm <- svm(factor(Posc)~ ., data = datos.entrenamiento, method = "C-classification", kernel = "radial",cost = 10, gamma = 0.1)
  pred <- predict(model.svm, datos.validacion[,-c(1)]) 
  tab <- table(pred, datos.validacion$Posc) 
  tab
  tasa.aciertos.svm[i]<-sum(tab[row(tab)==col(tab)])/sum(tab)
  
  #############
  #Redes Neuronales
  #############
  modelo.nn<-neuralnet(Posc~.,
                       data          = datos.entrenamiento,
                       threshold = 0.01,
                       hidden        = c(60),
                       linear.output = FALSE )
  # Red
  pred<-predict(modelo.nn,datos.validacion[,-c(1)])
  tab <- table(apply(pred, 1, which.max), datos.validacion$Posc) 
  tab
  tasa.aciertos.nn[i]<-sum(tab[row(tab)==col(tab)])/sum(tab)
  
  #############
  #PLS
  #############
  if(i==10){
    datos.entrenamientoPLS<- my_dataCE[-cjo[(9*143+1):1437],]
    datos.validacionPLS<- my_dataCE[cjo[(9*143+1):1437],]
  }else{
    datos.entrenamientoPLS<- my_dataCE[-cjo[(143*(i-1)+1):(i*143)],]
    datos.validacionPLS<- my_dataCE[cjo[(143*(i-1)+1):(i*143)],]
  }
  cc.all<-datos.entrenamiento[,c(1)]
  modelo.pls<-plsda(datos.entrenamientoPLS[,-c(1)], cc.all, ncomp = 13,cv=1)
  res<-predict(modelo.pls, datos.validacionPLS[,-c(1)], datos.validacionPLS$Posc,type="class")
  tab <- getConfusionMatrix(res)
  tab
  tasa.aciertos.pls[i]<-sum(tab[row(tab)==col(tab)])/sum(tab)
  tasa.fallos.pls<-sum(tab[row(tab)!=col(tab)])/sum(tab)
  
  #############
  #Simca
  #############
  if(i==10){
    datos.entrenamientoPCA1<- my_dataCE[-cjo[(9*143+1):1437],]
    datos.validacionPCA<- my_dataCE[cjo[(9*143+1):1437],]
  }else{
    datos.entrenamientoPCA1<- my_dataCE[-cjo[(143*(i-1)+1):(i*143)],]
    datos.validacionPCA<- my_dataCE[cjo[(143*(i-1)+1):(i*143)],]
  }
  datos.entrenamientoCC<-datos.entrenamientoPCA1[datos.entrenamientoPCA1$Posc=="CC",-c(1)]
  clases.CC<-datos.entrenamientoPCA1[datos.entrenamientoPCA1$Posc=="CC",c(1)]
  
  datos.entrenamientoDF<-datos.entrenamientoPCA1[datos.entrenamientoPCA1$Posc=="DF",-c(1)]
  clases.DF<-datos.entrenamientoPCA1[datos.entrenamientoPCA1$Posc=="DF",c(1)]
  
  datos.entrenamientoDL<-datos.entrenamientoPCA1[datos.entrenamientoPCA1$Posc=="DL",-c(1)]
  clases.DL<-datos.entrenamientoPCA1[datos.entrenamientoPCA1$Posc=="DL",c(1)]
  
  modelo.simca.CC <- simca(datos.entrenamientoCC, "CC", ncomp = 10, cv = 1)
  modelo.simca.DF <- simca(datos.entrenamientoDF, "DF", ncomp = 10, cv = 1)
  modelo.simca.DL <- simca(datos.entrenamientoCC, "DL", ncomp = 10, cv = 1)
  
  modelo.simca<-simcam(list(modelo.simca.CC, modelo.simca.DF, modelo.simca.DL))
  res<-predict(modelo.simca, datos.validacionPCA[,-c(1)], datos.validacionPCA$Posc)
  tab <- getConfusionMatrix(res)
  tab
  tasa.aciertos.simca[i]<-sum(tab[row(tab)==col(tab)])/sum(tab)
  
  #############
  #Bagging
  #############
  datos.entrenamiento$Posc<-factor(datos.entrenamiento$Posc)
  bag.Posc<- bagging(Posc ~., data=datos.entrenamiento, coob=TRUE)#no puedes ponerle el factor dentro de la fórmula da error
  
  pred <- predict(bag.Posc, datos.validacion[,-c(1)]) #para predecir hemos de quitar la clasificación que ocupa el lugar 8
  #matriz de confusión
  tab <- table(pred$class, datos.validacion$Posc)
  tab
  #tasa de acierto
  tasa.aciertos.bag[i]<-sum(tab[row(tab)==col(tab)])/sum(tab)
  
  #############
  #Boosting
  #############
  datos.entrenamiento$Posc<-factor(datos.entrenamiento$Posc)
  bot.Posc<- boosting(Posc ~., data=datos.entrenamiento, coob=TRUE)
  
  pred <- predict(bot.Posc, datos.validacion[,-c(1)]) #pred es una lista y has que acceder a las clase predicha
  #matriz de confusión
  tab <- table(pred$class, datos.validacion$Posc) #tabla cruzada de predicciones y clasificación real
  tab
  #tasa de acierto
  tasa.aciertos.bot[i]<-sum(tab[row(tab)==col(tab)])/sum(tab)
}
tasa<-cbind(tasa.aciertos.tree,tasa.aciertos.knn,tasa.aciertos.nbayes,
            tasa.aciertos.nbayes.laplace,tasa.aciertos.svm,
            tasa.aciertos.svp,tasa.aciertos.rf,tasa.aciertos.nn,
            tasa.aciertos.pls,tasa.aciertos.simca,
            tasa.aciertos.bag,tasa.aciertos.bot)
tasa
tasa.mean<-apply(tasa,2, mean)
tasa.mean
write.table(tasa.mean, file = "tasas_mediasCV", append = FALSE, quote = TRUE, sep = " ", row.names = TRUE, col.names = TRUE)
tasa.int<-apply(tasa,2, quantile, probs=c(0.025,0.975))
tasa.int
write.table(tasa.int, file = "tasas_intervalosCV", append = FALSE, quote = TRUE, sep = " ", row.names = TRUE, col.names = TRUE)

vector.tasa<-as.vector(tasa)
#al convertirlo en vector pone una columna debajo de la otra
cbind(vector.tasa[1:10], tasa[,1])
metodo<-rep(c("tree","knn","nbayes","nbayes.laplace","svm","svp","rf","nn","pls","simca", "bagging", "boosting"), each=10)
plot(factor(metodo),vector.tasa)
#los dos con mejores resultados son nbayes.laplace y svp
#veamos si hay diferencias significativas y cual es mejor
test1<-t.test(tasa[metodo=="boosting"], tasa[metodo=="rf"], alternative = c("two.sided", "less", "greater"), paired = TRUE, var.equal = FALSE, conf.level = 0.95)
test2<-t.test(tasa[metodo=="boosting"], tasa[metodo=="svp"], alternative = c("two.sided", "less", "greater"), paired = TRUE, var.equal = FALSE, conf.level = 0.95)
test3<-t.test(tasa[metodo=="boosting"], tasa[metodo=="nbayes"], alternative = c("two.sided", "less", "greater"), paired = TRUE, var.equal = FALSE, conf.level = 0.95)
test<-cbind(test1,test2,test3)
write.table(test, file = "testmediasCV", append = FALSE, quote = TRUE, sep = " ", row.names = TRUE, col.names = TRUE)
