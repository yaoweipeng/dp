clear;clc;

load('wjet.mat');
me  = 9.1e-31;
mi  = me*1;
c   = 3e8;
qe  = 1.6e-19;
ne  = 1;
n0  = 1;
v0 = 0.2*c;
eps = 8.9e-12;

wpe = sqrt(n0*qe*qe/eps/me);
ld  = c/wpe;

e0 = me*wpe*c/qe;
b0 = e0/c;
p0 = me*v0;

res = 100;

file = '/Volumes/LabJet2017/dieckmann2017/d2/';

for time = 	16:1:16
    time;
    [b,h] = lv([file,'6',num2str(time,'%04d'),'.sdf']);
    
    pxel = gd(b,h,'px/subset_ll/el')/p0;
    pyel = gd(b,h,'py/subset_ll/el')/p0;
    
    pxer = gd(b,h,'px/subset_rr/er')/p0;
    pyer = gd(b,h,'px/subset_rr/er')/p0;
    
    pxe = [pxel;pxer];
    pye = [pyel;pyer];
    
    xel = gd(b,h,'grid/subset_ll/el');
    xel = xel.x/ld;
    xer = gd(b,h,'grid/subset_rr/er');
    xer = xer.x/ld;
    
    xe = [xel;xer];
    xxx = 5.2;
%     r1 = find(xe > -4.2 & xe < -3.9);
%     r2 = find(xe >  1.9 & xe <  2.2);
    r3 = find(xe >  xxx & xe <  xxx+0.3);
    
%     pxe1 = pxe(r1);pye1 = pye(r1);
%     pxe2 = pxe(r2);pye2 = pye(r2);
    pxe3 = pxe(r3);pye3 = pye(r3);
    
    a1 = sum((pxe3-0.1).^2);
    a2 = sum((pye3).^2);
    A  = a1/a2 - 1
    
    
%     ne1 = hist3([pxe1,pye1],[res,res]);
%     fpxe = linspace(min(pxe1),max(pxe1),res);
%     fpye = linspace(min(pye1),max(pye1),res);
%     ne0 = max(max(ne1));
%     
%     
%     figure('visible','on','position',[100,100,800,600]);
%     imagesc(fpye,fpxe,log10(ne1/ne0));
%     set(gca,'fontsize',36,'xlim',[-1.2,1.2],'ylim',[-2,2]);
%     set(gcf,'color','w');
%     xlabel('p_y/p_0');
%     ylabel('p_x/p_0');
%     axis xy;
%     colormap(jet);
%     colorbar;
%     caxis([-4.5, 0]);
    
%     ne2 = hist3([pxe2,pye2],[res,res]);
%     fpxe = linspace(min(pxe2),max(pxe2),res);
%     fpye = linspace(min(pye2),max(pye2),res);
% %     ne0 = max(max(ne1));
%     
%     figure('visible','on','position',[100,100,800,600]);
%     imagesc(fpye,fpxe,log10(ne2/ne0));
%     set(gca,'fontsize',36,'xlim',[-1.2,1.2],'ylim',[-2,2]);
%     set(gcf,'color','w');
%     xlabel('p_y/p_0');
%     ylabel('p_x/p_0');
%     axis xy;
%     colormap(jet);
%     colorbar;
%     caxis([-4.5, -1]);
    
%     ne3 = hist3([pxe3,pye3],[res,res]);
%     fpxe = linspace(min(pxe3),max(pxe3),res);
%     fpye = linspace(min(pye3),max(pye3),res);
% %     ne0 = max(max(ne1));
%     
%     figure('visible','on','position',[100,100,800,600]);
%     imagesc(fpye,fpxe,log10(ne3/ne0));
%     set(gca,'fontsize',36,'xlim',[-1.2,1.2],'ylim',[-2,2]);
%     set(gcf,'color','w');
%     xlabel('p_y/p_0');
%     ylabel('p_x/p_0');
%     axis xy;
%     colormap(jet);
%     colorbar;
%     caxis([-4.5, -1.5]);
    
    
%     export_fig([file,'ex',num2str(time),'.png'],'-painters'); 
    
end