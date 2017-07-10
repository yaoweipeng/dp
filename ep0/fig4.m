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

for time = 	1:1:1;
    time
    [b,h] = lv([file,num2str(time-1,'%04d'),'.sdf']);

    
    el = gd(b,h,'number_density/el');
    er = gd(b,h,'number_density/er');
    pl = gd(b,h,'number_density/pl');
    pr = gd(b,h,'number_density/pr');
    
    if time == 1
        ex  = gd(b,h,'ex')/e0;
        ey  = gd(b,h,'ey')/e0;
        bz  = gd(b,h,'bz')/b0;
    elseif time > 1
        ex  = gd(b,h,'ex_averaged')/e0;
        ey  = gd(b,h,'ey_averaged')/e0;
        bz  = gd(b,h,'bz_averaged')/b0;
    end
       
    el2 = sum(el,2)/240;
    er2 = sum(er,2)/240;
    pl2 = sum(pl,2)/240;
    pr2 = sum(pr,2)/240;
    
    ex2 = sum(ex,2)/240;
    ey2 = sum(ey,2)/240;
    bz2 = sum(bz,2)/240;
    
    xx = linspace(-30,30,6000);
%     yy = linspace(0,2.4,240);
    
    figure('visible','off','position',[100,100,1000,800]);
    subplot(2,2,1);
    plot(xx,el2+er2,'-r','linewidth',2.0);
    hold on;
    plot(xx,el2,'-b');
    plot(xx,er2,'-g');
    set(gca,'fontsize',36,'xlim',[-30,30],'ylim',[0,3]);
    set(gcf,'color','w');
    xlabel('x');
    ylabel('electron');
    legend('location','northwest','l+r','l','r');
    grid on;
    
%     figure('visible','on','position',[100,100,800,600]);
    subplot(2,2,2);
    plot(xx,pl2+pr2,'-r','linewidth',2.0);
    hold on;
    plot(xx,pl2,'-b');
    plot(xx,pr2,'-g');
    set(gca,'fontsize',36,'xlim',[-30,30],'ylim',[0,3]);
    set(gcf,'color','w');
    xlabel('x');
    ylabel('ion');
    legend('location','northwest','l+r','l','r');
    grid on;
    
    subplot(2,2,3);
    plot(xx,ex2,'-r');
%     hold on;
%     plot(xx,ey2,'-g');
%     plot(xx,bz2,'-g');
    set(gca,'fontsize',36,'xlim',[-30,30],'ylim',[-0.01,0.01]);
    set(gcf,'color','w');
    xlabel('x');
    ylabel('Ex');
%     legend('location','northwest','ex','ey');
    grid on;
    
    subplot(2,2,4);
    plot(xx,bz2*v0,'-r');
    hold on;
    plot(xx,ey2,'--b');
    set(gca,'fontsize',36,'xlim',[-30,30],'ylim',[-0.01,0.01]);
    set(gcf,'color','w');
    xlabel('x');
    ylabel('Bz & Ey');
    legend('location','northwest','Bz*v0','Ey');
    grid on;
    
    export_fig([file,'axial_ave_snap',num2str(time-1),'.png'],'-painters'); 
    close(gcf);
    
end