# PROYECTO PARA LA ASIGNATURA DE SIMULACION Y REDES NEURONALES
# AUTOR: JAVIER PORCEL MARI
# MASTER EN INGENIERIA DE ANALISIS DE DATOS UPV
# SEGUNDA PARTE

# PRIMER PROBLEMA - SEGUNDO APARTADO
estado <- numeric(200000)+1
camino1 <- 0
camino2 <- 0
camino3 <- 0
camino4 <- 0
camino5 <- 0
i <- 0
for (i in 1:200000) {
  camino1 <- sample(1:1000, 1)/1000
  camino2 <- sample(1:1000, 1)/1000
  camino3 <- sample(1:1000, 1)/1000
  camino4 <- sample(1:1000, 1)/1000
  camino5 <- sample(1:1000, 1)/1000
  if (camino1 > 0.05) {
    camino1 <- 1
  } else {
    camino1 <- 0
  }
  if (camino2 > 0.025) {
    camino2 <-1
  } else {
    camino2 <- 0
  }
  if (camino3 > 0.05) {
    camino3 <- 1
  } else {
    camino3 <- 0
  }
  if (camino4 > 0.02) {
    camino4 <- 1
  } else {
    camino4 <- 0
  }
  if (camino5 > 0.075) {
    camino5 <- 1
  } else {
    camino5 <- 0
  }
  if (camino1 == 0 && camino4 == 0){
    estado[i] <- 0
  } 
  if (camino2 == 0 && camino5 == 0){
    estado[i] <- 0
  } 
  if (camino1 == 0 && camino3 == 0 && camino5 == 0){
    estado[i] <- 0
  } 
  if (camino2 == 0 && camino3 == 0 && camino4 == 0){
    estado[i] <- 0
  }
}

Fiabilidad <- mean(estado)*100
Probabilidad_de_fallo <- 100 - Fiabilidad


# PRIMER PROBLEMA - TERCER APARTADO

FiabilidadMatriz <- matrix(1, ncol=1000, nrow=300)
Fiabilidad1 <- 0
Fiabilidad2 <- 0
Fiabilidad3 <- 0
Fiabilidad4 <- 0
Fiabilidad5 <- 0
lambda1 <- 1e-3
lambda2 <- 2e-2
lambda3 <- 5e-2
lambda4 <- 1e-2
lambda5 <- 8e-4
i <- 0
t <- 0
for (t in 1:300) {
  for (i in 1:1000) {
    Fiabilidad1 <- exp(-lambda1*t)
    Fiabilidad2 <- exp(-lambda2*t)
    Fiabilidad3 <- exp(-lambda3*t)
    Fiabilidad4 <- exp(-lambda4*t)
    Fiabilidad5 <- exp(-lambda5*t)
    camino1 <- sample(1:1000, 1)/1000
    camino2 <- sample(1:1000, 1)/1000
    camino3 <- sample(1:1000, 1)/1000
    camino4 <- sample(1:1000, 1)/1000
    camino5 <- sample(1:1000, 1)/1000
    if (camino1 <= Fiabilidad1) {
      camino1 <- 1
    } else {
      camino1 <- 0
    }
    if (camino2 <= Fiabilidad2) {
      camino2 <- 1
    } else {
      camino2 <- 0
    }
    if (camino3 <= Fiabilidad3) {
      camino3 <- 1
    } else {
      camino3 <- 0
    }
    if (camino4 <= Fiabilidad4) {
      camino4 <- 1
    } else {
      camino4 <- 0
    }
    if (camino5 <= Fiabilidad5) {
      camino5 <- 1
    } else {
      camino5 <- 0
    }
    if (camino1 == 0 && camino4 == 0){
      FiabilidadMatriz[t, i] <- 0
    } 
    if (camino2 == 0 && camino5 == 0){
      FiabilidadMatriz[t, i] <- 0
    } 
    if (camino1 == 0 && camino3 == 0 && camino5 == 0){
      FiabilidadMatriz[t, i] <- 0
    } 
    if (camino2 == 0 && camino3 == 0 && camino4 == 0){
      FiabilidadMatriz[t, i] <- 0
    }
  }
}
Media <- 1:300
for (j in 1:300){
  Media[j] <- mean(FiabilidadMatriz[j,])
}
plot(1:300, Media, xlab = "Tiempo (h)", ylab = "R(t)", type ="l")
Media[300]

# SEGUNDO PROBLEMA - PRIMER APARTADO

lambdaA <- matrix(0, nrow=3, ncol=3)
lambdaA[1,2] <- 3e-3
lambdaA[1,3] <- 1e-3
lambdaA[1,1] <- 1 - lambdaA[1,2] - lambdaA[1,3]
lambdaA[2,3] <- 6e-3
lambdaA[2,2] <- 1 - lambdaA[2,3]
lambdaA[3,1] <- 8e-3
lambdaA[3,2] <- 5e-3
lambdaA[3,3] <- 1 - lambdaA[3,1] - lambdaA[3,2]

lambdaB <- matrix(0, nrow=3, ncol=3)
lambdaB[1,2] <- 1e-3
lambdaB[1,3] <- 5e-3
lambdaB[1,1] <- 1 - lambdaB[1,2] - lambdaB[1,3]
lambdaB[2,3] <- 4e-3
lambdaB[2,2] <- 1 - lambdaB[2,3]
lambdaB[3,1] <- 7.5e-3
lambdaB[3,2] <- 3.5e-3
lambdaB[3,3] <- 1 - lambdaB[3,1] - lambdaB[3,2]

lambdaC <- matrix(0, nrow=3, ncol=3)
lambdaC[1,2] <- 8e-3
lambdaC[1,3] <- 2.5e-3
lambdaC[1,1] <- 1 - lambdaC[1,2] - lambdaC[1,3]
lambdaC[2,3] <- 2e-3
lambdaC[2,2] <- 1 - lambdaC[2,3]
lambdaC[3,1] <- 4e-3
lambdaC[3,2] <- 1.5e-3
lambdaC[3,3] <- 1 - lambdaC[3,1] - lambdaC[3,2]

lambda1<-diag(3)
lambda2<-diag(3)
lambda3<-diag(3)
library(Biodem)
for (t in 1:10000){
  lambda1<-lambda1%*%lambdaA
  lambda2<-lambda2%*%lambdaB
  lambda3<-lambda3%*%lambdaC
  pA <- c(1,0,0)%*%lambda1
  pB <- c(1,0,0)%*%lambda2
  pC <- c(1,0,0)%*%lambda3
  Fiabilidad[t] <- (pA[1]+pA[2])+(pB[1]+pB[2])*(pC[1]+pC[2])-(pA[1]+pA[2])*(pB[1]+pB[2])*(pC[1]+pC[2])
}
Fiabilidad[1000]
plot(1:10000, Fiabilidad)

# SEGUNDO PROBLEMA - TERCER APARTADO

lambdaA <- matrix(0, nrow=3, ncol=3)
lambdaA[1,2] <- 3e-3
lambdaA[1,3] <- 1e-3
lambdaA[2,3] <- 6e-3
lambdaA[3,1] <- 8e-3
lambdaA[3,2] <- 5e-3

lambdaB <- matrix(0, nrow=3, ncol=3)
lambdaB[1,2] <- 1e-3
lambdaB[1,3] <- 5e-3
lambdaB[2,3] <- 4e-3
lambdaB[3,1] <- 7.5e-3
lambdaB[3,2] <- 3.5e-3

lambdaC <- matrix(0, nrow=3, ncol=3)
lambdaC[1,2] <- 8e-3
lambdaC[1,3] <- 2.5e-3
lambdaC[2,3] <- 2e-3
lambdaC[3,1] <- 4e-3
lambdaC[3,2] <- 1.5e-3

lambdaA123 = c(lambdaA[1,2]+lambdaA[1,3],lambdaA[2,3], lambdaA[3,1]+lambdaA[3,2])
lambdaB123 = c(lambdaB[1,2]+lambdaB[1,3],lambdaB[2,3], lambdaB[3,1]+lambdaB[3,2])
lambdaC123 = c(lambdaC[1,2]+lambdaC[1,3],lambdaC[2,3], lambdaC[3,1]+lambdaC[3,2])

Tmiss <- 1000
Tfallo <- 0
TfalloA <- 0
TfalloB <- 0
TfalloC <- 0

for (i in 1:10000){
  estadoactual <- c(1,1,1)
  t <- 0
  while (t<=Tmiss){
    Tasa_a <- lambdaA123[estadoactual[1]]
    Tasa_b <- lambdaB123[estadoactual[2]]
    Tasa_c <- lambdaC123[estadoactual[3]]
    Tasa_Sistema <- Tasa_a + Tasa_b + Tasa_c
    Rt = sample(1:1000, 1)/1000
    Rc = sample(1:1000, 1)/1000
    Rs = sample(1:1000, 1)/1000
    t1 <- t - log(1-Rt)/Tasa_Sistema
    if (estadoactual[1]==3 && (estadoactual[2]==3 || estadoactual[3]==3)){
      if (t1 < Tmiss){
        Tfallo <- Tfallo + t1 - t
      } else {
        Tfallo <- Tfallo + Tmiss - t
      }
    }
    if (estadoactual[1]==3){
      if (t1 < Tmiss){
        TfalloA <- TfalloA + t1 - t
      } else {
        TfalloA <- TfalloA + Tmiss - t
      }
    }
    if (estadoactual[2]==3){
      if (t1 < Tmiss){
        TfalloB <- TfalloB + t1 - t
      } else {
        TfalloB <- TfalloB + Tmiss - t
      }
    }
    if (estadoactual[3]==3){
      if (t1 < Tmiss){
        TfalloC <- TfalloC + t1 - t
      } else {
        TfalloC <- TfalloC + Tmiss - t
      }
    }
    if (Rc < Tasa_a/Tasa_Sistema){
      if (Rs < lambdaA[estadoactual[1], 1]/lambdaA123[estadoactual[1]]){
        estadoactual[1]<-1
      } else if (Rs < (lambdaA[estadoactual[1], 1]+lambdaA[estadoactual[1], 2])/lambdaA123[estadoactual[1]]){
        estadoactual[1]<-2
      } else {
        estadoactual[1]<-3
      }
    } else if (Rc < (Tasa_a + Tasa_b)/Tasa_Sistema){
        if (Rs < lambdaB[estadoactual[2], 1]/lambdaB123[estadoactual[2]]){
          estadoactual[2]<-1
      } else if (Rs < (lambdaB[estadoactual[2], 1]+lambdaB[estadoactual[2], 2])/lambdaB123[estadoactual[2]]){
          estadoactual[2]<-2
      } else {
        estadoactual[2]<-3
      }
    } else {
      if (Rs < lambdaC[estadoactual[3], 1]/lambdaC123[estadoactual[3]]){
        estadoactual[3]<-1
      } else if (Rs < (lambdaC[estadoactual[3], 1]+lambdaC[estadoactual[3], 2])/lambdaC123[estadoactual[3]]){
        estadoactual[3]<-2
      } else {
        estadoactual[3]<-3
      }
    }
    t <- t1
  }
}
P <- Tfallo / (10000*Tmiss)
1-P

