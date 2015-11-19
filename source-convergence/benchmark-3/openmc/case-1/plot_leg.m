clear

flux_n = [
0.893731    
-5.73286E-02
7.59871E-03 
-1.78636E-03
7.81331E-04 
2.88713E-04 
-1.67162E-04
6.51941E-05 
5.10878E-05 
-1.04488E-04
-8.57890E-05
];

tot_n = [
0.725853    
-7.57053E-02
1.03142E-02 
-1.92113E-03
4.20032E-04 
2.15060E-04 
-4.31789E-05
5.49287E-05 
-9.27154E-06
-7.89297E-05
-4.61963E-05
];


dx=0.001;
num_x = 2/dx + 1;
x=zeros(num_x,1);
x(1)=-1.0;
for j = 2:num_x
  x(j) = x(j-1)+dx;
  if x(j) > 1.0
    x(j) = 1.0;
  end
end

ftot=zeros(num_x,1);
fflux=zeros(num_x,1);
fsigt=zeros(num_x,1);
for j = 1:num_x
  for n = 1:size(tot_n,1)
    coeff=legendre(n-1,x(j),"unnorm")(1);
    coeff=coeff*(2.0*(n-1)+1)*0.5;
    ftot(j) = ftot(j) + tot_n(n)*coeff;
    fflux(j) = fflux(j) + flux_n(n)*coeff;
  end
  fsigt(j) = ftot(j) / fflux(j);
end
%plot(x,ftot,x,fflux,x,fsigt)

% Integrate fsigt
ave=sum(fsigt)/length(fsigt)
xmin=1;
xmax=500;
ave1=sum(fsigt(xmin:xmax))/length(fsigt(xmin:xmax))
xmin=501;
xmax=1600;
ave2=sum(fsigt(xmin:xmax))/length(fsigt(xmin:xmax))
xmin=1601;
xmax=num_x;
ave2=sum(fsigt(xmin:xmax))/length(fsigt(xmin:xmax))