clear;clc;
me  = 9.1e-31;
mi  = me*100;
c   = 3e8;
qe  = 1.6e-19;
ne  = 1;
eps = 8.9e-12;
wpe = sqrt(ne*qe*qe/eps/me);
wpi = sqrt(ne*qe*qe/eps/mi);
lambda = c/wpi;
res = 2000;

file = '/Volumes/LabJet2017/dieckmann2017/ep0/';

for time = 1:1:41;
    time
    [b,h] = lv([file,'6',num2str(time-1,'%04d'),'.sdf']);

    gamel = gd(b,h,'gamma/subset_ll/el');
    gamer = gd(b,h,'gamma/subset_rr/er');

    game = [gamel;gamer];

    gampl = gd(b,h,'gamma/subset_ll/pl');
    gampr = gd(b,h,'gamma/subset_rr/pr');

    gamp = [gampl;gampr];

    % posel = gd(b,h,'grid/subset_ll/el');
    % xel   = posel.x./lambda;
    % yel   = posel.y./lambda;
    % 
    % poser = gd(b,h,'grid/subset_rr/er');
    % xer   = poser.x./lambda;
    % yer   = poser.y./lambda;
    % 
    % xe = [xel;xer];
    % 
    % rx   = find(xe > -8 & xe < 0);
    % game  = game(rx);

    [Ne,Ee] = hist(game,res);
    [Nel,Eel] = hist(gamel,res);
    [Ner,Eer] = hist(gamer,res);

    [Np,Ep] = hist(gamp,res);
    [Npl,Epl] = hist(gampl,res);
    [Npr,Epr] = hist(gampr,res);

    figure('visible','off','position',[100,100,1000,800]);
    subplot(1,2,1);
    loglog(Ee, Ne, '-r','linewidth',2.0);
    set(gca,'color','w','fontsize',36,'ylim',[1,1e5]);
    hold on;grid on;
    loglog(Eel,Nel, '--b','linewidth',1.0);
    loglog(Eer,Ner, '--g','linewidth',1.0);
    legend('location','northeast','l+r','l','r');

    subplot(1,2,2);
    loglog(Ep, Np, '-r','linewidth',2.0);
    set(gca,'color','w','fontsize',36,'ylim',[1,1e5]);
    hold on;grid on;
    loglog(Epl,Npl, '--b','linewidth',1.0);
    loglog(Epr,Npr, '--g','linewidth',1.0);
    legend('location','northeast','l+r','l','r');
    
    export_fig([file,'spe_snap',num2str(time-1),'.png'],'-painters'); 
    close(gcf);
    
end