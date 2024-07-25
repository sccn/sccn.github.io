---
layout: default
title: Supplementary-functions
long_title: Supplementary-functions
parent: amica
grand_parent: Plugins
---
The functions below are not included in AMICA but they might still be useful.

**gg6**
```matlab
function x = gg6(n,N,mu,beta,rho)
% Generate N Generalized Gaussian m-dimensional vectors with means mu(:),
% inverse scales beta(:), and parameters rho(:).
if length(mu) == 1
    mu = mu*ones(1,n);
    beta = beta*ones(1,n);
    rho = rho*ones(1,n);
end
x = zeros(n,N);
for i = 1:n
   x(i,:) = mu(i) + (1/sqrt(beta(i))) * ( mygamrnd(1/rho(i),1,1,N)).^(1/rho(i) ) .* ((rand(1,N)<0.5)*2-1) ;
end   

function r = mygamrnd(a,b,rows,columns)
% This is essentially copied from the gamrnd function in the Matlab Stats
% Toolbox. If you have that toolbox, you can just use the code above and
% replace mygamrnd() with gamrnd().
% Initialize r to zero.
lth = rows*columns;
r = zeros(lth,1);
a = a(:); b = b(:);
scalara = (length(a) == 1);
if scalara
   a = a*ones(lth,1);
end
scalarb = (length(b) == 1);
if scalarb
   b = b*ones(lth,1);
end
% If a == 1, then gamma is exponential. (Devroye, page 405).
k = find(a == 1);
if any(k)
   r(k) = -b(k) .* log(rand(size(k)));
end
k = find(a < 1 & a > 0);
% (Devroye, page 418 Johnk's generator)
if any(k)
  c = zeros(lth,1);
  d = zeros(lth,1);
  c(k) = 1 ./ a(k);
  d(k) = 1 ./ (1 - a(k));
  accept = k;
  while ~isempty(accept)
    u = rand(size(accept));
    v = rand(size(accept));
    x = u .^ c(accept);
    y = v .^ d(accept);
    k1 = find((x + y) <= 1);
    if ~isempty(k1)
      e = -log(rand(size(k1)));
      r(accept(k1)) = e .* x(k1) ./ (x(k1) + y(k1));
      accept(k1) = [];
    end
  end
  r(k) = r(k) .* b(k);
end  
% Use a rejection method for a > 1.
k = find(a > 1);
% (Devroye, page 410 Best's algorithm)
bb = zeros(size(a));
c  = bb;
if any(k)
  bb(k) = a(k) - 1;
  c(k) = 3 * a(k) - 3/4;
  accept = k;
  count = 1;
  while ~isempty(accept)
    m = length(accept);
    u = rand(m,1);
    v = rand(m,1);
    w = u .* (1 - u);
    y = sqrt(c(accept) ./ w) .* (u - 0.5);
    x = bb(accept) + y;
    k1 = find(x >= 0);
    if ~isempty(k1)
      z = 64 * (w .^ 3) .* (v .^ 2);
      k2 = (z(k1) <= (1 - 2 * (y(k1) .^2) ./ x(k1)));
      k3 = k1(find(k2));
      r(accept(k3)) = x(k3);
      k4 = k1(find(~k2));
      k5 = k4(find(log(z(k4)) <= (2*(bb(accept(k4)).*log(x(k4)./bb(accept(k4)))-y(k4)))));
      r(accept(k5)) = x(k5);
      omit = [k3; k5];
      accept(omit) = [];
    end
  end
  r(k) = r(k) .* b(k);
end
r = reshape(r,rows,columns);
```

**ggcode**
```matlab
x = -6:0.01:6;
rho = [1 1.5 2 4 10];
p = [];
for k = 1:length(rho)
    p = [p exp(-abs(x').^rho(k)) / (2*gamma(1+1/rho(k)))];
end
figure, hold on; set(gca,'fontsize',14);
plot(x,p,'linewidth',2);
str = num2str(rho');
clear str2;
for k = 1:length(rho)
    str2(k,:) = ['\it\rho =' str(k,:)];
end
legend(str2); xlabel('\itx'); ylabel('\itGG(x\rm;\it\rho)'); xlim([-6 6])
```

**ggcode2**
```matlab
x = -10:0.01:10;
mu=[-3 -1 2];
beta= [1 5 2]; sbeta = sqrt(beta);
rho=[1 2 10];
clear p2;
for k = 1:length(mu)
    p2(:,k) = exp(-abs(sbeta(k)*(x-mu(k))').^rho(k)) * sbeta(k) / (2*gamma(1+1/rho(k)));
end
figure, hold on; set(gca,'fontsize',14);
plot(x,p2,'linewidth',2);
rstr = num2str(rho'); mstr = num2str(mu'); bstr = num2str(beta');
clear str2;
for k = 1:length(rho)
    str2(k,:) = ['\it\mu = ' mstr(k,:) ', \it\beta = ' bstr(k,:) ', \it\rho = ' rstr(k,:) ];
end
legend(str2,'Location','NE'); xlabel('\itx'); ylabel('\itGG(x\rm;\it\mu,\it\beta,\it\rho)');
set(gca,'XTick',-10:10);xlim([-8 8]);
```

**ggcode3**
```matlab
clear x h b;
figure, hold on;
mu = [-3 -1 2];
beta = [1 5 2];
rho = [1 2 10];
delt = 0.15;
cents = -12:delt:12;
for k = 1:length(mu)
    x(k,:) = gg6(1,100000,mu(k),beta(k),rho(k));
    h(k,:) = histc(x(k,:),cents);
end
bar(cents,h(1,:)/(100000*delt),'b');
bar(cents,h(2,:)/(100000*delt),'g');
bar(cents,h(3,:)/(100000*delt),'r');
xlim([-8 8]); set(gca,'XTick',-10:10);
set(gca,'fontsize',14);
xlabel('\itx \rm(bin)'); ylabel('normalized histogram');
```

**ggcode4**
```matlab
clear x h b;
x = -10:0.01:10;
mu=[-2 0 2];
beta= [1 1 1]; sbeta = sqrt(beta);
rho=[1 2 10];
alpha = [0.5 0.2 0.3];
p = zeros(size(x));
for j = 1:length(mu)
    d(j,:) = alpha(j) * exp(-abs(sbeta(j)*(x-mu(j))).^rho(j)) * sbeta(j) / (2*gamma(1+1/rho(j)));
    p = p + d(j,:);
end
figure, hold on; set(gca,'fontsize',14);
plot(x,d','g');
plot(x,p,'linewidth',2);
set(gca,'XTick',-10:10); xlim([-8 6]); ylim([0 0.3]);
xlabel('\itx');ylabel('\itp_M(x)');    

N = 100000;
clear x h b;
figure, hold on;set(gca,'fontsize',14);
mu=[-2 0 2];
beta= [1 1 1]; sbeta = sqrt(beta);
rho=[1 2 10];
alpha = [0.5 0.2 0.3];  
for k = 1:length(mu)
    x(k,:) = gg6(1,N,mu(k),beta(k),rho(k));
end
nrnd = ceil(10*rand(1,N));
ind = 1 * (nrnd <= 5) + 2 * (nrnd > 5).*(nrnd <= 7) + 3 * (nrnd > 7);  
[h,b] = hist([x(1,ind==1) x(2,ind==2) x(3,ind==3)],150);
delt = b(2)-b(1);
bar(b,h/(N*delt),'b');
set(gca,'XTick',-10:10); xlim([-8 6]); ylim([0 0.3]);
xlabel('\itx \rm(bin)'); ylabel('normalized histogram');
```

**ICA_fig.m**
```matlab
N=2000;
A = [1 4;4 1];
s = gg6(2,N,[0 0],[1 3],[1.5 1.5]);
x = A*s;
[h1,b1] = hist(s(1,:),50);
[h2,b2] = hist(s(2,:),50);
figure, hold on; set(gca,'fontsize',14);
subplot(2,4,1); set(gca,'fontsize',14);
plot(s(1,:),s(2,:),'b.'); axis(4*[-1 1 -1 1]); xlabel('\its_{\rm1}'); ylabel('\its_{\rm2}');
subplot(2,4,2); set(gca,'fontsize',14);
bar(b2,h2/(N*(b2(2)-b2(1))));  axis(4*[-1 1 0 1/4]); xlabel('\its_{\rm2}'); ylabel('norm. histogram');
subplot(2,4,5); set(gca,'fontsize',14);
bar(b1,h1/(N*(b1(2)-b1(1))));  axis(4*[-1 1 0 1/4]);  xlabel('\its_{\rm1}'); ylabel('norm. histogram');
subplot(2,4,3); hold on; set(gca,'fontsize',14);
subplot(2,4,3); plot(x(1,:),x(2,:),'g.'); axis(15*[-1 1 -1 1]);
subplot(2,4,3); plot([0 A(1,1)],[0 A(2,1)],'r-','LineWidth',2);
subplot(2,4,3); plot([0 A(1,2)],[0 A(2,2)],'r-','LineWidth',2);
xlabel('\itx_{\rm1}'); ylabel('\itx_{\rm2}');
[h1,b1] = hist(x(1,:),50);
[h2,b2] = hist(x(2,:),50);
subplot(2,4,4); set(gca,'fontsize',14);
bar(b2,h2/(N*(b2(2)-b2(1))),'g');  axis([-15 15 0 0.25]); xlabel('\itx_{\rm2}'); ylabel('norm. histogram');
subplot(2,4,7); set(gca,'fontsize',14);
bar(b1,h1/(N*(b1(2)-b1(1))),'g');  axis([-15 15 0 0.25]);  xlabel('\itx_{\rm1}'); ylabel('norm. histogram');
```