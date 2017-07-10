clear;clc;

load('wjet.mat');
me  = 9.1e-31;
mi  = me*100;
c   = 3e8;
qe  = 1.6e-19;
ne  = 1;
n0  = 1;
v0 = 0.2*c;
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

for time = 	36:1:41
    time
    [b,h] = lv([file,'6',num2str(time-1,'%04d'),'.sdf']);
    
    pxel = gd(b,h,'px/subset_ll/el')/pe0;
    pyel = gd(b,h,'py/subset_ll/el')/pe0;
    
    pxer = gd(b,h,'px/subset_rr/er')/pe0;
    pyer = gd(b,h,'py/subset_rr/er')/pe0;
    
%     pxe = [pxel;pxer];
%     pye = [pyel;pyer];
%     pxe = pxel;
%     pye = pyel;

    xel = gd(b,h,'grid/subset_ll/el');
    xel = xel.x/ld;
    xer = gd(b,h,'grid/subset_rr/er');
    xer = xer.x/ld;
    
%     xe = [xel;xer];

%     xe = xel;
    
    %----
    pxpl = gd(b,h,'px/subset_ll/pl')/pi0;
    pypl = gd(b,h,'py/subset_ll/pl')/pi0;
    
    pxpr = gd(b,h,'px/subset_rr/pr')/pi0;
    pypr = gd(b,h,'py/subset_rr/pr')/pi0;
    
%     pxp = [pxpl;pxpr];
%     pyp = [pypl;pypr];
%     pxp = pxpl;
%     pyp = pypl;
    
    xpl = gd(b,h,'grid/subset_ll/pl');
    xpl = xpl.x/ld;
    xpr = gd(b,h,'grid/subset_rr/pr');
    xpr = xpr.x/ld;
    
%     xp = [xpl;xpr];
%     xp = xpl;
    
%     % pick of the paper
%     r1 = find(xe >  -4.5 & xe < -4.2);
%     r2 = find(xe >  1.9 & xe <  2.2);
%     r3 = find(xe >  8.3 & xe <  8.6);

    % pick of mine
%     r1 = find(xe >  -8 & xe < -4);
%     r2 = find(xe >  1 & xe <  5);
%     r3 = find(xe >  8 & xe <  12);
    
%     pxe1 = pxe(r1);pye1 = pye(r1);
%     pxe2 = pxe(r2);pye2 = pye(r2);
%     pxe3 = pxe(r3);pye3 = pye(r3);
    
    
    nel1 = hist3([pxel,pyel],[res,res]);
    fpxel = linspace(min(pxel),max(pxel),res);
    fpyel = linspace(min(pyel),max(pyel),res);
    nel0 = max(max(nel1));

    figure('visible','off','position',[100,100,1000,800]);
    subplot(2,2,1);
    imagesc(fpxel,fpyel,log10(nel1'/nel0));
    set(gca,'fontsize',36,'ylim',[-5,5],'xlim',[-5,5]);
    set(gcf,'color','w');
    ylabel('pel_y/p_0');
    xlabel('pel_x/p_0');
    axis xy;
    colormap(a);
    colorbar;
    caxis([-2, 0]);
    
    ner1 = hist3([pxer,pyer],[res,res]);
    fpxer = linspace(min(pxer),max(pxer),res);
    fpyer = linspace(min(pyer),max(pyer),res);
    ner0 = max(max(ner1));

%     figure('visible','on','position',[100,100,1000,400]);
    subplot(2,2,2);
    imagesc(fpxer,fpyer,log10(ner1'/ner0));
    set(gca,'fontsize',36,'ylim',[-5,5],'xlim',[-5,5]);
    set(gcf,'color','w');
    ylabel('per_y/p_0');
    xlabel('per_x/p_0');
    axis xy;
    colormap(a);
    colorbar;
    caxis([-2, 0]);

    npl1 = hist3([pxpl,pypl],[res,res]);
    fpxpl = linspace(min(pxpl),max(pxpl),res);
    fpypl = linspace(min(pypl),max(pypl),res);
    npl0 = max(max(npl1));

%     figure('visible','on','position',[100,100,800,600]);
    subplot(2,2,3);
    imagesc(fpxpl,fpypl,log10(npl1'/npl0));
    set(gca,'fontsize',36,'ylim',[-1,1],'xlim',[-0.5,1.5]);
    set(gcf,'color','w');
    ylabel('pil_y/p_0');
    xlabel('pil_x/p_0');
    axis xy;
    colormap(a);
    colorbar;
    caxis([-2, 0]);
    
    npr1 = hist3([pxpr,pypr],[res,res]);
    fpxpr = linspace(min(pxpr),max(pxpr),res);
    fpypr = linspace(min(pypr),max(pypr),res);
    npr0 = max(max(npr1));

%     figure('visible','on','position',[100,100,800,600]);
    subplot(2,2,4);
    imagesc(fpxpr,fpypr,log10(npr1'/npr0));
    set(gca,'fontsize',36,'ylim',[-1,1],'xlim',[-0.5,1.5]);
    set(gcf,'color','w');
    ylabel('pir_y/p_0');
    xlabel('pir_x/p_0');
    axis xy;
    colormap(a);
    colorbar;
    caxis([-2, 0]);
    
    
    export_fig([file,'pxpy',num2str(time-1),'.png'],'-painters'); 
    close(gcf)













    
%     ne2 = hist3([pxe2,pye2],[res,res]);
%     fpxe = linspace(min(pxe2),max(pxe2),res);
%     fpye = linspace(min(pye2),max(pye2),res);
% %     ne0 = max(max(ne1));
%     
%     figure('visible','on','position',[100,100,800,600]);
%     imagesc(fpxe,fpye,log10(ne2'/ne0));
%     set(gca,'fontsize',36,'ylim',[-1.2,1.2],'xlim',[-2,2]);
%     set(gcf,'color','w');
%     ylabel('p_y/p_0');
%     xlabel('p_x/p_0');
%     axis xy;
%     colormap(jet);
%     colorbar;
%     caxis([-4.5, -1]);
%     
%     ne3 = hist3([pxe3,pye3],[res,res]);
%     fpxe = linspace(min(pxe3),max(pxe3),res);
%     fpye = linspace(min(pye3),max(pye3),res);
% %     ne0 = max(max(ne1));
%     
%     figure('visible','on','position',[100,100,800,600]);
%     imagesc(fpxe,fpye,log10(ne3'/ne0));
%     set(gca,'fontsize',36,'ylim',[-1.2,1.2],'xlim',[-2,2]);
%     set(gcf,'color','w');
%     ylabel('p_y/p_0');
%     xlabel('p_x/p_0');
%     axis xy;
%     colormap(jet);
%     colorbar;
%     caxis([-4.5, -1.5]);
    
    
%     export_fig([file,'ex',num2str(time),'.png'],'-painters'); 
    
end