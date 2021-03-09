% T:the total time of the reaction
% a1,a2,a3 represent the rate constants
% e0,s0,es0,p0 represent the initial value of the concentration of E,S,ES,P

T=1;
N=10000;
dt=T/N;
t=0:dt:T;
y=zeros(4,length(t));
a1=100;
a2=600;
a3=150;
e0=1;
s0=10;
es0=0;
p0=0;

y(:,1)=[e0;s0;es0;p0];
for n=1:length(t)-1
    k1=[(a2+a3)*y(3,n)-a1*y(1,n)*y(2,n);a2*y(3,n)-a1*y(1,n)*y(2,n);...
        a1*y(1,n)*y(2,n)-(a2+a3)*y(3,n);a3*y(3,n)];
    k2=[(a2+a3)*(y(3,n)+dt/2*k1(3))-a1*(y(1,n)+dt/2*k1(1))*(y(2,n)+dt/2*k1(2));...
        a2*(y(3,n)+dt/2*k1(3))-a1*(y(1,n)+dt/2*k1(1))*(y(2,n)+dt/2*k1(2));...
        a1*(y(1,n)+dt/2*k1(1))*(y(2,n)+dt/2*k1(2))-(a2+a3)*(y(3,n)+dt/2*k1(3));...
        a3*(y(3,n)+dt/2*k1(3))];
    k3=[(a2+a3)*(y(3,n)+dt/2*k2(3))-a1*(y(1,n)+dt/2*k2(1))*(y(2,n)+dt/2*k2(2));...
        a2*(y(3,n)+dt/2*k2(3))-a1*(y(1,n)+dt/2*k2(1))*(y(2,n)+dt/2*k2(2));...
        a1*(y(1,n)+dt/2*k2(1))*(y(2,n)+dt/2*k2(2))-(a2+a3)*(y(3,n)+dt/2*k2(3));...
        a3*(y(3,n)+dt/2*k2(3))];
    k4=[(a2+a3)*(y(3,n)+dt*k3(3))-a1*(y(1,n)+dt*k3(1))*(y(2,n)+dt*k3(2));...
        a2*(y(3,n)+dt*k3(3))-a1*(y(1,n)+dt*k3(1))*(y(2,n)+dt*k3(2));...
        a1*(y(1,n)+dt*k3(1))*(y(2,n)+dt*k3(2))-(a2+a3)*(y(3,n)+dt*k3(3));...
        a3*(y(3,n)+dt*k3(3))];
    y(:,n+1)=y(:,n)+1/6*(k1+2*k2+2*k3+k4)*dt;  
    
end

figure(1),plot(t,y,'Linewidth',1);
xlabel('t');
ylabel('y');
legend('[E]','[S]','[ES]','[P]');
title('The numerical solution');
hold on

V=150*y(3,1:100);
S=0:99;
figure(2),plot(S,V,'Linewidth',1);
xlabel('Concentration of Substrate(μM/L)');
ylabel('Rate of Reaction(μM/min)');

Vmax=max(V);
Smax=S(find(V==Vmax));
hold on
plot(Smax,Vmax,'r.','markersize',16)
text(Smax,Vmax,[' S=',num2str(Smax),char(10),' Vmax=',num2str(Vmax)]);

