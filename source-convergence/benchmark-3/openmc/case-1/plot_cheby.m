clear

flux_n = [
0.893122    
-0.113869   
-0.575630   
6.31008E-02 
-0.127722   
2.03398E-02 
-5.54408E-02
6.93932E-03 
-3.03475E-02
4.94586E-03 
-2.01796E-02 
];

tot_n = [
0.725322    
-0.150707   
-0.456501   
8.47175E-02 
-0.110813   
2.55487E-02 
-4.56965E-02
9.79382E-03 
-2.57592E-02
6.48650E-03 
-1.65917E-02
];


dx=0.001;
num_x = 2/dx + 1;
x=zeros(num_x,1);
x(1)=-1.0;
for j = 2:num_x
  x(j) = x(j-1)+dx;
end

ftot=zeros(num_x,1);
fflux=zeros(num_x,1);
fsigt=zeros(num_x,1);
for j = 1:num_x
  for n = 1:size(tot_n,1)
    coeff=1.0
    %coeff=asin(x(j));
    ftot(j) = ftot(j) + tot_n(n)*chebyshevpoly(1,n-1,x(j))*coeff;
    fflux(j) = fflux(j) + flux_n(n)*chebyshevpoly(1,n-1,x(j))*coeff;
  end
  fsigt(j) = ftot(j) / fflux(j);
end
plot(x,ftot,x,fflux,x,fsigt)


% Integrate fsigt
ave=sum(fsigt)/length(fsigt)
xmin=501;
xmax=1600;
ave2=sum(fsigt(xmin:xmax))/length(fsigt(xmin:xmax))