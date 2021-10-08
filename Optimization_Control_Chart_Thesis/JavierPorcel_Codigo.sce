// ==============================================================================
// TFM JAVIER PORCEL MARI
// VALENCIA 2021
// ==============================================================================

// Clean plots
clf()
// Clean console
clc()
// Clean workspace
clear()
// Set working directory
cd("C:/Users/JAVI/Desktop/TFM")

// ------------------------------------------------------------------------------
// JOHNSON DISTRIBUTIONS
// ------------------------------------------------------------------------------
format(25);
Jtype = ["B"; "B"; "U"; "U"; "U"; "U";
         "B"; "B"; "U"; "U"; "U"; "U"; 
         "B"; "B"; "U"; "U"; "U"; "U"]

Ja = [
  0.; 0.; 0.; 0.; 0.; 0.;
  1.74642830857010758943626229557833166151;
  3.32789132381672536784153764062847739022;
  -4.85598745088089370566862569594819129775;
  -1.04438933697571120946340909857749695448;
  -0.52977458286145969287844983446062716444;
  -0.34371386717998937758370229564494168076;
  
  3.37153689359224037661433093037670570547;
  5.21933524353541219076783885100278703868;
  -4.01872982057191060039104634115859799883;
  -0.75701261664619041238141624389115395037;
  -0.43186873681561772117311342224111378956;
  -0.29867866225722724403897426961140969985]

Jb = [
  0.64646005097083720877580377544491249367;
  1.39833730706480665525203763381572201528;
  100.;
  2.32115548141591265489566269241805350277;
  1.61043109802798400472117114957805882116;
  1.34925107124421982672157193726909725955;
  
  0.69076307557374844062848335460718608085;
  1.22701925790980838307542721643016935644;
  1.80444211955137355943514847493631987497;
  1.43196957533586078620611350537732178049;
  1.20933055279040199782191033417917696741;
  1.08916837329898641023346423021464511577;
  
  0.74593166247571219250998719250234579684;
  0.98133598238435636274623736299637443869;
  1.08644119278200855055763353598608437671;
  0.98743930478592712145401232678242473738;
  0.9079732861493920122301339214072614797;
  0.8555768706280539154424246218382444065]

Jc = [
  -1.81531640559448629853130518464898084325;
  -3.10974220782783891848630844309862248348;
  0.; 0.; 0.; 0.;
  
  -0.48931893698288401224217306196432734367;
  -1.00163621345669029289984284967824485705;
  -1.41900498170269088110396585332059656851;
  -0.65538265907067714949198864107359538936;
  -0.3315419153227644307916851724891935819;
  -0.20230241986439714646030995430481162286;
  
  -0.27093613236330658835219937054263483016;
  -0.47315502136902041809145973325494766811;
  -0.5665244523471390467804271447527989781;
  -0.32032500617458316656917852134863102249;
  -0.18537971196280261135855039510532213063;
  -0.12122093889436368817120668700925957169]

Jd = [
  3.63063281118897259706261036929801914047;
  6.21948441565567783697261688619731113724;
  100.;
  2.10938136494640961313186053630477642153;
  1.31177712285895824442559128408848228655;
  1.;
        
  6.6213052042202285009336108971666295627;
  16.08828514862974619284545066659958256682;
  0.19331807239056496916824641865444966886;
  0.82361491419897282190401110495433271155;
  0.73314420124628385662970998863888855497;
  0.63054262902988914147483139115470665;
        
  25.15004224768683915100766195782836377563;
  97.04328850983479801334754766131519562171;
  0.02805859417661557430944067988854233275;
  0.3795419133008987804241261135623853673;
  0.3754308073205232238191875432701887019;
  0.34028822968081050623748938666543961555]

Jskewness = [0.; 0.; 0.; 0.; 0.; 0.;
             2.; 2.; 2.; 2.; 2.; 2.;
             5.; 5.; 5.; 5.; 5.; 5.]

Jkurtosis = [-1.2; -0.6; 0.0; 1.0; 3.0; 6.0;
             4.3; 6.1; 7.9; 10.8; 16.7; 25.5;
             39.9; 52.6; 65.3; 86.4; 128.7; 192.1]


// ==============================================================================
// Saved data into an Excel file named: Johnson18
// ------------------------------------------------------------------------------
// Some plots
// ------------------------------------------------------------------------------
// Limit for possible combinations of sqrt(beta_1) and beta_2

function y = limite(x)
  
y = x^2 + 1

endfunction

// Lognormal curve. Set of values of sqrt(beta_1) and beta_2 matching with a
// S_L distribution

function y = logx(w)
  
y = sqrt(w^3+3*w^2-4)

endfunction

function y = logy(w)
  
y = w^4 + 2*w^3 +3*w^2 - 3

endfunction

ww = linspace(1, 2.65, 200);

// 18 Johnson distributions
plot(Jskewness, Jkurtosis + 3, "d", "linewidth", 1)
xtitle("$Plot$", "$\sqrt\beta_1$", "$\beta_2$")
a = get("current_axes");
a.title
a.x_label
a.y_label


t=a.title;
t.font_size=4;

x_label=a.x_label;
x_label.font_size= 5;

y_label=a.y_label;
y_label.font_size= 5;

k = linspace(-0.05, 6, 1000);
m = limite(k);
plot(k, m)
plot(logx(ww), logy(ww),"--k")

// Place text inside the plot
xstring(4.5, 10,  "$Impossible zone$")
gce().font_size = 3
xstring(3.5, 32,  "$S[L]$")
gce().font_size = 3
xstring(3.5, 16,  "$S[B]$")
gce().font_size = 3
xstring(3.5, 115,  "$S[U]$")
gce().font_size = 3
// ----

exec('C:\Users\JAVI\Desktop\TFM\LIB\pdfjohnson.sci',-1)
exec('C:\Users\JAVI\Desktop\TFM\LIB\assert.sci',-1)
exec('C:\Users\JAVI\Desktop\TFM\LIB\idfjohnson.sci',-1)
exec('C:\Users\JAVI\Desktop\TFM\LIB\cdfjohnson.sci',-1)
exec('C:\Users\JAVI\Desktop\TFM\LIB\pmfbinomial.sci',-1)
exec('C:\Users\JAVI\Desktop\TFM\LIB\idfnormal.sci',-1)
exec('C:\Users\JAVI\Desktop\TFM\LIB\cdfnormal.sci',-1)
// ----
clf()
k = linspace(-3, 3, 1000);
for i = 1:18
  subplot(3, 6, i)
  densityfunc = pdfjohnson(k, Jtype(i), Ja(i), Jb(i), Jc(i), Jd(i)+Jc(i));
  plot(k, densityfunc)
  hl=legend([string(i)]);
  ax=gca();
  ax.data_bounds=[-3 0;3 2.7];
end
// ==============================================================================


// ------------------------------------------------------------------------------
// STUDY 1
// ------------------------------------------------------------------------------

// New values of a, b, c, d when the st. dev. of J is shifted by `tau`
// ------------------------------------------------------------------------------

// We mean the new J has:
// - the same MEDIAN
// - the same SKEWNESS
// - the same KURTOSIS
// - sigma.1 = tau*sigma.0

// THIS WORKS BECAUSE THE ORIGINAL MEDIAN OF ALL 18 `J` IS ZERO.
// If the original median was <> 0, then the new value of `c` would not be
// tau*c. The rest would remain the same, apparently.

// The old name was `new.J.sd.change`.
function [newa, newb, newc, newd] = shiftedJsd(tau, ftype, a, b, c, d)
  newa = a
  newb = b
  newc = tau*c
  newd = tau*d
endfunction



// Main procedure to obtain the optimal values for p.0 and LCL/UCL, given the
// values of n, alpha.max, tau and J.id.
// ------------------------------------------------------------------------------
function [bestp0, bestL, bestbeta, actualalpha, actualp1] = minbetaINConesided(tau, alphamax, Jid, n)
  
// Properties of the Johnson distribution being considered:
  ftype = Jtype(Jid)
  a = Ja(Jid)
  b = Jb(Jid)
  c = Jc(Jid)
  d = Jd(Jid)
  
// Parameters for the shifted J distribution:
  anew = double(1)
  bnew = double(1)
  cnew = double(1)
  dnew = double(1)
  
// Parameters of J' (shifted J):
// requires 'gsubfn' package
  [anew, bnew, cnew, dnew] = shiftedJsd(tau, ftype, a, b, c, d)

// Initialisation of the search
  
  bestbeta = double(10)
  bestp0   = double(-1)
  bestL    = double(-1)
  actualalpha = double(-1)
  actualp1 = double(-1)
  p00 = double(1)
  p11 = double(1)
// For now, we only consider these values for p.0:
  testp00   = [0.05; 0.1; 0.2; 0.3; 0.4; 0.5; 0.6; 0.7; 0.8; 0.9; 0.95]

  for j = 1:length(testp00)
    p00 = testp00(j)
// We calculate the limits of the 'centre' of the current J distrib.:
    Ilower = idfjohnson(p00/2,     ftype, a, b, c, d+c)
    Iupper = idfjohnson(1 - p00/2, ftype, a, b, c, d+c)
    
// We calculate p.1 the prob. of J' being OUTSIDE [I.lower, I.upper]:
    p11 = 1 - cdfjohnson(Iupper, ftype, anew, bnew, cnew, dnew+cnew) + cdfjohnson(Ilower, ftype, anew, bnew, cnew, dnew+cnew)

// Calculate all the probabilities we are going to need:
    binom0 = double((0:n)')
    binom1 = double((0:n)')
    binom0 = pmfbinomial((0:n)', p00, n)  // n+1 values, indexed from 1 to n+1
    binom1 = pmfbinomial((0:n)', p11, n)  // n+1 values, indexed from 1 to n+1
//  ########################################################################
//  # So, if we want to calculate  Pr(U == u | p.0),                       #
//  # we take binom.0[(u+n)/2 + 1]  <---- Mind the `1`!!!                  #
//  ########################################################################
    
//  This loop is OK for either LCL or UCL:    
    for L = linspace(n, -n, n+1)
//        # `L` stands for either `UCL` or `-LCL`  <-- Mind the `-`!!!
      if(L == n) then
        alpha = 0   // Will store the false alarm rate
        betaa  = 1  // Will store the miss rate
      else
        if (tau < 1) then
          alpha = alpha + binom0(((-L - 2) + n)/2 + 1)
        else
          alpha = alpha + binom0(((L + 2) + n)/2 + 1)
        end
         
        if (alpha > alphamax) then
          break // # DON'T CONTINUE WITH THIS `L` and lower!
        end
        if (tau < 1) then
          betaa = betaa - binom1(((-L - 2) + n)/2 + 1)
        else
          betaa = betaa - binom1(((L + 2) + n)/2 + 1)
        end

//        NOTE: The function `ifelse` (see later) could have been used
//        for the two previous `if-else` sentences, but we did it like
//        that for the sake of clarity.
      end // end else
      
//      THE CURRENT VALUES OF `p.0` and `L` are a FEASIBLE SOLUTION
      if(betaa < bestbeta) then
//          NEW IMPROVEMENT!
        bestp0 = p00
        if (tau < 1) then
            bestL = -L
        else
            bestL = L
        end
        bestbeta = betaa
        actualalpha = alpha
        actualp1 = p11
      end // end if
    end // end for
  end 
//   RETURNS `L`, which is `UCL` if `tau > 1` or `LCL` if `tau < 1`.
  
//  return(list("p.0" = best.p0, "L" = best.L, "beta" = best.beta,
//              "alpha" = actual.alpha, "p.1" = actual.p1))
endfunction


// ==============================================================================


// RESULTS INTO TABLE
// ------------------------------------------------------------------------------

// REMEMBER that this function has to be called like this:
// study1.tests.INC.onesided("filename_USING_QUOTATION_MARKS")
filename = "ResultadosconScilab"
function study1testsINConesided(filename)
  
//  Values to test for each parameter:
  
  testalpha0 = 0.0027  // <--- Changed notation to match the paper
  testn       = [10; 15; 20; 25; 30]
// c(11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31)
  testtau     = [0.25; 0.5; 2; 4]
  testJid     = linspace(1, 18, 18)'
  
//  Lengths:
  
  lenalpha0   = length(testalpha0)
  lenn        = length(testn)
  lentau      = length(testtau)
  lenJid      = length(testJid)
  totallen = lenalpha0*lenn*lentau*lenJid
//  This properly creates all the combinations to be tested:  
  alpha0 = ones(totallen, 1)*testalpha0
  matrixn = repmat(testn,       lenalpha0, each = lentau*lenJid)' // # <---
  n = ones(totallen, 1)
  for i = 1:lenn
    n((1+totallen/lenn*(i-1)):(totallen/lenn*i))=matrixn(:,i)
  end
  tau = ones(totallen, 1)
  matrixtau     = repmat(testtau,     lenalpha0*lenn, each = lenJid)'   // # <---
  for i = 1:(lentau*lenn)
    tau((1+totallen/lentau/lenn*(i-1)):(totallen/lentau/lenn*i))=matrixtau(:,i)
  end
  Jid = ones(totallen, 1)
  matrixJid     = repmat(testJid,    lenalpha0*lenn*lentau, each = 1) // # <---
  Jid = matrixJid
//  Things to calculate for each combination:
// Sustituo de la función numeric para Scilab  
  p0      = (1:totallen)'
  L       = (1:totallen)'  // # <-- LCL or UCL
  alpha   = (1:totallen)'  // # <-- Actual alpha
  ARL0   = (1:totallen)'  // # <-- Actual ARL_0
  p1     = (1:totallen)'
  betaa   = (1:totallen)'
  ARL1   = (1:totallen)'
  ARLvar  = (1:totallen)'
  Jskew   = (1:totallen)'
  Jkurt   = (1:totallen)'
  
//  THIS DOES NOT WORK BECAUSE find.beta DOES NOT ADMIT VECTORS!!
//  list[beta, L, alpha.0, p.1] = find.beta(alpha, n, p.0, tau, J.id)
  
  for i = 1:totallen
    [p0(i), L(i), betaa(i), alpha(i), p1(i)] = minbetaINConesided(tau(i), alpha0(i), Jid(i), n(i))
  end
  M = zeros(totallen, 14)
//  # This can be done directly from/to vectors:
  ARL0 = (1./alpha)
  ARL1 = (1./(1 - betaa))
  ARLvar = (ARL1 - ARL0)./ARL0
  Jskew  = Jskewness(Jid)
  Jkurt  = Jkurtosis(Jid)
  M = [alpha0, n, p0, L, alpha, ARL0, tau, Jid, p1, betaa, ARL1, ARLvar, Jskew, Jkurt]
  csvWrite(M, filename, " ", ",")
endfunction

// ==============================================================================
// This function calculates the value of three probabilities.
function [piout, pitie, piin] = CalculateThreePi(n, tau, p00, Jid, rho)
  ftype = Jtype(Jid)
  a = Ja(Jid)
  b = Jb(Jid)
  c = Jc(Jid)
  d = Jd(Jid)
// This calculates the tolerances for the initial distribution.
  Ilower = idfjohnson(p00/2,     ftype, a, b, c, d+c)
  Iupper = idfjohnson(1 - p00/2, ftype, a, b, c, d+c)
  
  anew = double(1)
  bnew = double(1)
  cnew = double(1)
  dnew = double(1)

  [anew, bnew, cnew, dnew] = shiftedJsd(tau, ftype, a, b, c, d)
// Here we calculate the probabilities using the previous tolerances and the shifted distribution.
  if ((Ilower + rho/2) < (Iupper - rho/2))  then
    piin = cdfjohnson(Iupper-rho/2, ftype, anew, bnew, cnew, dnew+cnew) -cdfjohnson(Ilower+rho/2, ftype, anew, bnew, cnew, dnew+cnew)
  else
    piin = 0
  end
  
  piout = cdfjohnson(Ilower-rho/2, ftype, anew, bnew, cnew, dnew+cnew) + 1 - cdfjohnson(Iupper+rho/2, ftype, anew, bnew, cnew, dnew+cnew)
  
  pitie = 1 - piout - piin

endfunction

exec('C:\Users\JAVI\Desktop\TFM\LIB\combination.sci',-1)
exec('C:\Users\JAVI\Desktop\TFM\LIB\homogesize.sci',-1)

// This function calculate the value Pr(U=u).
function dbinomtie = CalculatePmfBinomTie(n, u, piout, pitie, piin)
  dbinomtie = 0
  for i = max(0,-u):int((n-u)/2)
    dbinomtie = dbinomtie + combination(i, n)*combination(u+i, n-i)*piin^i*pitie^(n-u-2*i)*piout^(u+i)
  end
endfunction

// This function puts together the previous two functions.
function dbinomtie = PmfBinomTie(n, tau, u, p00, Jid, rho)
  [piout, pitie, piin] = CalculateThreePi(n, tau, p00, Jid, rho)
  dbinomtie = CalculatePmfBinomTie(n, u, piout, pitie, piin)
endfunction

// This function calculates the value Pr(U<=u).
function pbinomtie = CmfBinomTie(n, tau, u, p00, Jid, rho)
  pbinomtie = 0
  [piout, pitie, piin] = CalculateThreePi(n, tau, p00, Jid, rho)
  for i = -n:u
    pbinomtie = pbinomtie + CalculatePmfBinomTie(n, i, piout, pitie, piin)
  end
endfunction

// This function calculates a necessary parameter to obtain alpha and beta.
function x = Accepttie(n, Jid, rho, tau, LCL, UCL, p00)  
  [piout, pitie, piin] = CalculateThreePi(n, tau, p00, Jid, rho)
  x = 0
  for i = LCL:UCL
    x = x + CalculatePmfBinomTie(n, i, piout, pitie, piin)
  end 
endfunction

// This function prints a csv file with the real parameters.
filename = "ResultadosconScilab2"
function Secondtable(filename, rho)
  M = csvRead("1_Sin_Empates", " ", ",")
  alpha0 = M(:,1)
  n = M(:,2)
  p00 = M(:,3)
  L = M(:,4)
  alpha = M(:,5)
  ARL0 = M(:,6)
  tau = M(:,7)
  Jid = M(:,8)
  p1 = M(:,9)
  betaa = M(:,10)
  ARL1 = M(:,11)
  totallen = length(alpha)
  alphatiee = (1:totallen)'
  betatiee = (1:totallen)'
  ARL0tie = (1:totallen)'
  ARL1tie = (1:totallen)'
  ARL0vartie = (1:totallen)'
  ARL1vartie = (1:totallen)' 
  LCL = double(1)
  UCL = double(1)
  piin1 = (1:totallen)' 
  pitie1 = (1:totallen)' 
  piout1 = (1:totallen)' 
  piin2 = (1:totallen)'
  pitie2 = (1:totallen)' 
  piout2 = (1:totallen)' 
  dismpiin1 = (1:totallen)' 
  dismpiout1 = (1:totallen)' 
  dismpiin2 = (1:totallen)' 
  dismpiout2 = (1:totallen)'  
  for i = 1:totallen
    if tau(i) < 1 then
      LCL = L(i)
      UCL = n(i)
    else
      LCL = -n(i)
      UCL = L(i) 
    end
    alphatiee(i) = 1-Accepttie(n(i), Jid(i), rho, tau=1, LCL, UCL, p00(i)) 
    betatiee(i) = Accepttie(n(i), Jid(i), rho, tau(i), LCL, UCL, p00(i))  
    ARL0tie(i) = 1/alphatiee(i)
    ARL1tie(i) = 1/(1-betatiee(i))
    ARL0vartie(i) = (ARL0tie(i)-ARL0(i))/ARL0(i)*100
    ARL1vartie(i) = (ARL1tie(i)-ARL1(i))/ARL1(i)*100
    [piout1(i), pitie1(i), piin1(i)] = CalculateThreePi(n(i), tau=1, p00(i), Jid(i), rho)
    [piout2(i), pitie2(i), piin2(i)] = CalculateThreePi(n(i), tau(i), p00(i), Jid(i), rho)
    dismpiout1(i) = (piout1(i) - p00(i))/p00(i)*100
    dismpiin1(i) = (piin1(i) - (1-p00(i)))/(1-p00(i))*100
    dismpiout2(i) = (piout2(i) - p1(i))/p1(i)*100
    dismpiin2(i) = (piin2(i) - (1-p1(i)))/(1-p1(i))*100
    
  end
  M = [alpha0, n, p00, L, alpha, alphatiee, ARL0, ARL0tie, ARL0vartie, tau, Jid, p1, betaa, betatiee, ARL1, ARL1tie, ARL1vartie, piout1, pitie1, piin1, piout2, pitie2, piin2, dismpiout1, dismpiin1, dismpiout2, dismpiin2]
  csvWrite(M, filename, " ", ",")
endfunction

// Main procedure to obtain the optimal values for p.0 and LCL/UCL, given the
// values of n, alpha.max, tau and J.id.
// ------------------------------------------------------------------------------
function [bestp0, bestL, bestbeta, actualalpha] = minbetaINConesidedTie(tau, alphamax, Jid, n, rho)
  
// Properties of the Johnson distribution being considered:
  ftype = Jtype(Jid)
  a = Ja(Jid)
  b = Jb(Jid)
  c = Jc(Jid)
  d = Jd(Jid)
  
// Parameters for the shifted J distribution:
  anew = double(1)
  bnew = double(1)
  cnew = double(1)
  dnew = double(1)
  
// Parameters of J' (shifted J):
// requires 'gsubfn' package
  [anew, bnew, cnew, dnew] = shiftedJsd(tau, ftype, a, b, c, d)

// Initialisation of the search
  
  bestbeta = double(10)
  bestp0   = double(-1)
  bestL    = double(-1)
  actualalpha = double(-1)
  actualp1 = double(-1)
  p00 = double(1)
  p11 = double(1)
// For now, we only consider these values for p.0:
  testp00   = [0.05; 0.1; 0.2; 0.3; 0.4; 0.5; 0.6; 0.7; 0.8; 0.9; 0.95]

  for j = 1:length(testp00)
    p00 = testp00(j)
// We calculate the limits of the 'centre' of the current J distrib.:
    Ilower = idfjohnson(p00/2,     ftype, a, b, c, d+c)
    Iupper = idfjohnson(1 - p00/2, ftype, a, b, c, d+c)
    
    // Equal till here.
    
    // Calculate three pi's for the two situations.
    [piout1, pitie1, piin1] = CalculateThreePi(n, tau=1, p00, Jid, rho)
    [piout2, pitie2, piin2] = CalculateThreePi(n, tau, p00, Jid, rho)
    
    
//  This loop is OK for either LCL or UCL:    
    for L = linspace(n, -n, 2*n+1) // ** Bajando de 1 en 1
//        # `L` stands for either `UCL` or `-LCL`  <-- Mind the `-`!!!
      if(L == n) then
        alpha = 0   // Will store the false alarm rate
        betaa  = 1  // Will store the miss rate
      else
        if (tau < 1) then
          alpha = alpha + CalculatePmfBinomTie(n, -L-1, piout1, pitie1, piin1)
        else
          alpha = alpha + CalculatePmfBinomTie(n, L+1, piout1, pitie1, piin1)
        end
         
        if (alpha > alphamax) then
          break // # DON'T CONTINUE WITH THIS `L` and lower!
        end
        if (tau < 1) then
          betaa = betaa - CalculatePmfBinomTie(n, -L-1, piout2, pitie2, piin2)
        else
          betaa = betaa - CalculatePmfBinomTie(n, L+1, piout2, pitie2, piin2)
        end

//        NOTE: The function `ifelse` (see later) could have been used
//        for the two previous `if-else` sentences, but we did it like
//        that for the sake of clarity.
      end
      
//      THE CURRENT VALUES OF `p.0` and `L` are a FEASIBLE SOLUTION
      if(betaa < bestbeta) then
//          NEW IMPROVEMENT!
        bestp0 = p00
        if (tau < 1) then
            bestL = -L
        else
            bestL = L
        end
        bestbeta = betaa
        actualalpha = alpha
      end // end if
    end // end for
  end 
//   RETURNS `L`, which is `UCL` if `tau > 1` or `LCL` if `tau < 1`.

endfunction
// RESULTS INTO TABLE
// ------------------------------------------------------------------------------

filename = "ResultadosconScilabreoptimizados"
function study2testsINConesidedTie(filename, rho)
  M = csvRead("1_Sin_Empates", " ", ",")
  alpha0 = M(:,1)
  n = M(:,2)
  p00 = M(:,3)
  L = M(:,4)
  alpha = M(:,5)
  ARL0 = M(:,6)
  tau = M(:,7)
  Jid = M(:,8)
  p1 = M(:,9)
  betaa = M(:,10)
  ARL1 = M(:,11)
  totallen = length(alpha)
  piin1 = (1:totallen)' 
  pitie1 = (1:totallen)' 
  piout1 = (1:totallen)' 
  piin2 = (1:totallen)'
  pitie2 = (1:totallen)' 
  piout2 = (1:totallen)' 
  dismpiin1 = (1:totallen)' 
  dismpiout1 = (1:totallen)' 
  dismpiin2 = (1:totallen)' 
  dismpiout2 = (1:totallen)'
  
  for i = 1:totallen
    [p00(i), L(i), betaa(i), alpha(i)] = minbetaINConesidedTie(tau(i), alpha0(i), Jid(i), n(i), rho)
    [piout1(i), pitie1(i), piin1(i)] = CalculateThreePi(n(i), tau=1, p00(i), Jid(i), rho)
    [piout2(i), pitie2(i), piin2(i)] = CalculateThreePi(n(i), tau(i), p00(i), Jid(i), rho)
    dismpiout1(i) = (piout1(i) - p00(i))/p00(i)*100
    dismpiin1(i) = (piin1(i) - (1-p00(i)))/(1-p00(i))*100
    dismpiout2(i) = (piout2(i) - p1(i))/p1(i)*100
    dismpiin2(i) = (piin2(i) - (1-p1(i)))/(1-p1(i))*100    
  end
  N = zeros(totallen, 23)
// This can be done directly from/to vectors:
  ARL0 = (1./alpha)
  ARL1 = (1./(1 - betaa))
  ARLvar = (ARL1 - ARL0)./ARL0
  Jskew  = Jskewness(Jid)
  Jkurt  = Jkurtosis(Jid)
  N = [alpha0, n, p00, L, alpha, ARL0, tau, Jid, betaa, ARL1, ARLvar, Jskew, Jkurt, piout1, pitie1, piin1, piout2, pitie2, piin2, dismpiout1, dismpiin1, dismpiout2, dismpiin2]
  csvWrite(N, filename, " ", ",")
endfunction
