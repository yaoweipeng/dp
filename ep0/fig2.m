clear;clc;

load('wjet.mat');
me  = 9.1e-31;
mi  = me*100;
c   = 3e8;
qe  = 1.6e-19;
ne  = 1;
n0  = 1;
eps = 8.9e-12;
v0 = 0.2;

wpi = sqrt(n0*qe*qe/eps/mi);
wpe = sqrt(n0*qe*qe/eps/me);
ld  = c/wpi;

e0 = me*wpe*c/qe;
b0 = e0/c;

file = '/Volumes/LabJet2017/dieckmann2017/ep0/';

for time = 	1:1:41;
    time
    [b,h] = lv([file,num2str(time-1,'%04d'),'.sdf']);

    if time == 1
        ex  = gd(b,h,'ex')/e0;
        ey  = gd(b,h,'ey')/e0;
        bz  = gd(b,h,'bz')/b0;
    elseif time > 1
        ex  = gd(b,h,'ex_averaged')/e0;
        ey  = gd(b,h,'ey_averaged')/e0;
        bz  = gd(b,h,'bz_averaged')/b0;
    end
    
    xx = linspace(-30,30,6000);
    yy = linspace(0,2.4,240);
    
    figure('visible','off','position',[100,100,800,1000]);
    subplot(3,1,1);
    imagesc(xx,yy,ex');
    set(gca,'fontsize',36,'xlim',[-30,30]);
    set(gcf,'color','w');
    xlabel('x');
    ylabel('y');
    axis xy;
    colormap(redblue);
    colorbar;
    caxis([-0.01, 0.01]);
    
%     figure('visible','on','position',[100,100,800,600]);
    subplot(3,1,2);
    imagesc(xx,yy,ey');
    set(gca,'fontsize',36,'xlim',[-30,30]);
    set(gcf,'color','w');
    xlabel('x');
    ylabel('y');
    axis xy;
    colormap(redblue);
    colorbar;
    caxis([-0.02, 0.02]);
    
%     figure('visible','on','position',[100,100,800,600]);
    subplot(3,1,3);
    imagesc(xx,yy,v0*bz');
    set(gca,'fontsize',36,'xlim',[-30,30]);
    set(gcf,'color','w');
    xlabel('x');
    ylabel('y');
    axis xy;
    colormap(redblue);
    colorbar;
    caxis([-0.02,0.02]);
    
    export_fig([file,'field_snap',num2str(time-1),'.png'],'-painters'); 
    close(gcf);
    
end