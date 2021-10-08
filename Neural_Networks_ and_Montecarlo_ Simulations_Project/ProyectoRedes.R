# PROYECTO PARA LA ASIGNATURA DE SIMULACION Y REDES NEURONALES
# AUTOR: JAVIER PORCEL MARI
# MASTER EN INGENIERIA DE ANALISIS DE DATOS UPV
# PRIMERA PARTE

# CARGAR LIBRERIAS
library(ggplot2)
library(neuralnet) 
library(readr)

# CARGAR DATOS DE UN CSV
datos <- read_csv("healthcare-dataset-stroke-data.csv")

# ELIMINAR VALORES FALTANTES DE BMI
datos <- datos[datos$bmi != "N/A", ]

# CONVERTIR BMI A COLUMNA NUMERICA
datos$bmi <- as.numeric(datos$bmi)

# ELIMINAR VALORES FALTANTES DE smoking_status.
datos <- datos[datos$smoking_status != "Unknown", ]

# ELIMINAR COLUMNA ID
datos <- datos[, -c(1)]

# ELIMINAR VALORES FALTANTES DE gender
datos <- datos[datos$gender != "Other", ]

# CONVERTIR gender EN UNA VARIABLE DUMMY
datos$gender <- as.factor(datos$gender)
gender_dummies <- model.matrix(~ gender, datos)
datos$gender <- gender_dummies[, c(2)]


# CONVERTIR hypertension EN UNA COLUMNA NUMERICA
datos$hypertension <- as.numeric(datos$hypertension)

# CONVERTIR heart_disease EN UNA COLUMNA NUMERICA
datos$heart_disease <- as.numeric(datos$heart_disease)

# CONVERTIR ever_married EN COLUMNAS DUMMY
datos$ever_married <- as.factor(datos$ever_married)
ever_married_dummies <- model.matrix(~ ever_married, datos)
datos$ever_married <- ever_married_dummies[, c(2)]

# CONVERTIR work_type EN COLUMNAS DUMMY
datos$work_type <- as.factor(datos$work_type)
work_type_dummies <- model.matrix(~ work_type-1, datos)
datos$work_children <- work_type_dummies[, c(1)]
datos$work_Govt <- work_type_dummies[, c(2)]
datos$work_Never <- work_type_dummies[, c(3)]
datos$work_Private <- work_type_dummies[, c(4)]
datos$work_Self <- work_type_dummies[, c(5)]
datos <- datos[, -c(6)]


# CONVERTIR Residence_type EN COLUMNAS DUMMY
datos$Residence_type <- as.factor(datos$Residence_type)
Residence_type_dummies <- model.matrix(~ Residence_type, datos)
datos$Residence_type <- Residence_type_dummies[, c(2)]

# CONVERTIR smoking_status EN COLUMNAS DUMMY
datos$smoking_status <- as.factor(datos$smoking_status)
smoking_status_dummies <- model.matrix(~ smoking_status-1, datos)
datos$smoking_formerly <- smoking_status_dummies[, c(1)]
datos$smoking_never <- smoking_status_dummies[, c(2)]
datos$smoking_smokes <- smoking_status_dummies[, c(3)]
datos <- datos[, -c(9)]

# REORDENAR LA MATRIZ
datos <- datos[, c(1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 6, 7, 8, 15, 16, 17, 9)]

# BORRAR VECTORES Y MATRICES AUXILIARES
rm(gender_dummies)
rm(ever_married_dummies)
rm(work_type_dummies)
rm(Residence_type_dummies)
rm(smoking_status_dummies)

# ELIMINAR VALORES ATIPICOS Y LA VARIABLE work_never
datos <- datos[-c(420, 628, 678, 1222, 1310,1591, 1837, 1881, 2150, 2329,2718, 2780, 3085, 3212),-c(8)]




# DIVISION DE DATOS EN ENTRENAMIENTO Y VALIDACION CON oversampling
train.index <- sample(c(1:dim(datos)[1]),replace=FALSE, dim(datos)[1]*0.6)  
train.df <- datos[train.index, ]
table(train.df$stroke)

valid.df <- datos[-train.index, ]
table(valid.df$stroke)
filas<-NA
w<-1
for (i in 1:nrow(train.df)){
  if (train.df$stroke[i]==1){
    filas[w]<-i
    w<-w+1
  }
}
numc0<-nrow(train.df[train.df$stroke==0,])
s<-sample(filas, replace=TRUE, numc0)
train.bal.df<-rbind(train.df[train.df$stroke==0,], train.df[s,])
table(train.bal.df$stroke)

train<-train.bal.df
test<-valid.df

# NORMALIZACION DE VARIABLES
maxs      <- apply(train, 2, max)
mins      <- apply(train, 2, min)
train_nrm <- as.data.frame(scale(train, center = mins, scale = maxs - mins))
test_nrm <- as.data.frame(scale(test, center = mins, scale = maxs - mins))
table(train_nrm$stroke)
table(test_nrm$stroke)

# FORMULA
nms  <- names(train_nrm)
frml <- as.formula(paste("stroke ~", paste(nms[!nms %in% "stroke"], collapse = " + ")))

#MODELO 1
modelo1.nn<-neuralnet(frml,
                      data          = train_nrm,
                      threshold = 0.8 ,
                      hidden        = c(25),
                      linear.output = FALSE )
plot(modelo1.nn, radius = 0.1)
pred1_nrm <- predict(modelo1.nn, test_nrm[,-c(16)],type = "class")
pred1<- (pred1_nrm)*(max(datos$stroke)-min(datos$stroke))+min(datos$stroke)
roundpred1<-sapply(pred1,round,digits=0)
tab <- table(roundpred1, test$stroke) 
tab
tasa.aciertos.nn1<-sum(tab[row(tab)==col(tab)])/sum(tab)
sensibilidad.nn1 <-tab[2,2]/(tab[1,2]+tab[2,2])
especificidad.nn1 <-tab[1,1]/(tab[1,1]+tab[2,1])

#MODELO 2
modelo2.nn<-neuralnet(frml,
                      data          = train_nrm,
                      threshold=0.8,
                      hidden        = c(20, 5),
                      linear.output = FALSE )
plot(modelo2.nn)
pred2_nrm <- predict(modelo2.nn, test_nrm[,-c(16)],type = "class")
pred2<- (pred2_nrm)*(max(datos$stroke)-min(datos$stroke))+min(datos$stroke)
roundpred2<-sapply(pred2,round,digits=0)
tab <- table(roundpred2, test$stroke) 
tab
tasa.aciertos.nn2<-sum(tab[row(tab)==col(tab)])/sum(tab)
sensibilidad.nn2 <-tab[2,2]/(tab[1,2]+tab[2,2])
especificidad.nn2 <-tab[1,1]/(tab[1,1]+tab[2,1])

#MODELO 3
modelo3.nn<-neuralnet(frml,
                      data          = train_nrm,
                      threshold=0.8,
                      hidden        = c(15, 10),
                      linear.output = FALSE )
plot(modelo3.nn)
pred3_nrm <- predict(modelo3.nn, test_nrm[,-c(16)],type = "class")
pred3<- (pred3_nrm)*(max(datos$stroke)-min(datos$stroke))+min(datos$stroke)
roundpred3<-sapply(pred3,round,digits=0)
tab <- table(roundpred3, test$stroke) 
tab
tasa.aciertos.nn3<-sum(tab[row(tab)==col(tab)])/sum(tab)
sensibilidad.nn3 <-tab[2,2]/(tab[1,2]+tab[2,2])
especificidad.nn3 <-tab[1,1]/(tab[1,1]+tab[2,1])

#MODELO 4
modelo4.nn<-neuralnet(frml,
                      data          = train_nrm,
                      threshold=0.8,
                      hidden        = c(10, 15),
                      linear.output = FALSE )
plot(modelo4.nn)
pred4_nrm <- predict(modelo4.nn, test_nrm[,-c(16)],type = "class")
pred4<- (pred4_nrm)*(max(datos$stroke)-min(datos$stroke))+min(datos$stroke)
roundpred4<-sapply(pred4,round,digits=0)
tab <- table(roundpred4, test$stroke) 
tab
tasa.aciertos.nn4<-sum(tab[row(tab)==col(tab)])/sum(tab)
sensibilidad.nn4 <-tab[2,2]/(tab[1,2]+tab[2,2])
especificidad.nn4 <-tab[1,1]/(tab[1,1]+tab[2,1])

#MODELO 5
modelo5.nn<-neuralnet(frml,
                      data          = train_nrm,
                      threshold=0.8,
                      hidden        = c(5, 20),
                      linear.output = FALSE )
plot(modelo5.nn)
pred5_nrm <- predict(modelo5.nn, test_nrm[,-c(16)],type = "class")
pred5<- (pred5_nrm)*(max(datos$stroke)-min(datos$stroke))+min(datos$stroke)
roundpred5<-sapply(pred5,round,digits=0)
tab <- table(roundpred5, test$stroke) 
tab
tasa.aciertos.nn5<-sum(tab[row(tab)==col(tab)])/sum(tab)
sensibilidad.nn5 <-tab[2,2]/(tab[1,2]+tab[2,2])
especificidad.nn5 <-tab[1,1]/(tab[1,1]+tab[2,1])

plot(c(1, 2, 3, 4, 5),c(tasa.aciertos.nn1, tasa.aciertos.nn2, tasa.aciertos.nn3,
                        tasa.aciertos.nn4, tasa.aciertos.nn5), 
     type = "p", main = "Tasas de acierto de las 5 redes neuronales", xlab = "Red neuronal",
     ylab ="Tasa de acierto", cex = 2)
