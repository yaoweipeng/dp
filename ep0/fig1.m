clear;clc;

load('wjet.mat');
me  = 9.1e-31;
mi  = me*100;
c   = 3e8;
qe  = 1.6e-19;
ne  = 1;
n0  = 1;
eps = 8.9e-12;

wpe = sqrt(n0*qe*qe/eps/mi);
ld  = c/wpe;

e0 = me*wpe*c/qe;
b0 = e0/c;
v0= 0.2;

nx = 6000;
ny = 240;
lx = 60;
ly = 2.4;
dx = lx/nx;
dy = ly/ny;

file = '/Volumes/LabJet2017/dieckmann2017/ep0/';

for time = 	40:1:40;
    time
    [b,h] = lv([file,num2str(time,'%04d'),'.sdf']);

    ex  = gd(b,h,'ex');   % increase max(colormap)
    ey  = gd(b,h,'ey');
    
    x1  = -30;
    x2  = 30;
    r1  = floor((x1+30)/(lx/nx))+1;
    r2  = floor((x2+30)/(lx/nx));
%     ex(1:r1,:) = 0;
%     ex(r2:nx,:) = 0;
    ex  = ex(r1:r2,:);
    ey  = ey(r1:r2,:);
    ee  = ex + i*ey;
    ee2 = abs(fftshift(fft2(ee))).^2;
    ee0 = max(max(ee2));
    
    nnx = r2-r1+1;
    nny = ny;
    kx = ((1:nnx)-nnx/2)/nnx/dx/v0;
    ky = -((1:nny)-nny/2)/nny/dy/v0;
    
    figure('visible','on','position',[100,100,800,800]);
    imagesc(ky,kx,log10(ee2));
%     imagesc(ky,kx,log10(ee2));
    set(gca,'fontsize',36);
%     set(gca,'xlim',[0,200],'ylim',[0,200]);
    set(gcf,'color','w');
    xlabel('ky');
    ylabel('kx');
    axis xy;
    colormap(jet);
    colorbar;
    caxis([-2, 1]);
    
    
%     export_fig([file,'ex',num2str(time),'.png'],'-painters'); 
    
end