clear;clc;

load('wjet.mat');
me  = 9.1e-31;
mi  = me*100;
c   = 3e8;
qe  = 1.6e-19;
ne  = 1;
n0  = 1;
v0  = 0.2*c;
eps = 8.9e-12;

wpe = sqrt(n0*qe*qe/eps/me);
wpi = sqrt(n0*qe*qe/eps/mi);
ld  = c/wpi;

e0 = me*wpe*c/qe;
b0 = e0/c;
pe0 = me*v0;
pi0 = mi*v0;

res = 300;

file = '/Volumes/LabJet2017/dieckmann2017/ep0/';

for time = 	1:1:41
    time
    [b,h] = lv([file,'6',num2str(time-1,'%04d'),'.sdf']);
    
    pxel = gd(b,h,'px/subset_ll/el')/pe0;
    pxpl = gd(b,h,'px/subset_ll/pl')/pi0;
    
    pxer = gd(b,h,'px/subset_rr/er')/pe0;
    pxpr = gd(b,h,'px/subset_rr/pr')/pi0;
    
    pxe = [pxel;pxer];
    pxp = [pxpl;pxpr];
    
    xel = gd(b,h,'grid/subset_ll/el');
    xel = xel.x/ld;
    xpl = gd(b,h,'grid/subset_ll/pl');
    xpl = xpl.x/ld;
    
    xer = gd(b,h,'grid/subset_rr/er');
    xer = xer.x/ld;
    xpr = gd(b,h,'grid/subset_rr/pr');
    xpr = xpr.x/ld;
    
    xe = [xel;xer];
    xp = [xpl;xpr];
    
    
    ne = hist3([xe,pxe],[res,res]);
    fxe = linspace(min(xe),max(xe),res);
    fpxe = linspace(min(pxe),max(pxe),res);
    ne0 = max(max(ne));
    
    np = hist3([xp,pxp],[res,res]);
    fxp = linspace(min(xp),max(xp),res);
    fpxp = linspace(min(pxp),max(pxp),res);
    np0 = max(max(np));
    
    
    figure('visible','off','position',[100,100,800,600]);
    subplot(2,1,1);
    imagesc(fxe,fpxe,log10(ne'/ne0));
    set(gca,'fontsize',36,'xlim',[-30,30],'ylim',[-4,4]);
    set(gcf,'color','w');
    ylabel('pe_x/p_{e0}');
    xlabel('x');
    axis xy;
    colormap(a);
    colorbar;
    caxis([-1.5, 0]);
    
%     figure('visible','on','position',[100,100,800,600]);
    subplot(2,1,2)
    imagesc(fxp,fpxp,log10(np'/np0));
    set(gca,'fontsize',36,'xlim',[-30,30],'ylim',[-0.5,1.5]);
    set(gcf,'color','w');
    ylabel('pi_x/p_{i0}');
    xlabel('x');
    axis xy;
    colormap(a);
    colorbar;
    caxis([-1.5, 0]);
    
    
    export_fig([file,'ps2_snap',num2str(time-1),'.png'],'-painters'); 
    close(gcf);
end