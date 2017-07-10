clear;clc;
file = '/Volumes/LabJet2017/dieckmann2017/d3/';
load([file,'energy.mat']);

num = 40;
xx = linspace(0,120,num);
% aa = mp(1);
aa = 1;   % no normalization

figure('visible','on','Position',[1 1 800 600]);
semilogy(xx,mp/aa,'-m','linewidth',2.0);
hold on;
semilogy(xx,tpe/aa,'--m','linewidth',3.0);
semilogy(xx,eneel/aa,'-c','linewidth',1.0);
semilogy(xx,enepl/aa,'--c','linewidth',3.0);
semilogy(xx,eneer/aa,'-g','linewidth',1.0);
semilogy(xx,enepr/aa,'--g','linewidth',3.0);

semilogy(xx,mf/aa,'-r','linewidth',2.0);
semilogy(xx,tfe/aa,'--r','linewidth',3.0);
semilogy(xx,ee/aa,'-b','linewidth',2.0);
semilogy(xx,bb/aa,'--b','linewidth',2.0);

legend('location','best','mp','tpe','eneel','enepl','eneer','enepr','mf','tfe','ee','bb');

set(gca,'Fontsize',36);
set(gca,'XLim',[0, 120]);%,'YLim',[1e0,1e7]);

saveas(gcf,[file,'enex','.fig']);
%    export_fig('gcf',[file,'x-px-limity',num2str(time),'.png']); 
   
   
   
   
% end