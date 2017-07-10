clear all;clc;

me  = 9.1e-31;
mi  = me*100;
c   = 3e8;
qe  = 1.6e-19;
ne  = 1;
n0  = 1;
eps = 8.9e-12;

wpe = sqrt(n0*qe*qe/eps/mi);
ld  = c/wpe;

dx  = ld/100;

num = 40;
tfe = zeros(1,num);
tpe = zeros(1,num);

ee = zeros(1,num);
eex = zeros(1,num);
eey = zeros(1,num);
bb = zeros(1,num);
mf = zeros(1,num);

eneel = zeros(1,num);
enepl = zeros(1,num);
eneer = zeros(1,num);
enepr = zeros(1,num);
enee = zeros(1,num);
enep = zeros(1,num);
enbe = zeros(1,num);
enbi = zeros(1,num);
mp = zeros(1,num);


file = '/Volumes/LabJet2017/dieckmann2017/ep0/';

for time = 1:1:num
    time
    [b,h] = lv([file,num2str(time,'%04d'),'.sdf']);
    [b1,h1] = lv([file,'6',num2str(time,'%04d'),'.sdf']);
   
    
    ez = gd(b,h,'ez');
    ey = gd(b,h,'ey');
    ex = gd(b,h,'ex');
    bz = gd(b,h,'bz');
    by = gd(b,h,'by');
    bx = gd(b,h,'bx');
    
    ee(time) = 0.5*eps*dx^2*sum(sum((ex.^2+ey.^2+ez.^2)));
    eex(time) = 0.5*eps*dx^2*sum(sum((ex.^2)));
    eey(time) = 0.5*eps*dx^2*sum(sum((ey.^2)));
    bb(time) = 0.5*eps*dx^2*sum(sum(((bx.^2+by.^2+bz.^2)*c^2))); 
    mf(time) = ee(time)+bb(time);
    tfe(time) = gd(b,h,'total_field_energy');
    
    tpe(time) = gd(b,h,'total_particle_energy');
    
    gamel = gd(b1,h1,'gamma/subset_ll/el');
    gampl = gd(b1,h1,'gamma/subset_ll/pl');
    wel   = gd(b1,h1,'weight/subset_ll/el');
    wpl   = gd(b1,h1,'weight/subset_ll/pl');
    
    gamer = gd(b1,h1,'gamma/subset_rr/er');
    gampr = gd(b1,h1,'gamma/subset_rr/pr');
    wer   = gd(b1,h1,'weight/subset_rr/er');
    wpr   = gd(b1,h1,'weight/subset_rr/pr');
    
    eneel(time) = sum((gamel-1)*me*c*c*mean(wel))*10;
    enepl(time) = sum((gampl-1)*mi*c*c*mean(wpl))*10;
    eneer(time) = sum((gamer-1)*me*c*c*mean(wer))*10;
    enepr(time) = sum((gampr-1)*mi*c*c*mean(wpr))*10;
    
%     gambe = gd(b1,h1,'gamma/subset_back/ebg');
%     gambi = gd(b1,h1,'gamma/subset_back/pbg');
%     wbe   = gd(b1,h1,'weight/subset_back/ebg');
%     wbi   = gd(b1,h1,'weight/subset_back/pbg');
%     enbe(time) = sum((gambe-1)*me*c*c*mean(wbe))*100;
%     enbi(time) = sum((gambi-1)*mi*c*c*mean(wbi))*100;
    
    mp(time) = eneel(time)+enepl(time)+eneer(time)+enepr(time);
    
    
end

    save([file,'/energy.mat'],'ee','eex','eey','bb','mf','tfe','eneel','enepl','eneer','enepr','mp','tpe');
%     save([file,'/energy.mat'],'ee','bb','mf','tfe','enee','enei','mp','tpe');
    xx = linspace(0,120,num);
%    figure;
    figure('visible','on','Position',[1 1 1200 1000]);
    semilogy(xx,mf,'-r','linewidth',1.0);
    hold on;
    semilogy(xx,tfe,'--r','linewidth',3.0);
    semilogy(xx,ee,'-b','linewidth',1.0);
    semilogy(xx,eex,'-y','linewidth',1.0);
    semilogy(xx,eey,'--y','linewidth',1.0);
    semilogy(xx,bb,'--b','linewidth',3.0);
    
    semilogy(xx,mp,'-m','linewidth',1.0);
    semilogy(xx,tpe,'--m','linewidth',3.0);
    semilogy(xx,eneel,'-c','linewidth',1.0);
    semilogy(xx,enepl,'--c','linewidth',3.0);
    semilogy(xx,eneer,'-g','linewidth',1.0);
    semilogy(xx,enepr,'--g','linewidth',3.0);
%     legend('location','best','mf','tfe','ee','bb','mp','tpe','enee','enei','enbe','enbi');
    legend('location','best','mf','tfe','ee','eex','eey','bb','mp','tpe','eneel','enepl','eneer','enepr');
    
   set(gca,'Fontsize',36);
   set(gca,'XLim',[0, 120]);%,'YLim',[1e0,1e7]);
%    set(gca,'XLim',[0, 200],'YLim',[-15,15]);
%    xlabel('x/\lambda_e');
%    ylabel('energy ratio');
%    hold on;
%    semilogy(xx,bb/enet,'-b');
%    ylabel('py/m_ec');
%    axis xy;
%    colorbar;
%    colormap(jet);
%    caxis([4,10]);
%    export_fig('gcf',[file,'x-px-limity',num2str(time),'.png']); 
   
   
   
   
% end